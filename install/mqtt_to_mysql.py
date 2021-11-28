import paho.mqtt.client as mqtt
import mysql.connector
from time import time
 
MQTT_HOST = 'localhost'
MQTT_PORT = 1883
MQTT_CLIENT_ID = '08:00:27:65:01:9b'
MQTT_USER = None
MQTT_PASSWORD = None
TOPIC = 'sansiv/#'
 
#DATABASE_FILE = 'mqtt.db'
config = {
  'user': 'sql11454680',
  'password': 'EYTRb6D9mR',
  'host': 'sql11.freesqldatabase.com',
  'database': 'sql11454680',
  'auth_plugin':'mysql_native_password'
}
 
def on_connect(mqtt_client, user_data, flags, conn_result):
    mqtt_client.subscribe(TOPIC)
 
 
def on_message(mqtt_client, user_data, message):
    payload = message.payload.decode('utf-8')
 
    db_conn = mysql.connector.connect(**config)
    sql = 'INSERT INTO sensors_data (topic, payload) VALUES (%s, %s)'
    cursor = db_conn.cursor()
    cursor.execute(sql, (message.topic, payload))
    db_conn.commit()
    cursor.close()
 
 
def main():
    db_conn = mysql.connector.connect(**config)
    sql = """
    CREATE TABLE IF NOT EXISTS sensors_data (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        topic TEXT NOT NULL,
        payload TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor = db_conn.cursor()
    cursor.execute(sql)
    cursor.close()
 
    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.user_data_set({'db_conn': db_conn})
 
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
 
    mqtt_client.connect(MQTT_HOST, MQTT_PORT)
    mqtt_client.loop_forever()
 
 
main()