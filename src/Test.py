import unittest   # The test framework
import stradview_utils

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    def test_decrement(self):
        self.assertEqual(3, 4)

if __name__ == '__main__':
    unittest.main()
    
    test_file = 'case3.sw'
    test_file_name = r'File-conversion github\test_data\case3.sw'
    #os.path.join(os.getcwd(), 'test_data', test_file)
    data = parse_stradview_file(test_file_name)
    print(data)