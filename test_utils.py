import unittest
from unittest.mock import Mock
from datetime import datetime
from utils import get_day, get_date 

class TestUtils(unittest.TestCase):
    def test_set_days_in_numbers_format(self):
        mock = Mock(return_value=datetime(2024,1,2))
        get_date = mock
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(type(get_date()))
        print(type(datetime.now()))
        sut = get_day

        day = sut(get_date())
        print(sut(get_date()))

        assert day == 32

if __name__ == '__main__':
    unittest.main()
