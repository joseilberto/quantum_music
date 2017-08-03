import getopt
import sys

def get_arguments(argv):
    song_name = ''
    make_bar_code = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["song=","bar_code="])
    except getopt.GetoptError:
        print('script.py -s song_name -bc True/False')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -s song_name -bc True/False')
            sys.exit()
        elif opt in ("-s", "--song"):
            song_name = arg
        elif opt in ("-bc", "--bar_code"):
            make_bar_code = arg.lower() in ('true')
    return song_name, make_bar_code
