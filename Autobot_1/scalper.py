import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import info
# For using chrome
browser = webdriver.Chrome('/Users/henryike/Documents/chromedriver')

# For using firefox
browser = webdriver.Firefox(executable_path='/Users/henryike/Documents/scalperbot_1/geckodriver')

# Bestbuy RTX 3090 page
browser.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434')

# Tester link
#browser.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-nvlink-bridge-for-3090-cards-space-gray/6441554.p?skuId=6441554')


buyButton = False

while not buyButton:

    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Button not ready yet")

        time.sleep(1)
        browser.refresh()

    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print("Button was clicked")
        addToCartBtn.click()

        addToCartBtn = addButton = browser.find_element_by_link_text("Cart")

        print("Button was clicked")
        addToCartBtn.click()

        chkout1 = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
                )

        print("Button was clicked")
        chkout1.click()

        # Fill in email and password
        emailEntry = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )

        emailEntry.send_keys(info.email)

        pswdEntry = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )

        pswdEntry.send_keys(info.password)

        # Click sign in button
        persInfo = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button"))
        )

        print("Button was clicked")
        persInfo.click()

        # Enter security code
        secEntry = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )

        secEntry.send_keys(info.cvv)

        # Click the purchase button
        purchButt = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button")
        browser.execute_script("arguments[0].click();", purchButt)

        print("Button was clicked")
        #purchButt.click()

        buyButton = True