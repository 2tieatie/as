from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as un
from selenium.common.exceptions import StaleElementReferenceException


class Bot:

    def __init__(self):
        chrome_options = un.ChromeOptions()
        chrome_options.add_argument('--enable-javascript')
        self.driver = un.Chrome(executable_path='/chromedriver')
        time.sleep(2)
        self.DEBUG = True
        self.cities = []
        self.profiles = []

    def get_cities(self):
        self.driver.get('https://adultsearch.com/')
        view_more_but = self.driver.find_elements(By.XPATH, "//a[contains(text(), 'View More...')]")
        for but in view_more_but:
            self.driver.execute_script("arguments[0].click();", but)

        cities = self.driver.find_elements(By.XPATH, '//*[@class="color-tertiary text-decoration-none lh-25"]')
        if self.DEBUG:
            for city in cities:
                try:
                    self.cities.append(city.get_attribute("href"))
                except StaleElementReferenceException:
                    continue
        if self.DEBUG:
            for c in self.cities:
                print(c)

    def get_profiles(self, url: str):
        page = 0

        while True:
            page += 1
            self.driver.get(f'{url}female-escorts/?ipp=90&page={page}')
            profiles = self.driver.find_elements(By.XPATH, "//*[@class='card-view d-flex text-decoration-none color-tertiary' and not(contains(@href, 'ad?go='))]")
            if len(profiles) != 0:
                for profile in profiles:
                    self.profiles.append(profile.get_attribute("href"))
            else:
                break

        if self.DEBUG:
            for profile in self.profiles:
                print("Profile link:", profile)


b = Bot()

# b.get_cities()

b.get_profiles('https://adultsearch.com/us/california/los-angeles/')
