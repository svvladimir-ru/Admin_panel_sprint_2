import sqlite3

import psycopg2
import time
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from sqlite_loader import SQLiteLoader
from postgres_saver import PostgresSaver
from config import dsl


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)

    data = sqlite_loader.load_movies()
    postgres_saver.save_all_data(data)


if __name__ == '__main__':
    counter = 10
    # while counter:
        # try:
    with sqlite3.connect('sqlite_to_postgres/db.sqlite') as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
    sqlite_conn.close()
    pg_conn.close()
        #     break
        # except:
        #     time.sleep(2)
        #     counter -= 1
        #     continue

