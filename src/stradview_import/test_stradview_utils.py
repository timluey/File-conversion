import os
import unittest
from stradview_import.stradview_utils import parse_stradview_file


class TestStradviewUtils(unittest.TestCase):
    def test_raises_error_if_file_doesnt_exist(self):
        pass

    def test_parse_stradview_file(self):
        test_file = 'case3.sw'
        test_file_name = os.path.join(os.getcwd(), 'test_data', test_file)
        data = parse_stradview_file(test_file_name)
        
        file=open(test_file_name)
        token_lines = [line.split(' ') for line in file.readlines()]
        
        #Testing parameters
        self.assertEqual(data.res_buf_frames, 83)
        self.assertEqual(data.res_corrected_pos, False)
        self.assertEqual(data.res_yscale, 0.082617)
        self.assertEqual(data.res_thickness_scale_hu, 20)
        self.assertEqual(data.res_pos_manual_angle, 0)
        self.assertEqual(len(data.res_dicom_frame_list), 83)
        

        #Testing image parameters
        self.assertEqual(len(data.images), 83)
        self.assertEqual(data.images[5].elevation, 0 )
        self.assertEqual(data.images[10].location,(-21.908691, -41.058689, 38.09)) 
        self.assertEqual(data.images[59].time, 59)
        self.assertEqual(data.images[80].roll, 0)


        #Testing Object parameters
        self.assertEqual(len(data.objects), 18)
        self.assertEqual(data.objects[1].solid, 1)
        self.assertEqual(data.objects[3].alpha, 1)
        self.assertEqual(data.objects[6].metal, 0)
        self.assertEqual(data.objects[10].rough, 0.3)
        self.assertEqual(data.objects[17].rgb, (178, 89, 0))

        #Testing Contour parameters
        self.assertEqual(data.contours[1].closed, 1)
        self.assertEqual(data.contours[20].frame, 24)
        self.assertEqual(data.contours[80].obj, 1)
        self.assertEqual(data.contours[0].xy[0], (177.99, 335.29))
        self.assertEqual(len(data.contours[31].xy), 5)
        xy_values = [(float(x), float(y)) for x, y in zip(token_lines[157][4::2], token_lines[157][5::2])]
        self.assertEqual(data.contours[0].xy, xy_values)
        
        
        

        file.close()

if __name__ == '__main__':
    unittest.main()
