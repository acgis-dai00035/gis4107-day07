#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import string_utils
reload(string_utils)

def main():
    """main()"""
    expected = 'Abc Bbc Cbc/A.B.C.'
    arg = 'Abc Bbc Cbc'
    actual = string_utils.get_initials(arg)
    compare_expected_and_actual(arg, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
