# after-the-i-dos

My best friend wanted an audio guest book, but didn't want to pay the high price.

I told her I could set one up for free and here we are! 🎉

This is an API that allows guests to call and leave voicemails.


# 🚀 Features
- Accepts incoming calls via Twilio
- Plays a pre-recorded message before allowing guests to leave a voicemail
- Saves voicemail recordings to a database
- Provides an API to manage & retrieve recorded messages

# Stack 
- Python 3.8+
- Flask (API framework)
- Twilio (for handling phone calls)
- SQLite / SQLAlchemy (for storing messages)
- Flask-Migrate (database migrations)
- Gunicorn (for production deployment)


# Setup Instructions

## Set Up a Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate 
```

## Install Dependencies
```
pip install poetry
poetry install
```

## Set Up Environment Variables

Create a .env file in the root directory and add:

```
APP_SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
VOICE_MESSAGE_LINK=https://your-message-file.mp3
```
Replace values with your actual Twilio credentials.

## Set Up the Database

```
flask db upgrade  # Apply migrations
```
## Run the App

``` 
python3 app.py
```
OR with Gunicorn (for production):
```
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

# API Endpoints

| Method | Endpoint          | Description                               |
|--------|-------------------|-------------------------------------------|
| POST   | `/answer`         | Handles incoming calls and starts recording |
| POST   | `/record`         | Stores recorded voicemails                 |
| GET    | `/messages`       | Returns all stored messages               |
| DELETE | `/messages/<id>`  | Deletes a specific message                |

# 📌 To-do
- [x] Store recordings in cloud storage (e.g., AWS S3)
- [ ] Add authentication for message retrieval
- [ ] Build a frontend UI for easier playback