import os
from typing import Dict, List, Callable
from stradview_types import StradViewData, StradViewImage


# def make_my_value(x: int, y: float) -> str:
    # return ''

# Callable[[int, float], str]

# original_list = [1, 2, 4]
# def func(value): 
    # return value * 2

# result = {
    # x: func(x) for x in original_list
# }

# result = []
# for x in original_list:
    # result.append(func(x))

INT_PARAMETERS = [
    'RES_BUF_FRAMES',
    'RES_BUF_HEIGHT',
    'RES_BUF_WIDTH'
]

BOOLEAN_PARAMETERS = [
    'RES_BUF_RF'
]


def parse_stradview_file(path: str) -> StradViewData:
    result = StradViewData()

    def make_int_parser(name: str) -> Callable[[List[str]], None]:
        attr_name = name.lower()
        def parse(tokens: List[str]):
            value = int(token_line[1])
            setattr(result, attr_name, value)
        return parse

    def make_bool_parser(name: str) -> Callable[[List[str]], None]:
        attr_name = name.lower()
        def parse(tokens: List[str]):
            # TODO: get boolean value from tokens
            value = True
            setattr(result, attr_name, value)
        return parse

    def parse_image(tokens: List[str]):
        result.images.append(StradViewImage(

        ))

    param_parsers: Dict[str, Callable[[List[str], None]]] = { 
        name: make_int_parser(name) for name in INT_PARAMETERS
    } | {
        name: make_bool_parser(name) for name in BOOLEAN_PARAMETERS
    } | {
        'IM': parse_image
    }
    
    file = open(path)
    token_lines = [line.split(' ') for line in file.readlines()]
    skipped_tokens = set()

    for token_line in token_lines:
        start_token = token_line[0]

        if start_token in param_parsers:
            param_parsers[start_token](token_line)

        elif start_token == 'RES_BUF_RF':
            if token_line[1]=='true\n':
                result.res_buf_rf = True
            elif token_line[1]== 'false\n':
                result.res_buf_rf = False
        elif start_token == 'RES_BUF_DICOM':
            if token_line[1]=='true\n':
                result.res_buf_dicom = True
            elif token_line[1]== 'false\n':
                result.res_buf_dicom = False
        elif start_token == 'RES_DICOM_FRAME_LIST':
            result.res_dicom_frame_list = token_line[1:]
        elif start_token == 'RES_POS_REC':
            if token_line[1]=='true\n':
                result.res_pos_rec = True
            elif token_line[1]== 'false\n':
                result.res_pos_rec = False

        elif start_token == 'RES_BIN_IM_FILENAME':
            result.res_bin_im_filename = token_line[1]
        
        elif start_token == 'RES_VERSION':
            result.res_version = float(token_line[1])
        elif start_token == 'RES_CORRECTED_PRESSURE':
            if token_line[1]=='true\n':
                result.res_corrected_pressure = True
            elif token_line[1] == 'false\n':
                result.res_corrected_pressure = False
        elif start_token == 'RES_CORRECTED_POS':
            if token_line[1]=='true\n':
                result.res_corrected_pos = True
            elif token_line[1]== 'false\n':
                result.res_corrected_pos = False
        elif start_token == 'RES_MASKED_DATA':
            result.res_masked_data = int(token_line[1])
        elif start_token == 'RES_INVERT_BSCAN':
            if token_line[1]=='true\n':
                result.res_invert_bscan = True
            elif token_line[1]== 'false\n':
                result.res_invert_bscan = False
        elif start_token == 'RES_BUF_DOPPLER':
            if token_line[1]=='true\n':
                result.res_buf_doppler = True
            elif token_line[1]== 'false\n':
                result.res_buf_doppler = False
        elif start_token == 'RES_XTRANS':
            result.res_xtrans = float(token_line[1])
        elif start_token == 'RES_YTRANS':
            result.res_ytrans = float(token_line[1])
        elif start_token == 'RES_ZTRANS':
            result.res_ztrans = float(token_line[1])
        elif start_token == 'RES_AZIMUTH':
            result.res_azimuth = float(token_line[1])
        elif start_token == 'RES_ELEVATION':
            result.res_elevation = float(token_line[1])
        elif start_token == 'RES_ROLL':
            result.res_roll = float(token_line[1])
        elif start_token == 'RES_XSCALE':
            result.res_xscale = float(token_line[1])
        elif start_token == 'RES_YSCALE':
            result.res_yscale = float(token_line[1])
        elif start_token == 'RES_POS_MANUAL':
            if token_line[1]=='true\n':
                result.res_pos_manual = True
            elif token_line[1]== 'false\n':
                result.res_pos_manual = False
        elif start_token == 'RES_POS_MANUAL_TRAN':
            result.res_pos_manual_tran = int(token_line[1])
        elif start_token == 'RES_POS_MANUAL_SPAN':
            result.res_pos_manual_span = float(token_line[1])
        elif start_token == 'RES_POS_MANUAL_ROT':
            result.res_pos_manual_rot = int(token_line[1])
        elif start_token == 'RES_POS_MANUAL_ANGLE':
            result.res_pos_manual_angle = int(token_line[1])
        elif start_token == 'RES_POS_MANUAL_RADIUS':
            result.res_pos_manual_radius= int(token_line[1])
        elif start_token == 'RES_DICOM_HUM':
            result.res_dicom_hum = float(token_line[1])
        elif start_token == 'RES_DICOM_HUB':
            result.res_dicom_hub = float(token_line[1])
        elif start_token == 'RES_DICOM_WIN_WIDTH':
            result.res_dicom_win_width = float(token_line[1])
        elif start_token == 'RES_DICOM_WIN_WIDTH':
            result.res_dicom_win_width = float(token_line[1])
        elif start_token == 'RES_DICOM_WIN_CENTRE':
            result.res_dicom_win_centre = float(token_line[1])
        elif start_token == 'RES_DICOM_FILTER':
            result.res_dicom_filter = int(token_line[1])
        elif start_token == 'RES_DICOM_BMD_PHANTOM':
            result.res_dicom_bmd_phantom =token_line[1]
        elif start_token == 'RES_DICOM_BMD_SCALE':
            result.res_dicom_bmd_scale = float(token_line[1])
        elif start_token == 'RES_DICOM_BMD_OFFSET':
            result.res_dicom_bmd_offset = float(token_line[1])
        elif start_token == 'RES_THICKNESS_SCALE_MM':
            result.res_thickness_scale_mm = int(token_line[1])
        elif start_token == 'RES_THICKNESS_SCALE_HU':
            result.res_thickness_scale_hu = int(token_line[1])
        elif start_token == 'RES_THICKNESS_ZERO_HU':
            result.res_thickness_zero_hu = int(token_line[1])
        elif start_token == 'RES_THICKNESS_SCALE_HUMM':
            result.res_thickness_scale_humm = int(token_line[1])
        elif start_token == 'RES_THICKNESS_TYPE':
            result.res_thickness_type= int(token_line[1])
        elif start_token == 'RES_THICKNESS_LINE':
            result.res_thickness_line= float(token_line[1])
        elif start_token == 'RES_THICKNESS_GAUSS':
            result.res_thickness_gauss= float(token_line[1])
        elif start_token == 'RES_THICKNESS_RECT':
            result.res_thickness_rect= float(token_line[1])
        elif start_token == 'RES_THICKNESS_A':
            result.res_thickness_a= float(token_line[1])
        elif start_token == 'RES_THICKNESS_B':
            result.res_thickness_b= float(token_line[1])
        elif start_token == 'RES_THICKNESS_C':
            result.res_thickness_c= float(token_line[1])
        elif start_token == 'RES_THICKNESS_A_AVERAGE':
            result.res_thickness_a_average= float(token_line[1])
        elif start_token == 'RES_THICKNESS_C_AVERAGE':
            result.res_thickness_c_average= float(token_line[1])
        elif start_token == 'RES_THICKNESS_CREATE_INNER':
            if token_line[1]=='true\n':
                result.res_thickness_create_inner = True
            elif token_line[1]== 'false\n':
                result.res_thickness_create_inner = False
        elif start_token == 'RES_THICKNESS_CREATE_OUTER':
            if token_line[1]=='true\n':
                result.res_thickness_create_outer = True
            elif token_line[1]== 'false\n':
                result.res_thickness_create_outer = False
        elif start_token == 'RES_THICKNESS_CREATE_CAPS':
            if token_line[1]=='true\n':
                result.res_thickness_create_caps = True
            elif token_line[1]== 'false\n':
                result.res_thickness_create_caps = False
        elif start_token == 'RES_THICKNESS_OUTLIER_REJECT':
            result.res_thickness_outlier_reject = int(token_line[1])
        elif start_token == 'RES_THICKNESS_DISTANCE_REJECT':
            result.res_thickness_distance_reject = int(token_line[1])
        elif start_token == 'RES_THICKNESS_MAP_DIRECTION':
            result.res_thickness_map_direction = int(token_line[1])
        elif start_token == 'RES_BACKGROUND':
            result.res_background =(token_line[1])
        elif start_token == 'RES_SHADER':
            result.res_shader = int(token_line[1])
        elif start_token == 'RES_LIGHTING_AMBIENT':
            result.res_lighting_ambient= float(token_line[1])
        elif start_token == 'RES_LIGHTING_FRONT_SIDE':
            result.res_lighting_front_side= float(token_line[1])
        elif start_token == 'RES_OCCLUSION_RANGE':
            result.res_occlusion_range= int(token_line[1])
        elif start_token == 'RES_RADIANT_SHADOWS':
            if token_line[1]=='true\n':
                result.res_radiant_shadows = True
            elif token_line[1]== 'false\n':
                result.res_radiant_shadows = False
        else:
            skipped_tokens.add(start_token)

    print(f"Ignored tokens: {', '.join(skipped_tokens)}")
    return result

if __name__ == '__main__':
    test_file = 'case3.sw'
    test_file_name = os.path.join(os.getcwd(), 'test_data', test_file)
    data = parse_stradview_file(test_file_name)
    print(data)
