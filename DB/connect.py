# import sqlite3
from flask_sqlalchemy import SQLAlchemy
from app import app
import os
from datetime import datetime

db_path = os.getenv("DB_PATH", "/home/shaylevin89/mysite/DB/forecast.db")

SQLALCHEMY_DATABASE_URI = f"sqlite://{db_path}"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Forecast(db.Model):
    __tablename__ = "forecast"
    Longitude = db.Column(db.Float)
    Latitude = db.Column(db.Float)
    forecast_time = db.Column(db.DateTime, default=datetime.now)
    Temperature_Celsius = db.Column(db.Float)
    Precipitation_Rate = db.Column(db.Float)


print(Forecast.query())


columns = ['Longitude', 'Latitude', 'forecast_time', 'Temperature_Celsius', 'Precipitation_Rate']


def create_table(cur, conn):
    cur.execute(f'''CREATE TABLE IF NOT EXISTS forecast ( {columns[0]} real NOT NULL, {columns[1]} real NOT NULL,
        {columns[2]} TIMESTAMP NOT NULL, {columns[3]} real NOT NULL, {columns[4]} real NOT NULL );''')
    conn.commit()


def db_connect():
    conn = sqlite3.connect(config.db_path, check_same_thread=False)
    cur = conn.cursor()
    create_table(cur, conn)
    return cur, conn
