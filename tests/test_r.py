
import unittest
from queue_handler.queue_handler import Broker
from dotenv import dotenv_values


class Emailservice(unittest.TestCase):

    def test_1(self):
        config = dotenv_values(".env")

        broker = Broker(config["TOPIC"])
        broker.produce_msg({"subject": "newsletter", "temp_id": "one",
                            "users_details": [{'name': 'abbas', 'email': 'mhh400000@gmail.com'},
                                              {'name': 'reza', 'email': 'mhh4000000@gmail.com'}]})
        broker.consume_msg()
        self.assertEqual(broker.confirmed, True)
        print('test 1 completed')


if __name__ == "__main__":
    tester = Emailservice()
    tester.test_1()
