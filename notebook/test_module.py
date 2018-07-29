def func():
    print('    This is func() in test_module.py')
    print('    __name__ is', __name__)


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    print('call func()')
    func()
