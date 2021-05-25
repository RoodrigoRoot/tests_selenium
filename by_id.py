from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install()) #Definivimos el Navegador y descargamos el Driver
driver.get("http://www.python.org") #Deifinimos la URL a visitar

element = driver.find_element_by_id("id-search-field") # Aquí localizamos el elementos por ID
element.send_keys("Documentation") #Enviamos texto al elemento localizado.
element.send_keys(Keys.RETURN)

#driver.close()