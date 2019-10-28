#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import gpx_utils
reload(gpx_utils)

def main():
    """main()"""
    expected = (-75.7472631,45.3888995)
    arg = '<trkpt lat="45.3888995" lon="-75.7472631">'
    actual = gpx_utils.get_coords_from_gpx(arg)
    compare_expected_and_actual(arg, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
