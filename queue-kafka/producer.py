import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer
from data_gen_for_unittest.data_generator import generate_message


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    # while True:
    # Generate a message
    # dummy_message = generate_message()

    # Send it to our 'messages' topic
    # print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
    producer.send('messages', {"user_id": "mohammad"})

    # Sleep for a random number of seconds
    # time_to_sleep = random.randint(1, 11)
    # time.sleep(time_to_sleep)
