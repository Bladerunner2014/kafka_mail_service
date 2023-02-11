import logging

from queue_handler import queue_handler
from dotenv import dotenv_values

config = dotenv_values(".env")

logger = logging.getLogger(__name__)
if __name__ == '__main__':

    broker = queue_handler.Broker(config["TOPIC"])

    broker.consume_msg()



