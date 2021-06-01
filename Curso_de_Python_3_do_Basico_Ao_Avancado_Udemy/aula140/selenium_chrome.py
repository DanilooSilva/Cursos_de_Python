from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.__url = ''
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__driver.maximize_window()
        #self.__driver.get(self.__url)

    def sair(self):
        self.__driver.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    sleep(3)
    chrome.sair()