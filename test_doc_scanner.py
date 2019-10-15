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
import doc_scanner
reload(doc_scanner)

def main():
    """main()"""
    expected = False
    arg = 'hjTx6op3kgd'
    actual = doc_scanner.has_x_code(arg)
    compare_expected_and_actual(arg, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
