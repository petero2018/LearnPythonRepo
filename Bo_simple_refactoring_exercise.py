import unittest
from log_parser import return_method


class TestLogParser(unittest.TestCase):

    def test_parse(self):
        values = return_method('10.0.0.208 - - [17/Jul/2018:15:40:16] /v1/escalation/predict 200 Pingdom.com_bot_version_1.4', 'log')
        self.assertEqual(values[0:5], ['10.0.0.208', '17/Jul/2018:15:40:16', '/v1/escalation/predict', '200', 'Pingdom.com_bot_version_1.4'])

    def test_csv(self):
        values = return_method('10.0.0.208 - - [17/Jul/2018:15:40:16] /v1/escalation/predict 200 Pingdom.com_bot_version_1.4', 'csv')
        self.assertEqual(values, '10.0.0.208,17/Jul/2018:15:40:16,/v1/escalation/predict,200,Pingdom.com_bot_version_1.4')


if __name__ == '__main__':
    unittest.main()