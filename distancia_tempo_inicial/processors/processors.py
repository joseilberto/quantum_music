import getopt
import sys

def get_arguments(args):
    song_name = ''
    make_bar_code = ''
    try:
        opts, args = getopt.getopt(args,"hs:b:",["song=","bar_code="])
    except:
        import pdb; pdb.set_trace()
        print('You should run this file like:'
                'script.py -s song_name -bc True/False')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('You should run this file like:'
                    'script.py -s song_name -bc True/False')
            sys.exit()
        elif opt in ("-s", "--song"):
            song_name = arg
        elif opt in ("-b", "--bar_code"):
            make_bar_code = arg.lower() in ['true']
    return song_name, make_bar_code
