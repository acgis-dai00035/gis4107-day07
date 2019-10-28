

def main():
    """main()"""

def get_coords_from_gpx(gpx):
    """Given the above GPX trkpt element, this function would return (-75.7472631,45.3888995).
      If the GPX in the function call does not contain trkpt, return None.
    """
    list1 = gpx.split()
    if list1[0].find('trkpt'):
        lat = list1[1].partition('"')
        lon = list1[2].partition('"')
        return float(lon[2].replace('">','')),float(lat[2].replace('"',''))
    else:
        return None
if __name__ == '__main__':
    main()
