from extract_data import fetch_stock_data, stock_symbols
from kafka import KafkaProducer
import time
import json


KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'stock-data'

producer = KafkaProducer(
    bootstrap_servers = KAFKA_BROKER,
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

def send_stock_data():
    stock_data_list = fetch_stock_data(stock_symbols)
    if stock_data_list:
        for stock_data in stock_data_list:
            producer.send(KAFKA_TOPIC, stock_data)
            print(f"Sent: {stock_data}")


if __name__ == "__main__":
    try:
        while True:
            send_stock_data()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        producer.close() 