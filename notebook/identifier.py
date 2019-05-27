AbcDef_123 = 100
print(AbcDef_123)
# 100

# AbcDef-123 = 100
# SyntaxError: can't assign to operator

# 1_abc = 100
# SyntaxError: invalid token

_abc = 100
print(_abc)
# 100

変数その１ = 100
print(変数その１)
# 100

# 変数。 = 100
# SyntaxError: invalid character in identifier

# ☺ = 100
# SyntaxError: invalid character in identifier

ﾍﾝｽｳＡＢＣ = 100
ヘンスウABC = -100

print(ﾍﾝｽｳＡＢＣ)
# -100

print(ヘンスウABC)
# -100

print(ﾍﾝｽｳＡＢＣ is ヘンスウABC)
# True

print('AbcDef_123'.isidentifier())
# True

print('AbcDef-123'.isidentifier())
# False

print('変数その１'.isidentifier())
# True

print('☺'.isidentifier())
# False

print('None'.isidentifier())
# True

# None = 100
# SyntaxError: can't assign to keyword

print(len)
# <built-in function len>

print(len('abc'))
# 3

len = 100
print(len)
# 100

# print(len('abc'))
# TypeError: 'int' object is not callable
