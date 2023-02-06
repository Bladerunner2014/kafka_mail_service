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
        ).poll(timeout_ms=config["TIME_OUT"])

    for message in consumer:
        msg = json.loads(message.value)
        print(msg)
        print(message)
        send_mail(msg)
        '''con_message = {"subject":"newsletter","temp_id":"one", "users_details": [["abbas1234", 
        "reza", "karim@gmial.com"], ["user_name":"abbas1234", 
        "reza", "karim@gmial.com"]]} '''
        # last item in user_details lists is email
        # temp example: 'hey my {0} name is {1} and im {2} years old'
        # html = mail.process_data(con_message)
        # mail.send_email(html, con_message)

