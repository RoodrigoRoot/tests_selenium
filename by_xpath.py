from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install()) #Definivimos el Navegador y descargamos el Driver
url = "http://127.0.0.1:5500/html/index.html"
driver.get(url) #Deifinimos la URL a visitar


element = driver.find_element_by_xpath("//*[@id='user_form']/input[3]")

print(element.get_attribute("name"))