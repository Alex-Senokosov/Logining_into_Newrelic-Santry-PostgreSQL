import psycopg2
import datetime
DBNAME = 'Your_DBNAME'
USER = 'postgres'
PASSWORD = 'Your_PASSWORD'
HOST = '127.0.0.1'
ERROR = 'ERROR'
WARNING = 'WARNING'
INFO = 'INFO'
def create_flats_table():
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as cur:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS logs(
                id serial PRIMARY KEY,
                log_date TIMESTAMP,
                log_level CHARACTER VARYING(20) NOT NULL,
                log_info TEXT
                )''')
def insert_flat(log_level, log_info):
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO logs (log_date, log_level, log_info) VALUES (%s, %s, %s)
                 ''',
                        (datetime.datetime.now(), log_level, log_info)
                        )

def get_last_error(limit = 10):
    create_flats_table()
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT log_date, log_info FROM logs WHERE (log_level = 'ERROR') LIMIT %s
                 ''',
                        (limit, )
                        )
            return cur.fetchall()


error_logs = get_last_error()


def error(log_info):
     insert_flat(log_level=ERROR, log_info=log_info)
def warning(log_info):
    insert_flat(log_level=WARNING, log_info=log_info)
def info(log_info):
    insert_flat(log_level=INFO, log_info=log_info)
