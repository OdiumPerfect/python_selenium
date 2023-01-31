from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        # print(len(star_child_elements))
        # print(star_child_elements)
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value}':
                    star_element.click()


    def sort_by_price_low_first(self):
        sort_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        sort_button.click()
        sort_button_price = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        sort_button_price.click()