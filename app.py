from fastapi import FastAPI, HTTPException
from models import UserData, Consent, DataAccessRequest, SharedDataResponse
from privacy_engine import enforce_consent, is_consent_valid
from synthetic_data import generate_user
from audit import log_access, detect_anomalies
from policies import get_allowed_fields
from db import users_db, consents_db

app = FastAPI()

@app.post("/generate_user/{user_id}")
def create_user(user_id: str):
    user = generate_user(user_id)
    users_db[user_id] = user
    return {"status": "created", "user": user}

@app.post("/consent")
def add_consent(consent: Consent):
    consents_db[consent.user_id] = consent.dict()
    return {"status": "consent added"}

@app.post("/data_access", response_model=SharedDataResponse)
def access_data(request: DataAccessRequest):
    user = users_db.get(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    consent = consents_db.get(request.user_id)
    if not consent or not is_consent_valid(consent):
        raise HTTPException(status_code=403, detail="Consent invalid or missing")

    allowed_fields = get_allowed_fields(request.requester)
    requested_fields = consent["allowed_fields"]
    anomalies = detect_anomalies(request.requester, requested_fields, allowed_fields)

    if anomalies:
        raise HTTPException(status_code=403, detail="Policy violation detected")

    masked_data = enforce_consent(user, requested_fields)
    log_access(request.requester, request.user_id, requested_fields)

    return SharedDataResponse(masked_data=masked_data, status="success")
