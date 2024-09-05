"""
SCRIPT: streaming_data_reader.py
DESCRIPTION: Streaming data consumer
"""
import os
from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

TOPIC = 'toll'
DATABASE = 'tolldata'
USERNAME = 'root'
PASSWORD = '< MYSQL_PASSWORD >'

print("Connecting to the database")
connection = None
try:
    connection = mysql.connector.connect(host='mysql', database=DATABASE, user=USERNAME, password=PASSWORD)
except Exception as e:
    print(f"Could not connect to database. Please check credentials. Error: {str(e)}")
else:
    print("Connected to database")

if connection:
    cursor = connection.cursor()

    print("Connecting to Kafka")
    consumer = KafkaConsumer(TOPIC)
    print("Connected to Kafka")

    print(f"Reading messages from the topic {TOPIC}")
    for msg in consumer:

        # Extract information from kafka
        message = msg.value.decode("utf-8")

        # Transform the date format to suit the database schema
        (timestamp, vehcile_id, vehicle_type, plaza_id) = message.split(",")

        dateobj = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
        timestamp = dateobj.strftime("%Y-%m-%d %H:%M:%S")

        # Loading data into the database table
        sql = "insert into livetolldata values(%s,%s,%s,%s)"
        cursor.execute(sql, (timestamp, vehcile_id, vehicle_type, plaza_id))
        print(f"A {vehicle_type} was inserted into the database")
        connection.commit()

    connection.close()
