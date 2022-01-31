import os
import unittest   # The test framework
from stradview_utils import parse_stradview_file, _make_int_parser


class TestStradviewUtils(unittest.TestCase):
    def test_parse_stradview_file(self):
        test_file = 'case3.sw'
        test_file_name = os.path.join(os.getcwd(), 'test_data', test_file)
        data = parse_stradview_file(test_file_name)
        self.assertEqual(data.res_buf_frames, 83)
        self.assertEqual(len(data.images), 83)


if __name__ == '__main__':
    unittest.main()
