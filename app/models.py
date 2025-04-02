"""Models for the application."""

from datetime import datetime
from app.extensions import db


class Message(db.Model):
    """Model for storing messages."""

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    link = db.Column(db.String(255), nullable=False)
    caller = db.Column(db.String(20), nullable=False)
    uploaded = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the Message object to a dictionary."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "link": self.link,
            "caller": self.caller,
            "uploaded": self.uploaded,
        }

    def __repr__(self):
        """String representation of the Message object."""
        return f"<Message {self.id} - {self.caller} - {self.link}>"
