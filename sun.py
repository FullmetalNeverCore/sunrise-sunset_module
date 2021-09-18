from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from pyvirtualdisplay import Display
import pickle 
import colorama,random
import datetime 
from datetime import date
from colorama import Back,Fore,Style
import time
import psutil,subprocess
import os,sys,string


class SunData:
    def __init__(self):
                user_city = str(input('Название города: ')).lower()
                self.opts = Options()
                #self.display = Display(visible=0, size=(800, 600))
                # self.display.start()
                self.opts.add_argument("--disable-extensions")
                self.opts.add_argument("--proxy-server='direct://'")
                self.opts.add_argument("--proxy-bypass-list=*")
                self.opts.add_argument("--start-maximized")
                self.opts.add_argument('--headless')
                self.opts.add_argument('--disable-gpu')
                self.opts.add_argument('--disable-dev-shm-usage')
                self.opts.add_argument('--no-sandbox')
                self.opts.add_argument('--ignore-certificate-errors') 
                self.driver = webdriver.Chrome(options=self.opts)
                if not ' '.join(user_city).split() in ' '.join(string.ascii_lowercase).split():
                    self.url = "https://voshod-solnca.ru/sun/"+str(user_city)
                else:
                    print('Err - write city in latin alphabet'),os.execv(sys.argv[0], sys.argv)
    def main(self):
            self.driver.get(self.url)
            def sunset():
                time.sleep(4)
                ss = self.driver.find_element_by_id('sunset').get_attribute('value')
                return ss 
            def sunrise():
                time.sleep(4)
                sr = self.driver.find_element_by_id('sunrise').get_attribute('value')
                return sr
            print(sunset()),print(sunrise())
            self.driver.close()


SunData().main()
