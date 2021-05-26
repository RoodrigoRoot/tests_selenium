from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
import os


class WhatsappMessages:

    @staticmethod
    def send_message(user, message):

        element_xpath = "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
        url = "https://web.whatsapp.com/send?phone=+52{}"


        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")

        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir={}".format(profile))

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        try:
            driver.get(url.format(user.phone))
            time.sleep(15)
            element = driver.find_element_by_xpath(element_xpath)

            if element.is_enabled():
                element.send_keys(message)
                element.send_keys(Keys.RETURN)
                driver.close()
                print("Mensaje enviado")

        except Exception as e:
            print(e)
            driver.close()