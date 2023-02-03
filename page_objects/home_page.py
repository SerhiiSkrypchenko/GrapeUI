from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase

dev_url = "https://lunaonedev.firstbridge.io"
stage_url = ""
prod_url = ""


class HomePage(BaseCase):
    open_menu_btn_route = "//body/div[@id='root']/div[1]/div[1]/button[1]/span[1]"
    wallet_menu_btn_route = "//body/div[2]/div[1]/div[2]/div[2]/button[1]/span[1]"
    make_transfer_text = "//h2[contains(text(),'Make Transfer')]"

    def verify_home_page(self, driver):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomePage.make_transfer_text))
            )
            self.assertTrue("Make Transfer" in driver.page_source)
            self.assertTrue("Wallet ID" in driver.page_source)
            self.assertTrue("Available balance" in driver.page_source)
            self.assertTrue("Transaction History" in driver.page_source)
        except:
            capture_path = 'D:/Work/Screenshots from tests/Make transfer money is not present.png'
            driver.save_screenshot(capture_path)
            print("ERROR => Make transfer money is not present !!! See screenshot")