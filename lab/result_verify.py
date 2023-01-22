import numpy as np
from matplotlib import pyplot
import os
import glob
import natsort
import math

if __name__ == "__main__":
    n = 10240
    d_v = 3
    d_c = 4
    m = 7000
    x1 = []
    x2 = []

    get_dir = os.walk("./input")
                
    #カレントディレクトリを取得
    current_dir = os.getcwd()

    #入力ディレクトリを取得
    indir1 = current_dir + "/hash_codes/"
    indir2 = current_dir + "/verification/"
    indir3 = current_dir + "/parity_check_matrices/"

    #出力ディレクトリを取得
    outdir = current_dir + "/result_hash/"

    # 出力用フォルダがない場合は作る
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)
    
    H = np.loadtxt(indir3 + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_" + str(m) + str(n) + "_matrix.txt", dtype=int)
    verify_template = np.loadtxt(indir2 + "S1001L02_caht_lg_bin.txt",delimiter=",")

    all_text = glob.glob(indir1 + "/*.txt")
    storage_name = []
    for text in all_text:
        # 入力の名前を取得（拡張子付き）
        basename = os.path.basename(text)
        # 入力の名前から拡張子を分離
        name, ext = os.path.splitext(basename)
        storage_name.append(name)
    storage_name = np.array(natsort.natsorted(storage_name))  #昇順ストレージ

    storage = []
    for text_name in storage_name:
        storage.append(np.loadtxt(indir1 + text_name + ".txt", dtype=int))  # 行をmatに保存
    storage = np.array(storage)
    #print("storage ",storage.shape)

    temp1 = np.array(np.mod(H@verify_template, 2), dtype=int)
    with open(outdir + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + ".txt", 'w') as f:       
        for i in range(len(storage_name)):
            #print("H ",H.shape)
            #print("storage[i] ",storage[0][i].shape)
            hw = np.sum(np.mod(temp1 + storage[i], 2))
            wm = hw / H.shape[0]

            print("w/m for " + storage_name[i] + " = ",wm)
            if i <= 9:
                x1.append(wm)
            else:
                x2.append(wm)
            f.write("w/m for " + storage_name[i] + " = " + str(wm) + "\n")        
    pyplot.figure()
    pyplot.hist(x2,bins='auto',color='r')
    pyplot.hist(x1,bins='auto',color='b')
    pyplot.savefig(outdir + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_" + str(m) + str(n) + ".png")