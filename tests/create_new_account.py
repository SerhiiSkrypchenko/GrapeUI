from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuration
from pages import main_page

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(configuration.url)
assert "Luna 1" in driver.title
open_menu_btn = driver.find_element(By.XPATH, main_page.open_menu_btn)
open_menu_btn.click()

wallet_btn = driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[2]/div[2]/button[1]/span[1]")
wallet_btn.click()
create_wallet_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Create Wallet')]")
restore_wallet_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Restore Wallet')]")
create_wallet_btn.click()
new_password_field = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
confirm_password_field = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")
new_password_field.clear()
confirm_password_field.clear()
new_password_field.send_keys("12345678")
confirm_password_field.send_keys("12345678")
create_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Create')]")
create_btn.click()
text = driver.find_element(By.XPATH, "//div[contains(text(),'Secret Recovery Phrase')]")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]"))
    )
except:
    capture_path = 'D:/Work/Screenshots from tests/Text not present.png'
    driver.save_screenshot(capture_path)
    print("ERROR => Element of recovery Phrase wasn't found on page !!! See screenshot")


recovery_phrase = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]")

print(recovery_phrase.get_attribute("text"))

#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#test git
driver.close()
