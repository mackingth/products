import random
from pyldpc import make_ldpc, encode, decode, get_message, parity_check_matrix
import numpy as np
import os
import sympy


if __name__ == "__main__":
    n = 10240
    d_v = 3
    d_c = 4
    m = 7000
    H = np.zeros((m, n))

    get_dir = os.walk("./input")
    #カレントディレクトリを取得
    current_dir = os.getcwd()
    #出力ディレクトリを取得
    outdir = current_dir + "/parity_check_matrices/"

    # 出力用フォルダがない場合は作る
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)

    for i in range(H.shape[0]):
        a = []        
        while len(set(a)) != d_c:
            a = []
            for k in range(d_c):
                a.append(random.randrange(n))
        print(a)
        for j in a:
            H[i][j] = 1
        
    np.savetxt(outdir + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_" + str(m)+ str(n) + "_matrix.txt", H, fmt='%d')



"""
length = sympy.divisors(10240)
length.remove(1)
del length[8:]
n = 10240

if __name__ == "__main__":
    get_dir = os.walk("./input")
    #カレントディレクトリを取得
    current_dir = os.getcwd()
    #出力ディレクトリを取得
    outdir = current_dir + "/parity_check_matrices/"

    # 出力用フォルダがない場合は作る
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)
    for d_v in range(2,15):
        print("d_v = ", d_v)
        for d_c in length:
            if d_c <= d_v:
                continue
            else:
                H = np.array(parity_check_matrix(n, d_v, d_c))
                # np.set_printoptions(threshold=np.inf)
                np.savetxt(outdir + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_matrix.txt", H, fmt='%d')
"""