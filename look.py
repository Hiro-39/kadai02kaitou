import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd


# Chromeを起動する関数


def set_driver(driver_path,headless_flg):
    #chromeドライバー読みこみ
    options = ChromeOptions()
    
    #ヘッドレスモード（画面非表示モード）
    if headless_flg == True:
        options.add_argument('--headless')
        
    #起動オプション設定    
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windous NT 10.0; Win64; x64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    #　opions.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore.ssl-errors')
    options.add_argument('--incognito')
    
    # Chrome WebDriverオブジェクト作成
    return Chrome(executable_path=os.getcwd() +"/" + driver_path,options=options)
 
 # main処理
 
 
def main():
    search_keyword = "高収入"
    # driverを起動
    driver = set_driver("chromedriver.exe", False)
    # Web 開く
    driver.get("https://tenshoku.mynavi.jp") 
    time.sleep(5)
    # ポップアップ閉じる
    driver.execute_script('dobument.querySelector(".karte-clone").click()')
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector("karte-close").click()')
    
    #検索窓入力
    driver.find_element_by_class_name(
        "topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("cassetteRecruit__name")
    
    #ページ終了まで繰り返し取得
    exp_name_list = []
    #検索結果の一番上の会社名を取得
    name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
    
    #1ページ分切り返し
    print(len(name_list))
    for name in name_list:
        exp_name_list.append(name.text)
        print(name.text)
        
        
        
#　直接起動された場合はmain()を起動（モジュールとして呼び出された場合は起動しないようにするため）
if __name__ == "__main__":
    main()          