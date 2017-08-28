import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg_int', type=int)

args = parser.parse_args()
print(args.arg_int)
print(type(args.arg_int))
