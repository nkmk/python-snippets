def add(a, b):
    '''
    >>> add(1, 2)
    3
    >>> add(5, 10)
    15
    '''
    
    return a + b


if __name__ == '__main__':
    import sys
    result = add(int(sys.argv[1]), int(sys.argv[2]))
    print(result)
