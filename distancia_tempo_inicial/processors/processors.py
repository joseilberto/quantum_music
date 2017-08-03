import getopt
import sys

def get_arguments(params, args = sys.argv[1:]):
    sattr, lattr, example = params
    attr, attr2 = '', ''
    try:
        opts, args = getopt.getopt(args, '{}{}:{}:'.format(*sattr), lattr)
    except:
        print('You should run this file like:'
        'script.py -{} {} -{} {}'.format(sattr[1], example[0], sattr[2], example[1]))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('You should run this file like:'
                    'script.py -{} {} -{} {}'.format(sattr[1], example[0],
                    sattr[2], example[1]))
            sys.exit()
        elif opt in ("-{}".format(sattr[1]), "--{}".format(lattr[0])):
            attr = arg
        elif opt in ("-{}".format(sattr[2]), "--{}".format(lattr[1])):            
            attr2 = arg
    return attr, attr2
