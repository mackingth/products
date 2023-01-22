import os
import glob
import numpy as np
from natsort import natsorted

if __name__ == "__main__":
    n = 10240
    d_v = 3
    d_c = 4
    m = 7000

    get_dir = os.walk("./input")
    #カレントディレクトリを取得
    current_dir = os.getcwd()

    #入力ディレクトリを取得
    indir1 = current_dir + "/storage/"
    indir2 = current_dir + "/parity_check_matrices/"
    #出力ディレクトリを取得
    outdir = current_dir + "/hash_codes/"

    # 出力用フォルダがない場合は作る
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)
    #入力ディレクトリ内のテキストを選択
    all_text = glob.glob(indir1 + "/*.txt")
    storage_name = []
    for text in all_text:
        # 入力の名前を取得（拡張子付き）
        basename = os.path.basename(text)
        # 入力の名前から拡張子を分離
        name, ext = os.path.splitext(basename)
        storage_name.append(name)
    storage_name = np.array(natsorted(storage_name))  #昇順ストレージ

    storage = []
    for text_name in storage_name:
        row = []  # 各データを保存する行ベクトル
        with open(indir1 + text_name + ext, 'r', encoding='utf-8') as fin:  # ファイルを開く
            line = fin.readline()
            toks = line.split(',')  # 行をスペースで分割する
            for tok in toks:  # 分割したトークン列を回す
                num = int(tok)  # 整数に変換
                row.append(num)  # 行に保存
            storage.append(row)  # 行をmatに保存
    storage = np.array(storage)
    #print(storage)
    
    row = []  # 各データを保存する行ベクトル
    H = []  # parity check matrix
    H = np.loadtxt(indir2 + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_" + str(m) + str(n) + "_matrix.txt", dtype=int)
    for i in range(storage.shape[0]):
        print("i = ", i)
        result = np.mod(H@storage[i], 2)
        #print(result)
        np.savetxt(outdir + storage_name[i] + "_hash.txt", result, fmt='%d')