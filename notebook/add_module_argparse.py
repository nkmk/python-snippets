import argparse
import add_module

parser = argparse.ArgumentParser()
parser.add_argument('a', type=int)
parser.add_argument('b', type=int)

args = parser.parse_args()
print(add_module.add(args.a, args.b))
