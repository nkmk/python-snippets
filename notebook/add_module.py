import sys


def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(float(sys.argv[1]), float(sys.argv[2])))
