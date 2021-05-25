from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os


class WhatsAppMessages:
        

    
    @classmethod
    def send_message(cls, user, message):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir={}".format(profile))
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        url = "https://web.whatsapp.com/send?phone={}"

        try:
            driver.get(url.format(user.phone))
            time.sleep(20)
            elem = driver.find_element_by_css_selector("div._2x4bz div._2_1wd")
            if elem.is_enabled():
                elem.send_keys(message)
                time.sleep(10)
                elem.send_keys(Keys.RETURN)
                driver.close()
                print("Mensaje enviado")
                return True

        except Exception as e:
            print(e)
            print("Mensaje no enviado")
            driver.close()
            return False