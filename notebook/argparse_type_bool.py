import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg_bool', type=bool)

args = parser.parse_args()
print(args.arg_bool)
print(type(args.arg_bool))
