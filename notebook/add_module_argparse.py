import argparse
import add_module

parser = argparse.ArgumentParser()
parser.add_argument('a', type=float)
parser.add_argument('b', type=float)

args = parser.parse_args()
print(add_module.add(args.a, args.b))
