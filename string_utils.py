

def main():
    """main()"""

def get_initials(full_name):
    """Given a name return the initials
    """
    initials = ''
    for i in full_name.split():
        initials += i[0]+'.'
    return full_name+'/'+initials



if __name__ == '__main__':
    main()
