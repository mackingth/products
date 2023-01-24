import sys
from selenium import webdriver
import time
import os
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import datetime

ten_koza1 = ''
ten_koza2 = ''
ten_pass = ''
file_name = '' + datetime.datetime.now().strftime('%Y-%m-%d') + '_values_volume'

# 銘柄リスト
a = int(input('TOP6+6 or NEWS\nTOP6+6 = 1\nNEWS = 2\n'))
brandnumber = list(map(int,input("どの銘柄の4本値と出来高,陽線率を表示しますか?(番号の間は空白を入力してください)\n").split()))
terms = ['名前', '始値', '高値', '安値', '終値', '出来高', '高値陽線率', '終値陽線率']
whole_list = []
if a == 1:
    file_name += '_TOP6+6.csv'
else:
    file_name += '_NEWS.csv'

def job():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # 俺のログイン
    def login1():
        driver.get('https://trade.smbcnikko.co.jp/Etc/1/webtoppage/')
        branch_code = driver.find_element_by_name('koza1')
        account_number = driver.find_element_by_name('koza2')
        pass_wd = driver.find_element_by_name('passwd')
        branch_code.send_keys(ten_koza1)
        account_number.send_keys(ten_koza2)
        pass_wd.send_keys(ten_pass)
        pass_wd.submit()

    # 4本値,出来高取得
    def find(num: int):
        driver.implicitly_wait(20)
        finding = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[2]/form/table/tbody/tr/td[3]/input')
        finding.send_keys(brandnumber[num])
        finding.send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        name = driver.find_element_by_id('cloneOrg1').find_element_by_xpath('tbody/tr/td[2]/h2').text
        iframe1 = driver.find_element_by_id('qcs-content')
        driver.switch_to.frame(iframe1)
        driver.implicitly_wait(20)      #10秒でいける
        a = driver.find_element_by_class_name('qcs-middle-content')
        b = a.find_element_by_class_name('info-area')
        open = b.find_element_by_xpath('tbody/tr/td')
        high = b.find_element_by_xpath('tbody/tr[2]/td/span[2]')
        low = b.find_element_by_xpath('tbody/tr[3]/td/span[2]')
        volume = b.find_element_by_xpath('tbody/tr[5]/td')
        c = driver.find_element_by_class_name('qcs-bottom-content')
        close = c.find_element_by_xpath('div[2]/div/table/tbody/tr[4]/td[3]')

        if open.text == ' ':
            open = '0'
        else:
            open = float(open.text.replace(',',''))
        if high.text == ' ':
            high = '0'
        else:
            high = float(high.text.replace(',',''))
        if low.text == ' ':
            low = '0'
        else:
            low = float(low.text.replace(',',''))
        if volume.text == ' ':
            volume = '0'
        else:
            volume = float(volume.text.replace(',',''))
        if close.text == ' ':
            close = '0'
        else:
            close = float(close.text.replace(',',''))
        driver.switch_to.default_content()
        driver.find_element_by_name('menu01').click()
        high_rate = (high - open) / open * 100
        close_rate = (close - open) / open * 100
        lis = [name,open,high,low,close,volume,str(round(high_rate,2)) + '%',str(round(close_rate,2)) + '%']
        whole_list.append(lis)


    #メイン動作
    login1()
    whole_list.append(terms)
    for i in range(len(brandnumber)):
        find(i)
    with open(file_name, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(whole_list)
    driver.quit()

if __name__ == "__main__":
    job()
    sys.exit()
