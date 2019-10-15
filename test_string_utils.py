#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      evanw
#
# Created:     15-10-2019
# Copyright:   (c) evanw 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string_utlis
reload(string_utlis)

def main():
    """main()"""
    expected = '--'
    arg = 'a'
    actual = string_utlis.get_initials(arg)
    compare_expected_and_actual(arg, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()