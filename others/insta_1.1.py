import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import chromedriver_binary

DOMAIN_BASE = "https://www.instagram.com/"
a = int(input('どのアカウントにしますか？: 1.本垢 2.jp用 3.お試し用 4.女子用\n'))
if a == 1:
    LOGIN_ID = ""
    PASSWORD = ""
    search_list = ['#A','#B','#C']
elif a == 2:
    LOGIN_ID = ""
    PASSWORD =  ""
    search_list = ['#D','#E','#F']
elif a == 3:
    LOGIN_ID = ""
    PASSWORD =  ""
    search_list = ['#G','#H','I']
else:
    LOGIN_ID = ""
    PASSWORD =  ""

length = len(search_list)

def get_driver():

    #　ヘッドレスモードでブラウザを起動
    options = Options()
    #options.add_argument('--headless')
    # ブラウザーを起動
    driver = webdriver.Chrome(options=options)
    return driver

def auto_good(driver):
    count = 0
    def good_action(num,driver):
        #いいねしてない時
        if len(driver.find_elements_by_xpath('//div[@class="QBdPU "]/span/*[name()="svg"][@aria-label="いいね！"][@height="24"]')) > 0:
            time.sleep(random.uniform(0,1))
            driver.find_element_by_xpath('//div[@class="QBdPU "]/span/*[name()="svg"][@aria-label="いいね！"][@height="24"]').click()
            print('いいねしました')
            num += 1
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        elif len(driver.find_elements_by_xpath('//div[@class="QBdPU rrUvL"]/span/*[name()="svg"][@aria-label="いいね！"][@height="24"]')) > 0:
            time.sleep(random.uniform(0,1))
            driver.find_element_by_xpath('//div[@class="QBdPU rrUvL"]/span/*[name()="svg"][@aria-label="いいね！"][@height="24"]').click()
            print('いいねしました')
            num += 1
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        #いいねされてる時
        else:
            print('いいねされてます')
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        return num


    try:
        for i in range(100):
            search = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
            search.clear()
            send_tag = search_list[random.randrange(length-1)]
            search.send_keys(send_tag)
            print('タグ: ',send_tag)
            search_list_first = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')))
            search_list_first.click()
            driver.implicitly_wait(20)
            #下まで読み込み
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(10)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div/div[8]')))
            x = random.randint(1,3)
            y = random.randint(1,3)
            #１行目//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]→/div[1],[2],[3]/a　各要素のアドレス
            #２行目//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]→/div[1],[2],[3]/a　各要素のアドレス
            #３行目//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]→/div[1],[2],[3]/a　各要素のアドレス
            #人気欄
            popular_list_pass = driver.find_element_by_id("react-root").find_element_by_xpath("section/main/"
                                                                                              "article/div[1]/div"
                                                                                              "/div/div[" + str(x) + "]/div[" + str(y) + "]/a")
            url = popular_list_pass.get_attribute('href')
            driver.execute_script("window.open()")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(url)
            driver.implicitly_wait(10)
            count = good_action(count,driver)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(10)
            time.sleep(2)
            ik = len(driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div'))
            #最新欄 3×8個デフォルト表示
            print('要素数 = ', ik)
            a = random.randint(1,ik)
            b = random.randint(1,3)
            c = random.randint(1,ik)
            d = random.randint(1,3)
            e = random.randint(1,ik)
            f = random.randint(1,3)
            g = random.randint(1,ik)
            h = random.randint(1,3)

            #１行目//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1],[2],[3]/a　各要素のアドレス
            #２行目//*[@id="react-root"]/section/main/article/div[2]/div/div[2]/div[1],[2],[3]/a　各要素のアドレス
            #３行目//*[@id="react-root"]/section/main/article/div[2]/div/div[3]/div[1],[2],[3]/a　各要素のアドレス
            #ここが止まる
            update_list_pass1 = driver.find_element_by_xpath("//*[@id='react-root']"
                                                            "/section/main/article/div[2]/div/"
                                                            "div[" + str(a) + "]/div[" + str(b) + "]/a")
            update_list_pass2 = driver.find_element_by_xpath("//*[@id='react-root']"
                                                            "/section/main/article/div[2]/div/"
                                                            "div[" + str(c) + "]/div[" + str(d) + "]/a")
            update_list_pass3 = driver.find_element_by_xpath("//*[@id='react-root']"
                                                            "/section/main/article/div[2]/div/"
                                                            "div[" + str(e) + "]/div[" + str(f) + "]/a")
            update_list_pass4 = driver.find_element_by_xpath("//*[@id='react-root']"
                                                            "/section/main/article/div[2]/div/"
                                                            "div[" + str(g) + "]/div[" + str(h) + "]/a")
            url1 = update_list_pass1.get_attribute('href')
            url2 = update_list_pass2.get_attribute('href')
            url3 = update_list_pass3.get_attribute('href')
            url4 = update_list_pass4.get_attribute('href')
            for o in range(4):
                if o == 0:
                    url = url1
                elif o == 1:
                    url = url2
                elif o == 2:
                    url = url3
                else:
                    url = url4
                driver.execute_script("window.open()")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(url)
                driver.implicitly_wait(10)
                count = good_action(count, driver)
            #time.sleep(random.uniform(1,10))
            print('i = ', i)
            print('count = ', count)
    except:
        return False


# Instagramログイン
def do_login(driver):
    # ログインURL
    login_url = DOMAIN_BASE + "accounts/login/"
    driver.get(login_url)
    # 電話、メールまたはユーザー名のinput要素が読み込まれるまで待機（最大10秒）
    elem_id = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    try:
        # パスワードのinput要素
        elem_password = driver.find_element_by_name("password")

        if elem_id and elem_password:
            # ログインID入力
            elem_id.send_keys(LOGIN_ID)
            # パスワード入力
            elem_password.send_keys(PASSWORD)
            # ログインボタンクリック
            elem_btn = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
            )
            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            actions.perform()
            # 適当（3秒間待つように対応しています）
            time.sleep(3)
            # 遷移後のURLでログイン可否をチェック
            perform_url = driver.current_url

            if perform_url.find(login_url) == -1:
                # ログイン成功
                auto_good(driver)
            else:
                # ログイン失敗
                return False

        else:
            return False
    except:
        return False
    """
    finally:
        os.kill(driver.service.process.pid,signal.SIGTERM)
    """


if __name__ == "__main__":
    # Driver
    driver = get_driver()
    # ログイン
    login_flg = do_login(driver)
    print(login_flg)

    driver.quit()
