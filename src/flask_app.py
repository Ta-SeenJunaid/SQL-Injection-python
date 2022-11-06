from flask import Flask

from db import get_user_data

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi good to see you"
    )


@app.route("/user-messages/<user_id>")
def get_user_messages(user_id: int):
    messages = get_user_data(user_id)
    output = [f"<li>Message ID: {msg_id}, User ID: {user_id} , Mesage: {msg}</li>"
              for msg_id, user_id, msg in messages]

    return f"<br/><ol>{''.join(output)}</ol>"



