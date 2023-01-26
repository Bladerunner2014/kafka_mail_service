import json
from kafka import KafkaConsumer
import logging
from constants.error_message import ErrorMessage
from manager.mail_app import send_mail

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    # Kafka Consumer 
    try:
        consumer = KafkaConsumer(
            topic='messages',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='latest'
        ).poll(timeout_ms=1.0)
    except Exception as error:
        logger.error(ErrorMessage.LISTENING_FAIL)
        logger.error(error)
        raise Exception
    for message in consumer:
        con_message = json.loads(message.value)
        '''body_and_receiver = {"subject": "newsletter", "temp_id": "one", "content": "salam",
                             "users_details": [{'name': 'abbas', 'email': 'mhh400000@gmail.com'},
                                               {'name': 'reza', 'email': 'mhh4000000@gmail.com'}]}

        send_mail(body_and_receiver["users_details"])'''
        send_mail(con_message)
