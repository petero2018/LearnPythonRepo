import unittest
from log_parser import return_method


class TestLogParser(unittest.TestCase):

    def setUp(self):
        print('setUp log line')
        self.log_line = '10.0.0.208 - - [17/Jul/2018:15:40:16] /v1/escalation/predict 200 Pingdom.com_bot_version_1.4'

    def tearDown(self):
        print('tearDown \n')

    def test_parse(self):
        print('Log test')
        values = return_method(self.log_line, 'log')
        self.assertEqual(values[0:5], ['10.0.0.208', '17/Jul/2018:15:40:16', '/v1/escalation/predict', '200', 'Pingdom.com_bot_version_1.4'])

    def test_csv(self):
        print('Csv test')
        values = return_method(self.log_line, 'csv')
        self.assertEqual(values, '10.0.0.208,17/Jul/2018:15:40:16,/v1/escalation/predict,200,Pingdom.com_bot_version_1.4')


if __name__ == '__main__':
    unittest.main()