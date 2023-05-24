from selenium import webdriver 
import requests 
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time 




class CarData:
    def __init__(self):
        self.path = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Edge(self.path)
        self.driver.get('https://app.platerecognizer.com/view/467135406-c23560e1cb/?minimal&region=')


    def scrape_licence_number_plate(self):
        licence_plate_number = self.driver.find_element(By.CLASS_NAME,'item-data').text
        print(licence_plate_number)
        time.sleep(5)

        return licence_plate_number

    def upload_image(self):
        self.driver.switch_to_frame(0)
        image = self.driver.find_element(By.ID, 'file')
        print(image)
        print('================================')
        

        

car = CarData()
car.upload_image()
