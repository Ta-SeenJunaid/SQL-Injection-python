from db import connection_context
from models import Message

CREATE_TABLE_MESSAGE = """
CREATE TABLE IF NOT EXISTS messages (
    msg_id integer PRIMARY KEY,
    user_id integer,
    msg varchar(100)
);
"""

MESSAGE_DATA = [
    Message(msg_id=1, user_id=1, msg="msg 1 user 1"),
    Message(msg_id=2, user_id=2, msg="msg 2 user 2"),
    Message(msg_id=3, user_id=3,msg="msg 3 user 3"),
    Message(msg_id=4, user_id=1, msg="msg 4 user 1"),
    Message(msg_id=5, user_id=2, msg="msg 5 user 2"),
    Message(msg_id=6,user_id=3, msg="msg 6 user 3")
]


def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_MESSAGE)

        for message in MESSAGE_DATA:
            insert_cmd = f"""
                INSERT INTO messages (msg_id, user_id, msg)
                VALUES (
                    {message.msg_id},
                    {message.user_id},
                    '{message.msg}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)