import argparse
from distutils.util import strtobool

parser = argparse.ArgumentParser()
parser.add_argument('arg_bool', type=strtobool)

args = parser.parse_args()
print(args.arg_bool)
print(type(args.arg_bool))
