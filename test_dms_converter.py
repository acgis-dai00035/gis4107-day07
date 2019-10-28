#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import dms_converter
reload(dms_converter)

def main():
    """main()"""
    expected = 'W'
    arg = '075 45 03 w 45 23 05 N\n'
    actual = dms_converter.get_e_or_w(arg)
    compare_expected_and_actual(arg, expected, actual)

    expected1 = 'N'
    arg1 = '075 45 03 w 45 23 05 n\n'
    actual1 = dms_converter.get_n_or_s(arg1)
    compare_expected_and_actual(arg1, expected1, actual1)

    expected2 = '-75.7508333333,45.3847222222'
    arg2 = '075 45 03 w 45 23 05 n\n'
    actual2 = dms_converter.dms2dd(arg2)
    compare_expected_and_actual(arg2, expected2, actual2)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
