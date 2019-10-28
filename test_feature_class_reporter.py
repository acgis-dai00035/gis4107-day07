#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import feature_class_reporter
reload(feature_class_reporter)

def main():
    """main()"""
    expected = 'Point'
    arg = 'ABC_pnt'
    actual = feature_class_reporter.get_feature_type_from_name(arg)
    compare_expected_and_actual(arg, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
