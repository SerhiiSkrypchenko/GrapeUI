from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dev_url = "https://lunaonedev.firstbridge.io"
stage_url = ""
prod_url = ""


#buttons
open_menu_btn = "//body/div[@id='root']/div[1]/div[1]/button[1]/span[1]"