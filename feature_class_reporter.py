

def main():
    """main()"""

def get_feature_type_from_name(fc_name ):
    """Given a letter a, b, c return x, y, z respectively
    """
    suffix = fc_name.partition('_')
    if suffix[1] == '_':
        return{
            'pnt': 'Point',
            'PNT': 'Point',
            'lin': 'Line',
            'LIN': 'Line',
            'ply': 'Polygon',
            'PLY': 'Polygon',
            }.get(suffix[2],'Unknown')

    else :
        return 'Unknown'

if __name__ == '__main__':
    main()
