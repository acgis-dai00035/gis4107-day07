

def main():
    """main()"""

def get_e_or_w(dms_record):
    """This function return an uppercase ?W? or ?E? depending on what is embedded in the record.
      That is, w, W, e, or E
    """
    clean = dms_record.replace('\n','').split()
    return clean[3].upper()


def get_n_or_s(dms_record):
    clean = dms_record.replace('\n','').split()
    return clean[7].upper()

def get_p_or_n(ewns):
    if ewns == 'E'  or ewns == 'N':
        return ''
    else:
        return '-'

def dms2dd(dms_record):
    clean = dms_record.replace('\n','').split()
    lat = float(clean[0]) + float(clean[1])/60 + float(clean[2])/3600
    lon = float(clean[4]) + float(clean[5])/60 + float(clean[6])/3600
    if lat >= 0 and lat <=180 and lon >= 0 and lon <=90 :
        lat_p_n = get_p_or_n(get_e_or_w(dms_record)) + str(lat)
        lon_p_n = get_p_or_n(get_n_or_s(dms_record)) + str(lon)
        return lat_p_n + ',' + lon_p_n
    else:
        return None


    return lat_p_n + ',' + lon_p_n


if __name__ == '__main__':
    main()
