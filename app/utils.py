from app.models import Message
from app.extensions import db
from flask import current_app as app

def save_message(recording_url, caller):
    try:
        caller = clean_caller_number(caller)
        message = Message(link=recording_url, caller=caller)
        db.session.add(message)
        db.session.commit()
        app.logger.info(f"💾 Message saved: {recording_url}")
    except Exception as e:
        app.logger.error(f"💥 Error saving message: {e}")
        db.session.rollback()

def clean_caller_number(caller):
    return caller[2:] if caller.startswith('+1') else caller

