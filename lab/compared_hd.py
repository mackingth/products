from matplotlib import pyplot
import os
import glob
import numpy as np
import sys
import statistics
from scipy.spatial import distance

x = []
mean_hd = 0
shift = 8
shift_k = 20

if __name__ == "__main__":
    get_dir = os.walk("./input")
    
    #カレントディレクトリを取得
    current_dir = os.getcwd()

    #入力ディレクトリを取得
    indir = current_dir + "/output_bin/"

    #出力ディレクトリを取得
    outdir = current_dir + "/hd_output/"

    # 出力用フォルダがない場合は作る
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)

    #入力ディレクトリ内のテキストを選択
    all_text = glob.glob(indir + "/*.txt")

    mat = []  # 全てのベクトルを挿入した行列
    # それぞれのテキストに対する処理
    for text in all_text:

        # 入力の名前を取得（拡張子付き）
        basename = os.path.basename(text)
        print(basename)

        # 入力の名前から拡張子を分離
        name, ext = os.path.splitext(basename)

        #save_path = outdir + name + "_caht_lg_bin.txt" # pbmやbmpでも大丈夫

        row = []  # 各データを保存する横ベクトル
        with open(indir + basename, 'r', encoding='utf-8') as fin:  # ファイルを開く
            line = fin.readline()
            toks = line.split(',')  # 行をカンマで分割する
            for tok in toks:  # 分割したトークン列を回す
                num = int(tok)  # 整数に変換
                row.append(num)  # 行に保存
            mat.append(row)  # 行をmatに保存
    mat = np.array(mat)
    print(mat)  # 結果を出力
    print(mat.shape)
    N = mat.shape[1]
    K = mat.shape[0]
    v = mat[0]
    with open(outdir + "hd.txt", "w") as f:

        for k in range(K):
            hd = 0
            w = mat[k]
            #print("k = ",k)
            f.write("k = ")
            f.write(str(k))
            f.write("\n")

            # optimal hamming distance
            shift_arg = []
            shift_count = 0
            for t in range(-shift * shift_k, shift * shift_k+1 ,shift):
                roll = np.roll(v,t)
                shift_arg.append(distance.hamming(roll,w))
            #print("shift_arg = ",shift_arg)
            #f.write("shift_arg = ")
            #f.write(str(shift_arg))
            #f.write("\n")
            #print("optimal_min_hd = ",min(shift_arg))
            f.write("optimal_min_hd = ")
            f.write(str(min(shift_arg)))
            f.write("\n")
            #print("index = ",shift_arg.index(min(shift_arg)))
            
            ind = shift_arg.index(min(shift_arg))
            shift_count = ind - shift
            alignment_template = np.roll(v,shift_count)
            
            x.append(distance.hamming(alignment_template,w))

    print("mean_hd = ",statistics.mean(x))
    pyplot.hist(x,bins='auto')
    pyplot.savefig(current_dir + "/with_alignment.png")
    """
    pyplot.savefig(current_dir + "/without_alignment.png")
    """