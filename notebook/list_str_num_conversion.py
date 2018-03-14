l_n = [-0.5, 0, 1.0, 100, 1.2e-2, 0xff, 0b11]

l_n_str = [str(n) for n in l_n]
print(l_n_str)
# ['-0.5', '0', '1.0', '100', '0.012', '255', '3']

l_i = [0, 64, 128, 192, 256]

l_i_hex1 = [hex(i) for i in l_i]
print(l_i_hex1)
# ['0x0', '0x40', '0x80', '0xc0', '0x100']

l_i_hex2 = [format(i, '04x') for i in l_i]
print(l_i_hex2)
# ['0000', '0040', '0080', '00c0', '0100']

l_i_hex3 = [format(i, '#06x') for i in l_i]
print(l_i_hex3)
# ['0x0000', '0x0040', '0x0080', '0x00c0', '0x0100']

l_f = [0.0001, 123.456, 123400000]

l_f_e1 = [format(f, 'e') for f in l_f]
print(l_f_e1)
# ['1.000000e-04', '1.234560e+02', '1.234000e+08']

l_f_e2 = [format(f, '.3E') for f in l_f]
print(l_f_e2)
# ['1.000E-04', '1.235E+02', '1.234E+08']

l_si = ['-10', '0', '100']

l_si_i = [int(s) for s in l_si]
print(l_si_i)
# [-10, 0, 100]

l_sf = ['.123', '1.23', '123']

l_sf_f = [float(s) for s in l_sf]
print(l_sf_f)
# [0.123, 1.23, 123.0]

l_sb = ['0011', '0101', '1111']

l_sb_i = [int(s, 2) for s in l_sb]
print(l_sb_i)
# [3, 5, 15]

l_sbox = ['100', '0b100', '0o77', '0xff']

l_sbox_i = [int(s, 0) for s in l_sbox]
print(l_sbox_i)
# [100, 4, 63, 255]

l_se = ['1.23e3', '0.123e-1', '123']

l_se_f = [float(s) for s in l_se]
print(l_se_f)
# [1230.0, 0.0123, 123.0]

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

l_multi = ['-100', '100', '1.23', '1.23e2', 'one']

l_multi_i = [int(s) for s in l_multi if is_int(s)]
print(l_multi_i)
# [-100, 100]

l_multi_f = [float(s) for s in l_multi if is_float(s)]
print(l_multi_f)
# [-100.0, 100.0, 1.23, 123.0]
