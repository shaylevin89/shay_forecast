import os
import logging
import csv
import connect

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

path = os.getcwd()

cur, conn = connect.db_connect()


def insert_csv_to_db(file_name):
    try:
        file = open(f'{path}/csv_files/{file_name}', 'r')
        reader = csv.reader(file)
        next(reader)
        cur.executemany("INSERT INTO forecast VALUES (?, ?, ?, ?, ?)", reader)
        conn.commit()
        file.close()
        logging.info(f'file {file_name} uploaded successfully to database')
    except Exception as e:
        logging.error(f'{e}')


def file_uploader():
    # csv_files dir should contain the csv files for upload
    files = os.listdir(f'{path}/csv_files/')
    for file in files:
        insert_csv_to_db(file)


if __name__ == '__main__':
    file_uploader()

