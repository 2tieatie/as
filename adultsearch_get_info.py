from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as un
from selenium.common.exceptions import NoSuchElementException


class GetInfo:

    def __init__(self):
        chrome_options = un.ChromeOptions()
        chrome_options.add_argument('--enable-javascript')
        self.driver = un.Chrome(executable_path='/chromedriver')
        time.sleep(2)
        self.DEBUG = True

    def get_info(self, url: str):

        self.driver.get(url)

        self.name = None

        try:
            self.name = self.driver.find_element(By.XPATH, '//div[@class="details__card-header"]').text.replace('About', '').strip()

        except NoSuchElementException:
            self.name = None

        self.country = None
        self.city = None

        try:
            c_c = self.driver.find_element(By.XPATH, "//*[@class='details__heading-item details__heading-item_location']/span").text.strip().split(', ')
            self.country = c_c[1]
            self.city = c_c[0]
        except NoSuchElementException:
            self.country = None
            self.city = None

        self.phone = None

        try:
            self.phone = self.driver.find_element(By.XPATH, "//*[@class='details__heading-item details__heading-item_phone']/a").text.strip()

        except NoSuchElementException:
            self.phone = None

        self.email = None

        if self.DEBUG:
            print('Name:', self.name)
            print('Country:', self.country)
            print('City:', self.city)
            print('Phone:', self.phone)
            print('Email:', self.email)

gi = GetInfo()

gi.get_info('https://adultsearch.com/us/california/los-angeles/female-escorts/3064788')