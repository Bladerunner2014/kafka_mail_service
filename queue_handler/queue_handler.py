import json
from confluent_kafka import Producer, Consumer, KafkaError
from dotenv import dotenv_values
import logging
from constants.error_message import ErrorMessage
from constants.info_message import InfoMessage
from manager.mail_app import send_mail


class Broker:
    def __init__(self, topic):
        self.confirmed = None
        self.config = dotenv_values(".env")
        self.logger = logging.getLogger(__name__)
        self._config_kafka = {'bootstrap.servers': self.config["KAFKA_BOOTSTRAP_SERVERS"], 'group.id': self.config["GROUP_ID"],
                              "auto.offset.reset": self.config["AUTO_OFFSET_RESET"]}
        self.producer = Producer(self._config_kafka)
        self.consumer = Consumer(self._config_kafka, )
        self.topic = topic

    def delivery_report(self, err, msg):
        if err is not None:
            self.logger.error(ErrorMessage.KAFKA_PRODUCE)
            self.logger.error(err)
        else:
            self.logger.error(InfoMessage.KAFKA_PRODUCE)
            self.logger.error(msg.topic() + " " + msg.partition())

    def produce_msg(self, data):
        self.producer.poll(self.config["PRODUCER_TIME_OUT"])
        self.producer.produce(self.topic, json.dumps(data), callback=self.delivery_report)
        self.producer.flush()

    def consume_msg(self):
        self.consumer.subscribe([self.topic])
        print(self.consumer.assignment())
        while True:
            msg = self.consumer.poll(self.config["CONSUMER_TIME_OUT"])
            print(msg)
            if msg is None:
                continue
            if msg.error():
                print(msg.error().code())
            else:
                print("msg1")
                print(msg.value())
                msg = json.loads(msg.value())
                print(msg)
                try:
                    send_mail(msg)
                    self.confirmed = True
                except:
                    continue


