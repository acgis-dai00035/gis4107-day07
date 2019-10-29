#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import doc_scanner
reload(doc_scanner)

def main():
    """main()"""
    expected = True
    arg = 'adasdaTx6op3aasda'
    actual = doc_scanner.has_x_code(arg)
    compare_expected_and_actual(arg, expected, actual)

    expected1 =7
    arg1 = 'adasdaTx6op3aasda'
    actual1 = doc_scanner.get_x_code_position(arg1)
    compare_expected_and_actual(arg1, expected1, actual1)

    expected2 =7
    pattern = '456'
    arg2 = 'adasda456aasda'
    actual2 = doc_scanner.get_pattern_position(pattern,arg2)
    compare_expected_and_actual(arg2, expected2, actual2)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
