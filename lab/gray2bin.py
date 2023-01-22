import os
import glob
import cv2
from PIL import Image

if __name__ == "__main__":
    get_dir = os.walk("./input")

    #カレントディレクトリを取得
    current_dir = os.getcwd()

    #入力ディレクトリを取得
    indir = current_dir + "/input/"

    #出力ディレクトリを取得
    outdir = current_dir + "/output_bin/"

    # 出力用フォルダがない場合は作る
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)

    #入力ディレクトリ内の画像を選択
    all_images = glob.glob(indir + "/*/*/*/*.jpg")

    # それぞれの画像に対する処理
    for img in all_images:

        # 入力画像の画像名を取得（拡張子付き）
        basename = os.path.basename(img)
        print(basename)

        # 入力画像の画像名から拡張子を分離
        name, ext = os.path.splitext(basename)

        # 2値画像に変換した画像の保存先
        save_path = outdir + name + "_caht_lg_bin.txt" # pbmやbmpでも大丈夫

        im_gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE) #grayscale読み込み
        abc = []
        for x in range(im_gray.shape[1]):
            #print(im_gray[0,x])
            #print(format(im_gray[0,x],'08b'))
            #print(type(format(im_gray[0,x],'08b')))
            #print(list(format(im_gray[0,x],'08b')))
            abc.extend(list(format(im_gray[0,x],'08b')))
        #print(abc)
        #print(len(abc))
        with open(save_path, 'w') as f:
            f.write(', '.join(map(str, abc)))