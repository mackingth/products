import sys
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

motoki_koza1 = ''
motoki_koza2 = ''
motoki_pass = ''
ten_koza1 = ''
ten_koza2 = ''
ten_pass = ''
masaki_koza1 = ''
masaki_koza2 = ''
masaki_pass = ''

def job():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # もときのログイン
    def login1():
        driver.get('https://trade.smbcnikko.co.jp/Etc/1/webtoppage/')
        branch_code = driver.find_element_by_name('koza1')
        account_number = driver.find_element_by_name('koza2')
        pass_wd = driver.find_element_by_name('passwd')
        branch_code.send_keys(masaki_koza1)
        account_number.send_keys(masaki_koza2)
        pass_wd.send_keys(masaki_pass)
        pass_wd.submit()

    # 銘柄リスト
    brandnumber = []

    # 銘柄番号取得
    def find():
        driver.implicitly_wait(5)   #指定した待ち時間の間、要素が見つかるまで(ロードされるまで)待機します
        bigfinding = driver.find_element_by_id('market_info')
        smallfinding = bigfinding.find_element_by_xpath('table/tbody/tr/th[2]/table/tbody/tr/td[2]/div/a')
        smallfinding.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)

        # ウィンドウハンドルを取得する
        handle_array = driver.window_handles
        # seleniumで操作可能なdriverを切り替える
        driver.switch_to.window(handle_array[1])
        # smbcの銘柄の要素をスーパーパスを用いて取得
        superpass1 = driver.find_element_by_id('redips-drag')
        superpass2 = superpass1.find_element_by_xpath('table/tbody')
        # 実際の中身をtrをパスにして取得
        for i in range(1,11):
            tr_value = superpass2.find_element_by_xpath('tr[' + str(i) + ']')
            brandid = tr_value.find_element_by_id('meigCd')
            brandvalue = brandid.get_attribute('value')
            brandnumber.append(brandvalue)
            for j in range(2,11):
                brandid = tr_value.find_element_by_id('meigCd' + str(j))
                brandvalue = brandid.get_attribute('value')
                brandnumber.append(brandvalue)

        driver.close()
        driver.switch_to.window(handle_array[0])

    # 自分のログイン
    def login2(count : int):
        driver.back()
        driver.implicitly_wait(5)
        branch_code = driver.find_element_by_name('koza1')
        account_number = driver.find_element_by_name('koza2')
        pass_wd = driver.find_element_by_name('passwd')
        branch_code.clear()
        account_number.clear()
        if count == 0:
            branch_code.send_keys(ten_koza1)
            account_number.send_keys(ten_koza2)
            pass_wd.send_keys(ten_pass)
        elif count == 1:
            branch_code.send_keys(motoki_koza1)
            account_number.send_keys(motoki_koza2)
            pass_wd.send_keys(motoki_pass)
        pass_wd.submit()

    # 銘柄入替
    def replace():
        driver.implicitly_wait(5)   #指定した待ち時間の間、要素が見つかるまで(ロードされるまで)待機します
        bigfinding = driver.find_element_by_id('market_info')
        smallfinding = bigfinding.find_element_by_xpath('table/tbody/tr/th[2]/table/tbody/tr/td[2]/div/a')
        smallfinding.send_keys(Keys.ENTER)
        #driver.implicitly_wait(5)

        # ウィンドウハンドルを取得する
        handle_array = driver.window_handles
        # seleniumで操作可能なdriverを切り替える
        driver.switch_to.window(handle_array[1])
        # smbcの銘柄の要素をスーパーパスを用いて取得
        superpass1 = driver.find_element_by_id('redips-drag')
        superpass2 = superpass1.find_element_by_xpath('table/tbody')
        # 実際の中身をtrをパスにして入替
        count = 0
        for i in range(1,11):
            tr_value = superpass2.find_element_by_xpath('tr[' + str(i) + ']')
            brandid = tr_value.find_element_by_id('meigCd')
            brandid.clear()
            brandvalue = brandid.send_keys(brandnumber[count])
            count += 1
            for j in range(2,11):
                brandid = tr_value.find_element_by_id('meigCd' + str(j))
                brandid.clear()
                brandvalue = brandid.send_keys(brandnumber[count])
                count += 1
        brandid.send_keys(Keys.ENTER)
        driver.close()
        driver.switch_to.window(handle_array[0])

    login1()
    find()
    for i in range(2):
        login2(i)
        replace()
    driver.quit()

#メイン動作
if __name__ == "__main__":
    job()
    sys.exit()
