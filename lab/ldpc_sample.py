import numpy as np
from pyldpc import make_ldpc, encode, decode, get_message, parity_check_matrix

n = 15
d_v = 4
d_c = 5
snr = 100
H = parity_check_matrix(n, d_v, d_c)
print(H.shape[0])