# 安裝 selenium => pip install selenium

# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

# 設定Chrome Driver(或其他瀏覽器)執行擋路徑
# 須注意Driver版本需跟本機瀏覽器版本相符
options = Options()
# 不自動關閉瀏覽器
# options.add_experimental_option("detach", True)
options.chrome_executable_path = "..\chromedriver-win64\chromedriver.exe"

# 建立Driver實體物件，進行瀏覽器操作
driver = webdriver.Chrome(options=options)

# 視窗最大化
# driver.maximize_window()

# 開啟網頁 => 財報狗
driver.get("https://statementdog.com/users/sign_in")

# 輸入帳密並登入站台
userEmail = driver.find_element(By.ID, "user_email")
userEmail.send_keys("........@.........com")
userPa55Word = driver.find_element(By.ID, "user_password")
userPa55Word.send_keys("meme")
submitBtn = driver.find_element(By.CLASS_NAME, "submit-btn")
submitBtn.send_keys(Keys.ENTER)

# 切換至追蹤股組合頁簽
driver.get("https://statementdog.com/portfolios")

# 等待欄位資料載入完成
import time
time.sleep(3)

# 取得追蹤清單資訊
stockItems = driver.find_elements(By.CSS_SELECTOR, 'ul.portfolio-stock-item')
for item in stockItems:
    # print(item.get_attribute('outerHTML'))
    print(item.text.replace("刪除", '').replace("..", '').split())

# 取得網頁原始碼
# print(driver.page_source) 
# 取得一個網頁元素
# driver.find_element() 
# 取得多個網頁元素
# driver.find_elements() 
#在瀏覽器執行JS程式
# driver.execute_script("JavaScript Code") 
#將視窗捲到底部
# driver.execute_script("windows.scrollTo(0, document.body.scrollHeight);") 

# 需引用selenium.webdriver.common.by才可使用該類別
# driver.find_elements(By.ID, "ID") #透過ID取得
# driver.find_elements(By.CSS_SELECTOR, "[data-xxx=xxx]]") #任意屬性
# driver.find_elements(By.CLASS_NAME, "class") #透過CLASS取得

# 關閉當前網頁
# driver.close()

# 關閉所有網頁
driver.quit()