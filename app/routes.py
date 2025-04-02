from flask import Blueprint, request, jsonify, Response, current_app
from twilio.twiml.voice_response import VoiceResponse
from app import db
from app.models import Message
from app.utils import save_message
from app.services.twilio_service import client, VOICE_MESSAGE  # Import Twilio setup

routes = Blueprint("routes", __name__)


@routes.route("/answer", methods=["GET", "POST"])
def incoming():
    """Response to incoming calls"""
    current_app.logger.info("📞 Incoming call ...")
    response = VoiceResponse()
    response.play(VOICE_MESSAGE)
    response.record(max_length=300, action="/record", method="POST")  # 5 minutes max
    return Response(str(response), mimetype="text/xml")


@routes.route("/record", methods=["POST"])
def handle_recording():
    """Handle the recording"""
    recording_url = request.values.get("RecordingUrl")
    caller = request.values.get("From")

    current_app.logger.info(f"🎙️ Recording URL: {recording_url}")
    current_app.logger.info(f"👤: {caller}")
    save_message(recording_url, caller)
    response = VoiceResponse()
    response.say("Thank you for your message. Goodbye.")
    response.hangup()
    return Response(str(response), mimetype="text/xml")


@routes.route("/messages", methods=["GET"])
def get_messages():
    """Return all messages"""
    messages = Message.query.all()
    return jsonify([messages.to_dict() for messages in messages])


@routes.route("/messages/<int:id>", methods=["DELETE"])
def delete_message(id):
    """Delete message by id"""
    message = Message.query.get(id)
    if not message:
        return jsonify({"message": "message not found"}), 404
    db.session.delete(message)
    db.session.commit()
    return jsonify({"message": "deleted message " + str(id)})
