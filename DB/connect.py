import sqlite3
import os

db_path = os.getenv("DB_PATH", "/home/shaylevin89/mysite/DB/forecast.db")

columns = ['Longitude', 'Latitude', 'forecast_time', 'Temperature_Celsius', 'Precipitation_Rate']


def create_table(cur, conn):
    cur.execute(f'''CREATE TABLE IF NOT EXISTS forecast ( {columns[0]} real NOT NULL, {columns[1]} real NOT NULL,
        {columns[2]} TIMESTAMP NOT NULL, {columns[3]} real NOT NULL, {columns[4]} real NOT NULL );''')
    conn.commit()


def db_connect():
    conn = sqlite3.connect(db_path, check_same_thread=False)
    cur = conn.cursor()
    create_table(cur, conn)
    return cur, conn
