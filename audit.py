import logging
from datetime import datetime
import smtplib
from email.message import EmailMessage
logging.basicConfig(filename="audit.log", level=logging.INFO)
ALERT_EMAIL = "admin@fintech.com"

def log_access(requester, user_id, fields_accessed):
    logging.info(f"[{datetime.now()}] {requester} accessed fields {fields_accessed} of {user_id}")




def send_alert_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = ALERT_EMAIL
    msg["To"] = "security@fintech.com"

    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)

def detect_anomalies(requester, requested_fields, allowed_fields):
    anomaly = any(field not in allowed_fields for field in requested_fields)
    if anomaly:
        send_alert_email("Data Access Anomaly Detected",
                         f"{requester} tried to access: {requested_fields}, allowed: {allowed_fields}")
    return anomaly
