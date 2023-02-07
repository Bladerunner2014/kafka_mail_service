import json
from kafka import KafkaConsumer
# from manager.send_mail import MailService
import logging
# from constants.error_message import ErrorMessage
from manager.mail_app import send_mail
from dotenv import dotenv_values

config = dotenv_values(".env")

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    # Kafka Consumer 
    # mail = MailService()

    consumer = KafkaConsumer(
            config["TOPIC"],
            bootstrap_servers=config["BOOTSTARP_SERVERS"],
            auto_offset_reset=config["AUTO_OFFSET_RESET"]
        )

    for message in consumer:
        msg = json.loads(message.value)
        print(msg)
        print(message)
        send_mail(msg)



