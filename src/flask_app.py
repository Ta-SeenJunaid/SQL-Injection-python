from flask import Flask, request, render_template

from db import get_user_data

app = Flask(__name__)


@app.route("/")
def user_form():
    return render_template('from_ex.html')


@app.route("/", methods=['POST'])
def my_form_post():
    data = request.form['u']
    messages = get_user_data(data)
    output = [f"<li>Message ID: {msg_id}, User ID: {user_id} , Message: {msg}</li>"
              for msg_id, user_id, msg in messages]
    return f"<br/><ol>{''.join(output)}</ol>"


@app.route("/user-messages/<user_id>")
def get_user_messages(user_id: int):
    messages = get_user_data(user_id)
    output = [f"<li>Message ID: {msg_id}, User ID: {user_id} , Message: {msg}</li>"
              for msg_id, user_id, msg in messages]

    return f"<br/><ol>{''.join(output)}</ol>"

