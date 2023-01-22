from matplotlib import pyplot
import os
import glob
from pyldpc import make_ldpc, encode, decode, get_message, parity_check_matrix
import numpy as np
from natsort import natsorted
import sys
import math
import sympy
from scipy.spatial import distance

from scipy.fftpack import shift
length = sympy.divisors(10240)
length.remove(1)
del length[11:]

if __name__ == "__main__":
    for d_v in range(2,100):    # variable nodes degree
        for d_c in length:      # check nodes degree
            if d_c <= d_v:
                continue
            else:
                shift = 8
                x = []
                get_dir = os.walk("./input")
                
                #カレントディレクトリを取得
                current_dir = os.getcwd()

                #入力ディレクトリを取得
                indir1 = current_dir + "/storage/"
                indir2 = current_dir + "/verification/"
                #出力ディレクトリを取得
                outdir = current_dir + "/result/"

                # 出力用フォルダがない場合は作る
                if os.path.isdir(outdir) == False:
                    os.mkdir(outdir)
                #入力ディレクトリ内のテキストを選択
                all_text1 = glob.glob(indir1 + "/*.txt")
                all_text2 = glob.glob(indir2 + "/*.txt")

                storage = []  # 全てのベクトルを挿入した行列
                veri_temp = [] #比較用テンプレ
                storage_name = [] #名前リスト
                with open(outdir + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_result.txt", 'w') as f:
                    # それぞれのテキストに対する処理
                    print("loading storage...")
                    f.write("loading storage...\n")
                    for text in all_text1:
                        # 入力の名前を取得（拡張子付き）
                        basename = os.path.basename(text)
                        # 入力の名前から拡張子を分離
                        name, ext = os.path.splitext(basename)
                        storage_name.append(name)
                    storage_name = natsorted(storage_name)  #昇順ストレージ
                    #print(storage_name)

                    for text_name in storage_name:
                        row = []  # 各データを保存する行ベクトル
                        with open(indir1 + text_name + ext, 'r', encoding='utf-8') as fin:  # ファイルを開く
                            line = fin.readline()
                            toks = line.split(',')  # 行をカンマで分割する
                            for tok in toks:  # 分割したトークン列を回す
                                num = int(tok)  # 整数に変換
                                row.append(num)  # 行に保存
                            storage.append(row)  # 行をmatに保存
                    storage = np.array(storage)
                    #print(storage)  # 結果を出力
                    #print("storage.shape = ",storage.shape)
                    
                    print("loading template for verification...")
                    f.write("loading template for verification...\n")
                    for text in all_text2:
                        # 入力の名前を取得（拡張子付き）
                        basename = os.path.basename(text)
                        # 入力の名前から拡張子を分離
                        name, ext = os.path.splitext(basename)
                        #save_path = outdir + name + "_caht_lg_bin.txt" # pbmやbmpでも大丈夫
                        row = []  # 各データを保存する行ベクトル
                        with open(indir2 + basename, 'r', encoding='utf-8') as fin:  # ファイルを開く
                            line = fin.readline()
                            toks = line.split(',')  # 行をカンマで分割する
                            for tok in toks:  # 分割したトークン列を回す
                                num = int(tok)  # 整数に変換
                                row.append(num)  # 行に保存
                            veri_temp.append(row)  # 行をmatに保存
                    veri_temp = np.array(veri_temp)
                    #print(veri_temp)  # 結果を出力
                    #print("veri_temp.shape = ",veri_temp.shape)

                    N = storage.shape[1]
                    K = storage.shape[0]
                    H = np.array(parity_check_matrix(N, d_v, d_c))
                    #print("H.shape = ",H.shape)
                        
                    # 行列の計算
                    for k in range(K):  #range(K)
                        syndrome = []
                        print("----------------------------------------------------------")
                        f.write("----------------------------------------------------------\n")
                        print("k = ",k)
                        f.write("k = ")
                        f.write(str(k) + "\n")
                        v = np.array(storage[k])
                        #print("v = ",v)

                        # optimal hamming distance
                        shift_arg = []
                        for t in range(-shift,shift+1):
                            roll = np.roll(veri_temp[0],t)
                            shift_arg.append(distance.hamming(roll,v))
                        #print("shift_arg = ",shift_arg)
                        print("optimal_min_hd = ",min(shift_arg))
                        f.write("optimal_min_hd = ")
                        f.write(str(min(shift_arg)) + "\n")
                        #print("index = ",shift_arg.index(min(shift_arg)))
                        ind = shift_arg.index(min(shift_arg))
                        shift_count = ind - shift
                        alignment_template = np.array(np.roll(veri_temp[0],shift_count))

                        # parity check matrixをかける
                        add_temp = np.mod(v + alignment_template, 2)    # テンプレ同士の和(差)
                        result = np.mod(H@add_temp, 2)     # シンドローム

                        mlq = sum(result) / H.shape[0]
                        #print("Hamming weight for each k = ",mlq)

                        # error estimation for iris code
                        if mlq <= 0.5:
                            er_pro = (1 - math.pow((1 - 2 * mlq), 1/d_c)) / 2
                        else:
                            er_pro = 0.5
                        print("error probability for " + storage_name[k] + " = ",er_pro)
                        x.append(er_pro)
                        f.write("error probability for ")
                        f.write(str(storage_name[k]))
                        f.write( " = ")
                        f.write(str(er_pro) + "\n")
                pyplot.figure()
                pyplot.hist(x,bins='auto')
                pyplot.savefig(outdir + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + ".png")