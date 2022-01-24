#pip install attr
import attr
from typing import List

@attr.s(auto_attribs=True)
class StradViewImage:
    pass


@attr.s(auto_attribs=True)
class StradViewData:
    res_buf_frames: int = 0
    """The number of frames of recorded data."""

    res_dicom_frame_list: List[int] = []
    """ """

    images: List[StradViewImage] = []
    """ """


def parse_stradview_file(path: str) -> StradViewData:
    file = open(path)
    token_lines = [line.split(' ') for line in file.readlines()]
    skipped_tokens = set()
    result = StradViewData()

    for token_line in token_lines:
        start_token = token_line[0]
        if start_token == 'RES_BUF_FRAMES':
            result.res_buf_frames = int(token_line[1])
        elif start_token == 'RES_DICOM_FRAME_LIST':
            pass
            # Do the conversion
        else:
            skipped_tokens.add(start_token)

    print(f"Ignored tokens: {', '.join(skipped_tokens)}")
    return result

if __name__ == '__main__':
    test_file_name = r"./test_data/case3.sw"
    data = parse_stradview_file(test_file_name)
    print(data)
