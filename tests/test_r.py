import runpy
import json
from kafka import KafkaConsumer
from manager.email import MailService
import unittest
from manager.mail_app import send_mail


class Emailservice(unittest.TestCase):

    def test_1(self):
        consumer = KafkaConsumer(
            'messages',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest'
        )
        for message in consumer:
            answer = json.loads(message.value)
        self.assertEqual(answer, 'mohammad')
        print('test 1 completed')

    def test_2(self):
        body_and_receiver = {"subject": "newsletter", "temp_id": "one", "content": "salam",
                             "users_details": [{'name': 'abbas', 'email': 'mhh400000@gmail.com'},
                                               {'name': 'reza', 'email': 'mhh4000000@gmail.com'}]}

        self.assertEqual(send_mail(body_and_receiver["users_details"]).status_code, 200)

        print('test 2 completed')


if __name__ == "__main__":
    tester = Emailservice()
    runpy.run_path(path_name='queue-kafka/producer.py')
    tester.test_1()
    tester.test_2()
