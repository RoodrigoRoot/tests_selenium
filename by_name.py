from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install()) #Definivimos el Navegador y descargamos el Driver
url = "http://127.0.0.1:5500/html/index.html"
driver.get(url) #Deifinimos la URL a visitar

#element = driver.find_element_by_name("username")

#if element.is_enabled():
#    element.send_keys("Nombre usuario")

#else:
#    print("El elemento esta deshabilitado")


elements = driver.find_elements_by_name("email")
for element in elements:
    if element.is_enabled():
        element.send_keys("rod@azulschool.net")
    