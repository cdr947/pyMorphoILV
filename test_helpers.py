#!/usr/bin/env python3

import array
import unittest

import pyMorphoILV


class HelperTests(unittest.TestCase):
    def test_int2array_little_endian(self):
        self.assertEqual(pyMorphoILV.int2array(0x12345678), [0x78, 0x56, 0x34, 0x12])

    def test_short2array_little_endian(self):
        self.assertEqual(pyMorphoILV.short2array(0xABCD), [0xCD, 0xAB])

    def test_params_from_found_defaults(self):
        self.assertEqual(
            pyMorphoILV.paramsFromFound({}),
            (pyMorphoILV.def_baudrate, pyMorphoILV.def_endPOut, pyMorphoILV.def_endPIn),
        )

    def test_process_image_returns_bytes(self):
        row_number = 2
        col_number = 2
        image_data = [1, 2, 3, 4]
        buffer = array.array(
            'B',
            [
                0x3D,
                0x00,
                0x00,
                0x00,
                0x0A,
                row_number,
                0x00,
                col_number,
                0x00,
                0x01,
                0x00,
                0x01,
                0x00,
                0x00,
                0x00,
            ]
            + image_data,
        )
        processed = pyMorphoILV.Terminal.processImage(None, buffer, 0)
        self.assertEqual(processed["rowNumber"], row_number)
        self.assertEqual(processed["colNumber"], col_number)
        self.assertEqual(processed["huella"], bytes(image_data))


if __name__ == "__main__":
    unittest.main()
