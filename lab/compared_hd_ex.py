from matplotlib import pyplot
import numpy as np
import os
import statistics
import math
import pandas as pd
from scipy import stats
import scipy

if __name__ == "__main__":

    K = 1000
    n = 10240
    mean_wm = 0
    prob1 = 0.75 # 0.75はダメ 0.7625はok
    prob2 = 0.5
    d_v = 3
    d_c = 4
    m = 7000
    x1 = []
    x2 = []
    figlist = [0.25]

    get_dir = os.walk("./input")
                
    #カレントディレクトリを取得
    current_dir = os.getcwd()

    #入力ディレクトリを取得
    indir1 = current_dir + "/parity_check_matrices/"

    #出力ディレクトリを取得
    outdir = current_dir + "/result_ex/"
    
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)

    H = np.loadtxt(indir1 + "d_v_" + str(d_v) + "_d_c_" + str(d_c) + "_" + str(m)+ str(n) + "_matrix.txt", dtype=int)

    for i in figlist:
        for k in range(K):
            print("k = ",k)
            v = []
            #w = []
            x = []
            #y = []
            for l in range(n):
                v.append(np.random.choice([0, 1], p=[1 - i, i]))
                #w.append(np.random.choice([0, 1], p=[prob1, 1-prob1]))
                x.append(np.random.choice([0, 1], p=[prob2, 1-prob2]))
                #y.append(np.random.choice([0, 1], p=[prob2, 1-prob2]))
            v = np.array(v)
            #w = np.array(w)
            x = np.array(x)
            #y = np.array(y)
            
            temp1 = H@v
            #temp2 = H@w
            temp3 = H@x
            #temp4 = H@y
            

            hw1 = np.sum(np.mod(temp1, 2))
            wm1 = hw1 / H.shape[0]
            hw2 = np.sum(np.mod(temp3, 2))
            wm2 = hw2 / H.shape[0]

            #print("wm1 = ",wm1)
            #print("wm2 = ",wm2)
            x1.append(wm1)
            x2.append(wm2)
        #print("mean_wm1 = ", statistics.mean(x1))
        #print("mean_wm2 = ", statistics.mean(x2))

        x1 = pd.Series(x1)
        x2 = pd.Series(x2)
        x1_mean = x1.mean()
        x2_mean = x2.mean()
        x1_std = x1.std(ddof=1)
        x2_std = x2.std(ddof=1)
        p0 = stats.shapiro(x1)[1]
        p1 = stats.shapiro(x2)[1]
        #F検定
        f_p = stats.bartlett(x1,x2).pvalue
        # Welchのｔ検定
        welch_t = stats.ttest_ind(x1,x2,equal_var=False)
        # studentのｔ検定
        student_t = stats.ttest_ind(x1,x2)

        print('処理を施した平均値 : {:f}'.format(x1_mean))
        print('処理を施してない平均値 : {:f}'.format(x2_mean))
        print('処理を施した標本分散 : {:f}'.format(x1_std))
        print('処理を施してない標本分散 : {:f}'.format(x2_std))
        print('処理を施したp値 : {:f}'.format(p0))
        print('処理を施してないp値 : {:f}'.format(p1))
        print('welchのt検定 : t = {:f}, p = {:e}'.format(welch_t.statistic,welch_t.pvalue))
        print('studentのt検定 : t = {:f}, p = {:e}'.format(student_t.statistic,student_t.pvalue))
        print(welch_t.pvalue)
        print(student_t.pvalue)
        print('f検定p値 : ')
        print(f_p)
        
        pyplot.clf()
        pyplot.figure()
        pyplot.hist(x1,bins='auto',color='b')
        pyplot.hist(x2,bins='auto',color='r')
        pyplot.xlabel("w/m")
        pyplot.ylabel("total")
        #pyplot.show()
        pyplot.savefig(outdir + "d_c_" + str(d_c) + "_" + str(m) + "_" + str(i) + "_0.5.png")