import os
import time
from selenium import webdriver
from types import TracebackType
import bookings.constants as const
from bookings.booking_filtration import BookingFlitration
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"E:/Projects/Web Scraping/",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(10) #Max timeout
        self.maximize_window()
    
    # It is defined within classes that are meant to be used as context managers.
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(10)
        
    def currency_selector(self):
        currency_element=self.find_element(By.CSS_SELECTOR,'button[aria-label="Prices in Indian Rupee"]')
        currency_element.click()
        choose_currency=self.find_element(By.XPATH,'//*[@id="header_currency_picker"]/div/div/div[2]/div/div[3]/div/div/div/ul[1]/li[1]')
        choose_currency.click()
        
    def select_destination(self,place_to_go):
        search_field=self.find_element(By.ID,':rh:')
        search_field.send_keys(Keys.ESCAPE)
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result=self.find_element(By.CSS_SELECTOR,'li[id="autocomplete-result-0"]')
        first_result.click()
    
    def checkin_checkout(self,checkin_date,checkout_date):
        checkin_ele=self.find_element(By.CSS_SELECTOR,f'span[data-date="{checkin_date}"]')
        checkin_ele.click()
        checkout_ele=self.find_element(By.CSS_SELECTOR,f'span[data-date="{checkout_date}"]')
        checkout_ele.click()
    
    def no_guest(self,no_of_adults):
        occupancy_ele=self.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div/div[3]/div/button')
        occupancy_ele.click()
        while(True):
            occupancy_ele=self.find_element(By.XPATH,'//*[@id=":ri:"]/div/div[1]/div[2]/button[1]')
            occupancy_ele.click()
            min_adults_ele=self.find_element(By.ID,'group_adults')
            adults_value=min_adults_ele.get_attribute('value')
            if(int(adults_value)==1):
                break
        curr_adults=self.find_element(By.ID,'group_adults')
        curr_adults_value=curr_adults.get_attribute('value')
        while(int(curr_adults_value)!=no_of_adults):
            guest_selection=self.find_element(By.XPATH,'//*[@id=":ri:"]/div/div[1]/div[2]/button[2]')
            guest_selection.click()
            curr_adults=self.find_element(By.ID,'group_adults')
            curr_adults_value=curr_adults.get_attribute('value')
    
    def click_search(self):
        search_button=self.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div/div[4]')
        search_button.click()
    
    def apply_filtration(self):
        filtration=BookingFlitration(driver=self)
        