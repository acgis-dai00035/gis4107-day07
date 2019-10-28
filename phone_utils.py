

def main():
    """main()"""

def is_valid_phone_number(phone_number):
    """returns True if the phone number has all numbers and has the format
    shown above (i.e. 3 numbers, a dash, etc).  It returns False if any character
    is not a number (except the dashes) or it does not have the above format
    """
    if phone_number.count('-') == 2 :
        new_numnber = phone_number.replace('-',' ')
        if new_numnber.count(' ') == 2:
            number_list = new_numnber.split()
            if number_list[0].isdigit and number_list[1].isdigit and number_list[2].isdigit and len(number_list[0])==3 and len(number_list[1])==3 and len(number_list[2])==4 :
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def phone_number_has_letters(phone_number):
    """returns True if the phone number contains 1 or more letters and False if
    it does not.  If it does not have the NNN-NNN-NNNN format, return False.
    If it has the NNN-NNN-NNNN format, the first three digits are numbers,
    and any of the remaining characters are letters, return True.
    """
    if phone_number.count('-') == 2 :
        new_numnber = phone_number.replace('-',' ')
        if new_numnber.count(' ') == 2:
            number_list = new_numnber.split()
            if len(number_list[0])==3 and len(number_list[1])==3 and len(number_list[2])==4 and number_list[0].isdigit:
                rest = number_list[1] + number_list[2]
                count_letter = 0
                count_number = 0
                for i in rest :
                    if i.isalpha():
                        count_letter += 1
                    elif i.isdigit() :
                        count_number += 1
                    else:
                        return False
                if count_letter > 0 :
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    main()
