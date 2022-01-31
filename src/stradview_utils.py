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
    'RES_BUF_WIDTH',
    'RES_MASKED_DATA',
    'RES_POS_MANUAL_TRAN',
    'RES_POS_MANUAL_ROT',
    'RES_POS_MANUAL_ANGLE',
    'RES_POS_MANUAL_RADIUS',
    'RES_DICOM_FILTER',
    'RES_THICKNESS_SCALE_MM',
    'RES_THICKNESS_SCALE_HU',
    'RES_THICKNESS_ZERO_HU',
    'RES_THICKNESS_SCALE_HUMM',
    'RES_THICKNESS_OUTLIER_REJECT',
    'RES_THICKNESS_DISTANCE_REJECT',
    'RES_THICKNESS_MAP_DIRECTION',
    'RES_SHADER',
    'RES_OCCULSION_RANGE'
]

BOOLEAN_PARAMETERS = [
    'RES_BUF_RF',
    'RES_BUF_DICOM',
    'RES_POS_REC',
    'RES_CORRECTED_PRESSURE',
    'RES_CORRECTED_POS',
    'RES_INVERT_BSCAN',
    'RES_BUF_DOPPLER',
    'RES_POS_MANUAL',
    'RES_THICKNESS_CREATE_INNER',
    'RES_THICKNESS_CREATE_OUTER',
    'RES_THICKNESS_CREATE_CAPS',
    'RES_RADIANT_SHADOWS'
]

FLOAT_PARAMETERS = [
    'RES_XTRANS',
    'RES_YTRANS',
    'RES_ZTRANS',
    'RES_AZIMUTH',
    'RES_ELEVATION',
    'RES_ROLL',
    'RES_XSCALE',
    'RES_YSCALE',
    'RES_POS_MANUAL_SPAN',
    'RES_DICOM_HUM',
    'RES_DICOM_HUB',
    'RES_DICOM_WIN_WIDTH',
    'RES_DICOM_WIN_CENTRE',
    'RES_DICOM_BMD_SCALE',
    'RES_DICOM_BMD_OFFSET',
    'RES_THICKNESS_TYPE',
    'RES_THICKNESS_LINE',
    'RES_THICKNESS_GAUSS',
    'RES_THICKNESS_RECT',
    'RES_THICKNESS_A',
    'RES_THICKNESS_B',
    'RES_THICKNESS_C',
    'RES_THICKNESS_A_AVERAGE',
    'RES_THICKNESS_C_AVERAGE',
    'RES_LIGHTING_AMBIENT',
    'RES_LIGHTING_FRONT_SIDE'
]

STRING_PARAMETERS = [
    'RES_BIN_IM_FILENAME',
    'RES_VERSION',
    'RES_DICOM_BMD_PHANTOM',
    'RES_BACKGROUND'
]

LIST_PARAMETERS = [
    'RES_DICOM_FRAME_LIST'
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
            if token_line[1]=='true\n':
                value = True
            elif token_line[1]== 'false\n':
                value = False
            setattr(result, attr_name, value)
        return parse
    
    def make_float_parser(name: str) -> Callable[[List[str]], None]:
        attr_name = name.lower()
        def parse(tokens: List[str]):
            value = float(token_line[1])
            setattr(result, attr_name, value)
        return parse

    def make_string_parser(name: str) -> Callable[[List[str]], None]:
        attr_name = name.lower()
        def parse(tokens: List[str]):
            value = token_line[1]
            setattr(result, attr_name, value)

        return parse

    def make_list_parser(name: str) -> Callable[[List[str]], None]:
        pass
        attr_name = name.lower()
        def parse(tokens: List[str]):
            list = List[int]
            for i,line in enumerate (token_line):
                if i<1: continue
                value=int(token_line[i])
                List.append(value)
            setattr(result, attr_name, List)
                

        return parse

    def parse_image(tokens: List[str]):
        result.images.append(StradViewImage)

    param_parsers: Dict[str, Callable[[List[str], None]]] = { 
        name: make_int_parser(name) for name in INT_PARAMETERS
    } | {
        name: make_bool_parser(name) for name in BOOLEAN_PARAMETERS
    } | {
        name: make_float_parser(name) for name in FLOAT_PARAMETERS
    } | {
        name: make_string_parser(name) for name in STRING_PARAMETERS
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

        elif start_token == 'RES_DICOM_FRAME_LIST':
            for i,line in enumerate (token_line):
                if i<1: continue
                result.res_dicom_frame_list.append(token_line[i])

        else:
            skipped_tokens.add(start_token)

    print(f"Ignored tokens: {', '.join(skipped_tokens)}")
    return result

if __name__ == '__main__':
    test_file = 'case3.sw'
    test_file_name = r'File-conversion github\test_data\case3.sw'
    #os.path.join(os.getcwd(), 'test_data', test_file)
    data = parse_stradview_file(test_file_name)
    print(data)
