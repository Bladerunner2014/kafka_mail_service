import json
#from kafka import KafkaConsumer
import logging

from queue_handler import queue_handler
#from manager.mail_app import send_mail
from dotenv import dotenv_values

config = dotenv_values(".env")

logger = logging.getLogger(__name__)
if __name__ == '__main__':

    # consumer = KafkaConsumer(
    #         config["TOPIC"],
    #         bootstrap_servers=config["BOOTSTARP_SERVERS"],
    #         auto_offset_reset=config["AUTO_OFFSET_RESET"]
    #     )
    #
    # for message in consumer:
    #     msg = json.loads(message.value)
    #     print(msg)
    #     print(message)
    #     send_mail(msg)

    broker = queue_handler.Broker(config["TOPIC"])

    broker.consume_msg()



