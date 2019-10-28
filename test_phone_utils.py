#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import phone_utils
reload(phone_utils)

def main():
    """main()"""
    expected = True
    arg = '000-000-0000'
    actual = phone_utils.is_valid_phone_number(arg)
    compare_expected_and_actual(arg, expected, actual)

    expected1 = True
    arg1 = '000-000-0000'
    actual1 = phone_utils.phone_number_has_letters(arg1)
    compare_expected_and_actual(arg1, expected1, actual1)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
