#pip install attr
from tokenize import Double
import attr
from typing import List

@attr.s(auto_attribs=True)
class StradViewImage:
    pass


@attr.s(auto_attribs=True)
class StradViewData:
    res_buf_frames: int = 0
    """The number of frames of recorded data."""

    res_buf_width: int = 0
    """	The width of scan-converted data, in pixels"""

    res_buf_height: int = 0
    """	The height of scan-converted data, in pixels"""

    res_buf_rf: bool = True
    """	Whether the recorded data is RF or scan-converted. Note that RF data can not be loaded by Stradview"""

    res_buf_dicom: bool = True
    """	Whether the recorded data is RF or scan-converted. Note that RF data can not be loaded by Stradview"""

    res_dicom_frame_list: List[int] = []
    """An ordered list of values indicating which DICOM or image files or frames are included in this Stradwin file.
    A value of zero indicates the first DICOM/image file found in this directory. """

    res_pos_rec: bool = True
    """Whether we have locational data with each image"""

    res_bin_im_filename: str = ''
    """The name of the binary ".sxi" file (including extension) to load with this ".sw" file. Alternatively, if RES_BUF_DICOM is true, the name of the first (lowest number)
    DICOM or image file to associate with this ".sw" file, or the directory containing these files"""
    
    res_version: int = 0
    """The Stradwin version which wrote this file"""

    res_corrected_pressure: bool = True
    """Whether the image data has been corrected for probe pressure using an image-based algorithm"""

    res_corrected_pos: bool = True
    """Whether the image data has been corrected for small positional errors using an image-based algorithm"""

    res_masked_data: int = 0
    """1 if the image data has been masked (non-data areas set to zero and ignored in visualisations), 0 otherwise"""

    res_invert_bscan: bool = True
    """Whether the probe surface is at the top (false) or bottom (true) of the displayed image"""

    res_buf_doppler: bool = True
    """Whether the data is grey-scale (B-scan) or colour (Doppler)"""

    res_xtrans: float = 0
    """The x (lateral) translation (in cm) from the top left corner of the image to the position sensor coordinate system."""

    res_ytrans: float = 0
    """	The y (axial) translation (in cm) from the top left corner of the image to the position sensor coordinate system"""

    res_ztrans: float = 0
    """The z (elevational) translation (in cm) from the top left corner of the image to the position sensor coordinate system."""

    res_azimuth: float = 0
    """The Euler azimuth (in degrees from -180 to 180) from the top left corner of the image to the position sensor coordinate system"""

    res_elevation: float = 0
    """The Euler elevation (in degrees from -90 to 90) from the top left corner of the image to the position sensor coordinate system"""

    res_roll: float = 0
    """The Euler roll (in degrees from -90 to 90) from the top left corner of the image to the position sensor coordinate system"""

    res_xscale: float = 0
    """The lateral (x) scale of the scan-converted image, in cm per pixel"""

    res_yscale: float = 0
    """The axial (y) scale of the scan-converted image, in cm per pixel"""

    res_pos_manual: bool = True
    """Whether the positions have been manually entered."""

    res_pos_manual_tran: int = 0
    """The axis (or 0 for no translation) for manually entered positions"""

    res_pos_manual_span: float = 0
    """The total translation distance in mm for manually entered positions"""

    res_pos_manual_rot: int = 0
    """The axis (or 0 for no rotation) for manually entered rotations"""

    res_pos_manual_angle: int = 0
    """The total rotation angle in degrees for manually entered rotations"""

    res_pos_manual_radius: int = 0
    """The offset radius in mm about which the rotations occurs for manually entered rotations"""

    res_dicom_hum: float = 0
    """	Part of the conversion between raw data values and Hounsfield Units (HU), where HU = (raw * DICOM_HUM) + DICOM_HUB"""

    res_dicom_hub: float = 0
    """Part of the conversion between raw data values and Hounsfield Units (HU), where HU = (raw * DICOM_HUM) + DICOM_HUB"""

    res_dicom_win_width: float = 0
    """The window width for DICOM display, in Hounsfield Units. The default value is whatever is stored in the corresponding DICOM files"""

    res_dicom_win_centre: float = 0
    """The window centre for DICOM display, in Hounsfield Units. The default value is whatever is stored in the corresponding DICOM files"""

    res_dicom_filter: int = 0
    """Applies a Gaussian filter of extent (2*RES_DICOM_FILTER+1) to the raw data before windowing, to remove noise. '0' turns this filter off"""

    res_dicom_bmd_phantom: str = ''
    """The phantom which was detected in CT data and used to convert Hounsfield Units to density, or 'No' if this has not been done"""

    res_dicom_bmd_scale: float = 0
    """Part of the conversion between Hounsfield Units (HU) and density (mg/cm3), where density = (HU-BMD_OFFSET)/BMD_SCALE"""

    res_dicom_bmd_offset: float = 0
    """Part of the conversion between Hounsfield Units (HU) and density (mg/cm3), where density = (HU-BMD_OFFSET)/BMD_SCALE"""

    res_thickness_scale_mm: int = 0
    """The maximum scale value (in tenths of a mm) for the surface colour map when displaying bone cortical thickness estimation from CT DICOM data."""

    res_thickness_scale_hu: int = 0
    """The scale value range (in 100 Hounsfield Units) for the surface colour map when displaying bone cortical density estimation from CT DICOM data"""

    res_thickness_zero_hu: int = 0
    """The minimum scale value (in 100 Hounsfield Units) for the surface colour map when displaying bone cortical density estimation from CT DICOM data"""

    res_thickness_scale_humm: int = 0
    """The scale value range (in 1000 Hounsfield Unit x mm) for the surface colour map when displaying bone cortical mass estimation from CT DICOM data"""

    res_thickness_type: float = 0
    """The type of thickness algorithm used. This corresponds to the index (starting from zero) in the 'technique' choice in the thickness task page"""

    res_thickness_line: float = 0
    """The line length in cm for bone cortical thickness estimation from CT DICOM data"""

    res_thickness_gauss: float = 0
    """The std for the Gaussian blur in cm for bone cortical thickness estimation from CT DICOM data. 1e10 indicates the value should be estimated from the data"""

    res_thickness_rect: float = 0
    """The size of rectangular blur in cm for bone cortical thickness estimation from CT DICOM data. 1e10 indicates the value should be estimated from the data"""

    res_thickness_a: float = 0
    """The external CT value in HU for bone cortical thickness estimation from CT DICOM data. 1e10 indicates the value should be estimated from the data"""

    res_thickness_b: float = 0
    """The cortical CT value in HU for bone cortical thickness estimation from CT DICOM data. 1e10 indicates the value should be estimated from the data"""

    res_thickness_c: float = 0
    """The trabecular CT value in HU for bone cortical thickness estimation from CT DICOM data. 1e10 indicates the value should be estimated from the data"""

    res_thickness_a_average: float = 0
    """The average external CT value in HU for bone cortical thickness estimation from CT DICOM data.
    Only used when also modelling metal in CT data. 1e10 indicates the average has not been measured"""
    
    res_thickness_c_average: float = 0
    """The average trabecular CT value in HU for bone cortical thickness estimation from CT DICOM data.
    Only used when also modelling metal in CT data. 1e10 indicates the average has not been measured"""

    res_thickness_create_inner: bool = True
    """Whether to include the inner (endocortical) surface when creating a new surface from cortical thickness measurements"""

    res_thickness_create_outer: bool = True
    """Whether to include the outer (periosteal) surface when creating a new surface from cortical thickness measurements"""

    res_thickness_create_caps: bool = True
    """Whether to include the end cap (which closes the surface) when creating a new surface from cortical thickness measurements"""

    res_thickness_outlier_reject: int = 0
    """When creating a surface from cortical thickness measurements, whether to exclude measurements which represent too high a curvature (less then given angle)"""

    res_thickness_distance_reject: int = 0
    """When creating a surface from cortical thickness measurements, whether to exclude measurements too far away from the original surface (in pixels, 40 disables)"""

    res_thickness_map_direction: int = 0
    """Corresponds to the 'Map direction' choice in the thickness task page, where 0 = 'Normal', i.e. do not change the measurement directions"""

    res_background: str = ''
    """The colour used for background (non-data) in the data windows, as three hexadecimal RGB values"""

    res_shader: int = 0
    """The shader used to draw surfaces in the 3D window, as an index into the 'graphics shader' selection box.
    Only affects displays if your driver supports at least OpenGL 3.0"""

    res_lighting_ambient: float = 0
    """The amount of ambient light in the 3D window, in a range from 0.0 to 1.0. The radiant lighting is decreased proportionally as this value is increased"""

    res_lighting_front_side: float = 0
    """The relative importance of the side and the front light in the 3D window, in a range from 0.0 (front light only) to 1.0 (side light only).
    Since shadowing is only generated by the side light, this also controls the depth of the shadows"""

    res_occlusion_range: int = 0 
    """The extent of ambient occlusion modelling in the 3D window. Setting this to zero disables this feature, which was the default before version 7.0.
    Only affects displays if your driver supports at least OpenGL 3.0"""

    res_radiant_shadows: bool = True
    """Whether shadowing from the side lighting is included in the 3D window. Only affects displays if your driver supports at least OpenGL 3.0"""

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
        elif start_token == 'RES_BUF_WIDTH':
            result.res_buf_width = int(token_line[1])
        elif start_token == 'RES_BUF_HEIGHT':
            result.res_buf_height = int(token_line[1])
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
            for i,line in enumerate (token_line):
                if i<1: continue
                result.res_dicom_frame_list.append(token_line[i])
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
            elif token_line[1]== 'false\n':
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
    test_file_name = r"C:\Users\timot\OneDrive\Desktop\Formus Labs\Code\File-conversion github/test_data/case3.sw"
    data = parse_stradview_file(test_file_name)
    print(data)
