from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

Link = "https://www.jbhifi.com.au/products/pokemon-tcg-lost-origin-booster-card-games?queryID=0241a083063ea39d0ebb88b9dda4ea90&objectID=596511"
Coupon = "92OFOLKY15OUNP"
Email = "lohjiajhin@gmail.com"
N = 3   # Number of browsers to spawns

def browser_function():
    driver_path = "D:\Python\WebDrivers\chromedriver.exe"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get(Link)
    chr_driver.find_element_by_class_name("pdp-jss-desktopCallToAction-15").click()
    time.sleep(1.5)
    chr_driver.find_element_by_id("minicart-toggle").click()
    time.sleep(1)
    chr_driver.find_element_by_class_name("collect-checkout").click()
    time.sleep(1)
    chr_driver.find_element_by_id('checkout_couponcode').send_keys(Coupon)
    time.sleep(1)
    chr_driver.find_element_by_class_name('field__input-btn').click()
    time.sleep(2)
    chr_driver.get("https://www.jbhifi.com.au/checkout")
    time.sleep(1)
    chr_driver.find_element_by_id('checkout_email').send_keys(Email)

for i in range(N):
    browser_function()
