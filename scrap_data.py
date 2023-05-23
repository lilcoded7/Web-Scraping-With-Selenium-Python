from selenium import webdriver 
import requests 
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time 





def upload_image(image_path):
    path = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://app.platerecognizer.com/view/467135406-c23560e1cb/?minimal&region=')

    upload_image = driver.find_element(By.CLASS_NAME, 'btn btn-secondary width-full')
    upload_image.send_keys(image_path)
    upload_image.click()
    print('============================')

    time.sleep(5)


image_path = 'image/room-5.jpg'
upload_image(image_path)

def scrape_licence_number_plate():
    path = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://app.platerecognizer.com/view/467135406-c23560e1cb/?minimal&region=')

    licence_plate_number = driver.find_element(By.CLASS_NAME,'item-data').text
    print(licence_plate_number)

    return licence_plate_number

    time.sleep(5)






