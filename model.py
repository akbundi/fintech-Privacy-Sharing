from pydantic import BaseModel
from typing import List, Optional

class UserData(BaseModel):
    user_id: str
    name: str
    bank_account: str
    income: float
    transaction_history: List[str]
    pii: dict
    device_data: dict

class Consent(BaseModel):
    user_id: str
    allowed_fields: List[str]
    expiration: Optional[str]  # ISO format

class DataAccessRequest(BaseModel):
    requester: str
    user_id: str
    purpose: str

class SharedDataResponse(BaseModel):
    masked_data: dict
    status: str
