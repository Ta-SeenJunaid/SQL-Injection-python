import contextlib
import logging
import os
import sqlite3
from typing import List, Any

logger = logging.getLogger(__name__)

DB_FILENAME = os.path.realpath("data/test.db")


def _get_connection() -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(DB_FILENAME)
    except sqlite3.Error:
        logger.exception("Unable to get database")
        raise
    else:
        return conn


@contextlib.contextmanager
def connection_context():
    conn = _get_connection()
    cur = conn.cursor()

    yield cur

    conn.commit()
    cur.close()
    conn.close()


def get_user_data(user_id: int) -> List[Any]:
    query = f"""
        SELECT msg_id, user_id, msg FROM messages
        WHERE user_id='{user_id}';
    """
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()

        return results
