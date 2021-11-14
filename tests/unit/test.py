from datetime import datetime, timezone
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_datetime(self):
        now = datetime.now()
        past_time = datetime.strptime('Jun 1 2020  1:33PM', '%b %d %Y %I:%M%p')
        time_diff = now - past_time
        self.assertTrue(
            time_diff.days > 7
        )
