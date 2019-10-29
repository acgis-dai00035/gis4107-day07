
def main():
    """main()"""

def has_x_code(in_text):
    """Return True if the encoded string is found in in_text and False if it is not found
    """
    if in_text.find("Tx6op3") == -1 :
        return False
    else:
        return True

def get_x_code_position(in_text):
    """associate 1 with the first character in in_text.  If the code is not found, this function will return -1
    """
    if in_text.find("Tx6op3") == -1 :
        return in_text.find("Tx6op3")
    else:
        return in_text.find("Tx6op3")+1

def get_pattern_position(pattern,in_text):
    """associate 1 with the first character in in_text.  If the pattern is not found, this function will return -1
    """
    if in_text.find(pattern) == -1 :
        return in_text.find(pattern)
    else:
        return in_text.find(pattern)+1

if __name__ == '__main__':
    main()
