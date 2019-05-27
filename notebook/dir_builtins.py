import pprint

print(type(dir(__builtins__)))
# <class 'list'>

print(len(dir(__builtins__)))
# 153

pprint.pprint(dir(__builtins__), compact=True)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
#  'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
#  'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
#  'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
#  'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
#  'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
#  'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
#  'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
#  'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
#  'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
#  'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
#  'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
#  'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
#  'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
#  'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
#  'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
#  'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
#  'Warning', 'ZeroDivisionError', '__IPYTHON__', '__build_class__', '__debug__',
#  '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',
#  'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
#  'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
#  'credits', 'delattr', 'dict', 'dir', 'display', 'divmod', 'enumerate', 'eval',
#  'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr',
#  'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
#  'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map',
#  'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow',
#  'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
#  'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
#  'vars', 'zip']

print(dir(__builtins__)[0])
# ArithmeticError

print(type(dir(__builtins__)[0]))
# <class 'str'>

pprint.pprint([s for s in dir(__builtins__) if s.islower() and not s.startswith('_')], compact=True)
# ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
#  'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
#  'credits', 'delattr', 'dict', 'dir', 'display', 'divmod', 'enumerate', 'eval',
#  'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr',
#  'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
#  'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map',
#  'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow',
#  'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
#  'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
#  'vars', 'zip']

pprint.pprint([s for s in dir(__builtins__) if s.endswith('Error')], compact=True)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BlockingIOError',
#  'BrokenPipeError', 'BufferError', 'ChildProcessError',
#  'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
#  'ConnectionResetError', 'EOFError', 'EnvironmentError', 'FileExistsError',
#  'FileNotFoundError', 'FloatingPointError', 'IOError', 'ImportError',
#  'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
#  'KeyError', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError',
#  'NotADirectoryError', 'NotImplementedError', 'OSError', 'OverflowError',
#  'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
#  'RuntimeError', 'SyntaxError', 'SystemError', 'TabError', 'TimeoutError',
#  'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
#  'UnicodeError', 'UnicodeTranslateError', 'ValueError', 'ZeroDivisionError']

pprint.pprint([s for s in dir(__builtins__) if s.endswith('Warning')], compact=True)
# ['BytesWarning', 'DeprecationWarning', 'FutureWarning', 'ImportWarning',
#  'PendingDeprecationWarning', 'ResourceWarning', 'RuntimeWarning',
#  'SyntaxWarning', 'UnicodeWarning', 'UserWarning', 'Warning']

print('len' in dir(__builtins__))
# True
