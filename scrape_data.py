from selenium import webdriver 
import requests 
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException




class CarData:
    def __init__(self):
        self.path = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(self.path)
        self.driver.get('https://app.platerecognizer.com/view/467135406-c23560e1cb/?minimal&region=')


    def scrape_licence_number_plate(self):
        licence_plate_number = self.driver.find_element(By.CLASS_NAME,'item-data').text
        print(licence_plate_number)
        time.sleep(5)

        return licence_plate_number

    def upload_image(self, url, image_path):
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print("Image uploaded successfully.")
            else:
                print("Error uploading image. Status code:", response.status_code)

       
        

# car = CarData()
# website_url = "https://imgbb.com/upload"  
# image_filepath = r"C:\Users\CODED\Desktop\cardata\image\room-5.jpg"  

# car.upload_image(website_url, image_filepath)
