from selenium import webdriver  # webdriver for browser interaction
from selenium.webdriver.common.by import By  # by (type)
from selenium.webdriver.support.ui import WebDriverWait, Select  # wait module
from selenium.webdriver.support import expected_conditions as EC  # used with wait for condition
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def __init__():
    # initializations
    driver_path = '/Users/Billy/Applications/chromedriver'  # chromedriver path
    profile_path = 'user-data-dir=/Users/Billy/Desktop/chromefile'  # chrome user profile path
    option = webdriver.ChromeOptions()  # initialize option
    option.add_argument(profile_path)  # option with profile path
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)  # start up chrome browser
    waitinput = WebDriverWait(browser, 100)  # default wait time of "browser" to 100
    wait = WebDriverWait(browser, 5)


# FUNCTION DEFINITIONS

# go to link
def goto(link):
    browser.get(link)


# get size for item
def getSize(size='Medium'):
    try:
        wait.until(EC.presence_of_element_located((By.NAME, 's')))
        Select(browser.find_element_by_name('s')).select_by_visible_text(size)
    except:
        pass


# click add to cart
def addToCart():
    wait.until(EC.presence_of_element_located((By.ID, 'add-remove-buttons')))
    browser.find_element_by_name('commit').click()
    waitinput.until(EC.presence_of_element_located((By.CLASS_NAME, 'has-cart')))


# click checkout
def checkout():
    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'checkout')))
    browser.find_element_by_partial_link_text('checkout').click()


# wait for user to click item
def waitForInput():
    waitinput.until(EC.presence_of_element_located((By.ID, 'img-main')))


def run():
    # BEGIN
    # EDIT HERE AND USE FUNCTiONS FOR THE BOT
    goto('http://www.supremenewyork.com/shop/all/accessories')

    # refresh until item is found
    while True:
        try:
            browser.find_element_by_partial_link_text('Arabic')
        except NoSuchElementException:
            print('looking...')
            browser.implicitly_wait(2)
            browser.refresh()
        else:
            break

    waitForInput()
    addToCart()
    goto('http://www.supremenewyork.com/shop/all/accessories')
    waitForInput()
    addToCart()
    checkout()


run()
