from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import base64
import re

class DoScrape:

    def __init__(self) -> None:
        pass

    def fakecaptcha_interaction(self, numbers, iteration):
        
        def makeDownload(URL, filename):
            def decode_base64(data, altchars=b'+/'):
                data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)
                missing_padding = len(data) % 4
                if missing_padding:
                    data += b'='* (4 - missing_padding)
                return base64.b64decode(data, altchars)
            fileString = URL[22:-1]
            print(fileString)
            local_file = filename
            arr = bytes(fileString, encoding='utf8')
            with open(local_file, 'wb')  as file:
                file.write(decode_base64(arr))
    

        print("hey")
        url = 'https://fakecaptcha.com/'
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options)
        browser.get(url)
        browser.implicitly_wait(3)
        search_field = browser.find_element_by_css_selector("input[name='words'][type='text']")
        search_field.send_keys(numbers)
        search_field.submit()
        browser.implicitly_wait(10)
        WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div/div[2]/a'))).click()
        img = search_field = browser.find_element_by_css_selector("img[id='words']")
        link = img.get_attribute('src')
        makeDownload(link, "/home/jovyan/my_notebooks/" + str(numbers)+"("+str(iteration)+").jpg")
        browser.close()
        browser.quit()


   
