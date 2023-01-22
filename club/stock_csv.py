#Python 3.10.4
#15,10,5,3m前に起動

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process,Manager
import time
import os
import datetime
import sys

#chrome設定
print(datetime.datetime.now())
print("I'm working...")
cwdpath = os.getcwd()
pathChrome = cwdpath + "\chromedriver.exe"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
"""
code1 = '384'
code2 = '41513'
code3 = 'Masaki54'
"""
code1 = '242'
code2 = '177253'
code3 = 'p99isgod'

# 銘柄リスト初期化
brandnumber = []
brandname = []

# 今日の日付取得
dt = str(datetime.date.today())

# フォルダ作成
os.makedirs(dt, exist_ok=True)

# ログイン,100銘柄取得
def login1():
    driver.get('https://trade.smbcnikko.co.jp/Etc/1/webtoppage/')
    branch_code = driver.find_element("name", "koza1")
    account_number = driver.find_element("name", "koza2")
    pass_wd = driver.find_element("name", "passwd")
    branch_code.send_keys(code1)
    account_number.send_keys(code2)
    pass_wd.send_keys(code3)
    pass_wd.submit()
    driver.implicitly_wait(5)   #指定した待ち時間の間、要素が見つかるまで(ロードされるまで)待機します
    driver.find_element("id", "market_info").find_element('xpath', 'table/tbody/tr[1]/th[2]/table'
                                                                   '/tbody/tr/td[2]/div/a').click()
    driver.implicitly_wait(5)

    # ウィンドウハンドルを取得する
    handle_array = driver.window_handles
    # seleniumで操作可能なdriverを切り替える
    driver.switch_to.window(handle_array[1])
    # smbcの銘柄の要素をスーパーパスを用いて取得
    superpass = driver.find_element('id', 'redips-drag').find_element('xpath', 'table/tbody')
    # 実際の中身をtrをパスにして取得
    for i in range(1,11):
        for j in range(1,11):
            brand_name = superpass.find_element('xpath', 'tr[' + str(i) + ']').find_element('xpath', 'td[' + str(j) + ']').text
            brand_name = brand_name.replace('　', '')
            if j == 1:
                brandvalue = superpass.find_element('xpath', 'tr[' + str(i) + ']').find_element('id' , 'meigCd').get_attribute('value')
            else:
                brandvalue = superpass.find_element('xpath', 'tr[' + str(i) + ']').find_element('id' , 'meigCd' + str(j)).get_attribute('value')
            brandnumber.append(brandvalue)
            brandname.append(brand_name)
    driver.close()
    driver.switch_to.window(handle_array[0])
    driver.close()

def job(st,list_number,list_name,dummy,whole_list):
    def login2():
        driver.get('https://trade.smbcnikko.co.jp/Etc/1/webtoppage/')
        branch_code = driver.find_element('name' , 'koza1')
        account_number = driver.find_element('name' , 'koza2')
        pass_wd = driver.find_element('name' , 'passwd')
        branch_code.send_keys(code1)
        account_number.send_keys(code2)
        pass_wd.send_keys(code3)
        pass_wd.submit()
        driver.implicitly_wait(5)
    # 板のo/uを取得する
    def find(num: int):
        if num == 0 or num == 1 or num == 2 or num == 3:
            finding = driver.find_element('name' , 'meigNm')
            finding.send_keys(list_number[num])
            finding.send_keys(Keys.ENTER)
        else:
            finding2 = driver.find_element('xpath', '//*[@id="notForPrint"]/div[1]'
                                                        '/table/tbody/tr/td[2]/form/table/tbody/tr/td[3]/input')
            finding2.send_keys(list_number[num])
            finding2.send_keys(Keys.ENTER)

    #o/uのリスト
    def over_under():
        driver.implicitly_wait(20)
        iframe1 = driver.find_element('id' , 'qcs-content')
        #iframe2 = driver.find_element('id' , 'qcs-content2')
        driver.switch_to.frame(iframe1)
        driver.implicitly_wait(20)
        over = driver.find_element('xpath', '/html/body/div'
                                                '/div[3]/div[1]/div'
                                                '/table/tbody[1]/tr[2]'
                                                '/td[2]')
        under = driver.find_element('xpath', '/html/body/div'
                                                '/div[3]/div[1]/div'
                                                '/table/tbody[4]/tr'
                                                '/td[4]')
        offer_price = driver.find_element('xpath', '/html/body/div/div[3]/div[1]/div'
                                                   '/table/tbody[2]/tr[10]/td[3]/span')
        bid_price =  driver.find_element('xpath', '/html/body/div/div[3]/div[1]/div'
                                                  '/table/tbody[3]/tr[1]/td[3]/span')
        if over.text == ' ':
            over = '0'
        else:
            over = int(over.text.replace(',',''))
        if under.text == ' ':
            under = '0'
        else:
            under = int(under.text.replace(',',''))
        if offer_price.text == ' ':
            offer_price = '0'
        else:
            offer_price = int(offer_price.text.replace(',',''))
        if bid_price.text == ' ':
            bid_price = '0'
        else:
            bid_price = int(bid_price.text.replace(',',''))
        driver.switch_to.default_content()
        lis = [over, under, offer_price, bid_price] # over,under,offer,bid
        return lis

    login2()
    driver.implicitly_wait(10)
    for i in range(st,100,4):
        driver.implicitly_wait(10)
        find(i)
        driver.implicitly_wait(10)
        list_ou = over_under()
        driver.implicitly_wait(10)
        tmp_list = [i, list_number[i], list_name[i], list_ou[0], list_ou[1], list_ou[2], list_ou[3]]
        whole_list.append(tmp_list)
    driver.close()

# メイン動作
if __name__ == "__main__":
    #start = time.time()
    login1()     # 100銘柄取得

    for i in range(7):
        dt_now = datetime.datetime.now()
        #4並列処理
        manager = Manager()
        #空の辞書を定義
        dummy = manager.dict()
        whole_list = manager.list()
        detail_list = ['インデックス', '銘柄番号', '銘柄名', 'over', 'under', 'offer', 'bid']
        #外のwifiだと全部できていない、処理を完了するまで待たせる必要がある
        p1 = Process(target=job, args=(0,brandnumber,brandname,dummy,whole_list))
        p2 = Process(target=job, args=(1,brandnumber,brandname,dummy,whole_list))
        p3 = Process(target=job, args=(2,brandnumber,brandname,dummy,whole_list))
        p4 = Process(target=job, args=(3,brandnumber,brandname,dummy,whole_list))
        #p5 = Process(target=job, args=(4,brandnumber,brandname,dummy,whole_list))
        #p6 = Process(target=job, args=(5,brandnumber,brandname,dummy,whole_list))
        #p7 = Process(target=job, args=(6,brandnumber,brandname,dummy,whole_list))
        #p8 = Process(target=job, args=(7,brandnumber,brandname,dummy,whole_list))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        #p5.start()
        #p6.start()
        #p7.start()
        #p8.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        #p5.join()
        #p6.join()
        #p7.join()
        #p8.join()
        sort_list = sorted(whole_list)
        sort_list.insert(0,detail_list)
        with open( cwdpath + "/" + dt + "/" + dt_now.strftime('%Y-%m-%d-%H-%M') + '.csv', 'w', encoding='utf_8_sig') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(sort_list)
        #delta = time.time() - start
        time.sleep(120)
    print("done")
    sys.exit()

    #print(str(delta) + "s")
    # 20s かかる
