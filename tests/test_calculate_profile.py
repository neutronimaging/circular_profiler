import pytest
from pathlib import Path
from PIL import Image
import numpy as np

from src.calculate_profiles import CalculateProfiles


class TestCalculateProfile:

    def setup_method(self):
        data_path = Path(__file__).parent
        self.images_path = Path(data_path) / 'data'

        image_file1 = str(self.images_path / 'image_0001.tiff')
        image_file2 = str(self.images_path / 'image_0002.tiff')

        self.image1 = np.asarray(Image.open(image_file1))
        self.image2 = np.asarray(Image.open(image_file2))

    def test_build_angles_matrix(self):
        image_width = 10
        image_height = 10
        x_central_pixel = 4
        y_central_pixel = 4

        calculated_angles_matrix = CalculateProfiles.build_angles_matrix(image_width=image_width,
                                                                         image_height=image_height,
                                                                         x_central_pixel=x_central_pixel,
                                                                         y_central_pixel=y_central_pixel)

        expected_angles_matrix = np.array([[315., 323.13010235, 333.43494882, 345.96375653,
                                            0., 14.03624347, 26.56505118, 36.86989765,
                                            45., 51.34019175],
                                           [306.86989765, 315., 326.30993247, 341.56505118,
                                            0., 18.43494882, 33.69006753, 45.,
                                            53.13010235, 59.03624347],
                                           [296.56505118, 303.69006753, 315., 333.43494882,
                                            0., 26.56505118, 45., 56.30993247,
                                            63.43494882, 68.19859051],
                                           [284.03624347, 288.43494882, 296.56505118, 315.,
                                            0., 45., 63.43494882, 71.56505118,
                                            75.96375653, 78.69006753],
                                           [270., 270., 270., 270.,
                                            np.NaN, 90., 90., 90.,
                                            90., 90.],
                                           [255.96375653, 251.56505118, 243.43494882, 225.,
                                            180., 135., 116.56505118, 108.43494882,
                                            104.03624347, 101.30993247],
                                           [243.43494882, 236.30993247, 225., 206.56505118,
                                            180., 153.43494882, 135., 123.69006753,
                                            116.56505118, 111.80140949],
                                           [233.13010235, 225., 213.69006753, 198.43494882,
                                            180., 161.56505118, 146.30993247, 135.,
                                            126.86989765, 120.96375653],
                                           [225., 216.86989765, 206.56505118, 194.03624347,
                                            180., 165.96375653, 153.43494882, 143.13010235,
                                            135., 128.65980825],
                                           [218.65980825, 210.96375653, 201.80140949, 191.30993247,
                                            180., 168.69006753, 158.19859051, 149.03624347,
                                            141.34019175, 135.]])

        matrix_height, matrix_width = np.shape(calculated_angles_matrix)
        assert matrix_height == image_height
        assert matrix_width == image_width

        for _row_index, _row_entry in enumerate(expected_angles_matrix):
            for _col_index, _col_entry in enumerate(_row_entry):
                pytest.approx(_col_entry, calculated_angles_matrix[_row_index, _col_index], 1e-6)

        # assert False
