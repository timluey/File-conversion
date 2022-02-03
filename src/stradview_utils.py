import os
from typing import Dict, List, Callable
from stradview_types import StradViewContour, StradViewData, StradViewImage, StradViewObject


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

_INT_PARAMETERS = [
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

_BOOLEAN_PARAMETERS = [
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

_FLOAT_PARAMETERS = [
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

_STRING_PARAMETERS = [
    'RES_BIN_IM_FILENAME',
    'RES_VERSION',
    'RES_DICOM_BMD_PHANTOM',
    'RES_BACKGROUND'
]

_ParserFunction = Callable[[StradViewData, List[str]], None]


def _make_int_parser(name: str) -> _ParserFunction:
    attr_name = name.lower()
    def parse(result: StradViewData, tokens: List[str]):
        value = int(tokens[0])
        setattr(result, attr_name, value)

    return parse


def _make_bool_parser(name: str) -> _ParserFunction:
    attr_name = name.lower()
    def parse(result: StradViewData, tokens: List[str]):
        if tokens[0]=='true\n':
            value = True
        elif tokens[0]== 'false\n':
            value = False
        else:
            raise ValueError()
        setattr(result, attr_name, value)
    return parse


def _make_float_parser(name: str) -> _ParserFunction:
    attr_name = name.lower()
    def parse(result: StradViewData, tokens: List[str]):
        value = float(tokens[0])
        setattr(result, attr_name, value)
    return parse


def _make_string_parser(name: str) -> _ParserFunction:
    attr_name = name.lower()
    def parse(result: StradViewData, tokens: List[str]):
        value = tokens[0]
        setattr(result, attr_name, value)

    return parse


def _parse_frame_list(result: StradViewData, token_line: List[str]):
    result.res_dicom_frame_list = [int(t) for t in token_line]


def _parse_image(result: StradViewData, tokens: List[str]):
    
    result.images.append(StradViewImage(
        time=int(tokens[0]),
        location=(float(tokens[1]),float(tokens[2]),float(tokens[3])),
        azimuth=float(tokens[4]),
        elevation=float(tokens[5]),
        roll=float(tokens[6])
    ))


def _parse_object(result: StradViewData, tokens: List[str]):
    
    result.objects.append(StradViewObject(
        number= int(tokens[0]),
        solid= int(tokens[1]),
        rgb= (float(tokens[2]),float(tokens[3]),float(tokens[4])),
        alpha= float(tokens[5]),
        rough= float(tokens[6]),
        metal= float(tokens[7]),
        name= tokens[8] + ' ' + tokens[9]        
    ))


def _parse_contour(result: StradViewData, tokens: List[str]):
    result.contours.append(StradViewContour(
        obj = int(tokens[0]),
        frame = int(tokens[1]),
        closed = int(tokens[2]),
        xy = [(float(x), float(y)) for x, y in zip(tokens[3::2], tokens[4::2])]
    ))
    

_PARSERS: Dict[str, _ParserFunction] = { 
    name: _make_int_parser(name) for name in _INT_PARAMETERS
} | {
    name: _make_bool_parser(name) for name in _BOOLEAN_PARAMETERS
} | {
    name: _make_float_parser(name) for name in _FLOAT_PARAMETERS
} | {
    name: _make_string_parser(name) for name in _STRING_PARAMETERS
} | {
    'RES_DICOM_FRAME_LIST': _parse_frame_list,
    'IM': _parse_image,
    'OBJECT': _parse_object,
    'CONT': _parse_contour
} 


def parse_stradview_file(path: str) -> StradViewData:

    with open(path) as file:
        token_lines = [line.split(' ') for line in file.readlines()]

    skipped_tokens = set()
    result = StradViewData()

    for token_line_ in token_lines:
        param_token = token_line_[0]

        if param_token in _PARSERS:
            _PARSERS[param_token](result, token_line_[1:])
        else:
            skipped_tokens.add(param_token)

    print(f"Ignored tokens: {', '.join(skipped_tokens)}")
    return result


if __name__ == '__main__':
    test_file = 'case3.sw'
    test_file_name = os.path.join(os.getcwd(), 'test_data', test_file)
    data = parse_stradview_file(test_file_name)
    print(data)
