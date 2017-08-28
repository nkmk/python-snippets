import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--en', action='store_true')

args = parser.parse_args()
print(args.en)
print(type(args.en))
