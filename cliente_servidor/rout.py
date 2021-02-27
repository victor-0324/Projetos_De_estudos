#usr/bin/python3.8
from selenium import webdriver
from time import sleep
from datetime import date, datetime
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import keyboard


username = 'mariavitoria'
password = 'mariavitoria'
Url_rout = 'http://10.0.0.1/login.html'
novo = 'Acesso Negado !! '

class Roteador:
    def __init__(self,username ,password, Url_rout, ):
        self.username = username
        self.password = password 
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #webdriver.Firefox() to use Firefox
        self.driver.set_window_size(600, 1080)
        self.driver.set_window_position(300, 50)
        self.driver.get(Url_rout)
        sleep(2)

        passwd = self.driver.find_element_by_xpath("//input[contains(@type,'password')]")
        passwd.send_keys(password)
        botao = self.driver.find_element_by_xpath("//button[contains(@class,'btn btn-primary btn-lg btn-block')]")
        botao.click()
        sleep(3)

        botao1 = self.driver.find_element_by_xpath("//button[contains(@class,'navbar-toggle collapsed')]")
        botao1.click()
        sleep(3)

        botao2 = self.driver.find_element_by_xpath("//span[contains(@class,'menu icon-wireless')]")
        botao2.click()
        sleep(3)

        botao3 = self.driver.find_element_by_xpath("//input[contains(@name,'wifiSSID')]") 
        botao3.click()

        botao5 = self.driver.find_element_by_xpath("//input[contains(@name,'wifiSSID')]") 
        botao5.clear()
        sleep(3)

        botao4 = self.driver.find_element_by_xpath("//input[contains(@name,'wifiSSID')]") 
        botao4.send_keys(novo)
        sleep(2)

        salve = self.driver.find_element_by_xpath("//button[contains(@class,'btn btn-frist btn-primary')]")
        salve.click()
        keyboard.press_and_release('shift + Enter')
        sleep(5)
        
        #keyboard.press_and_release('mariavitoria123')  
    
        
today = date.today()
now = datetime.now()

try:
    rotbot = Roteador(username, password, Url_rout)
    print(f"[{date.today().strftime('%Y-%m-%d')} {datetime.now().strftime('%H:%M:%S')}] [{username}] Closing window...")
    rotbot.driver.close()
except:
    print("Fail")

