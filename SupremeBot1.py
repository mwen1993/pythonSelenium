from selenium import webdriver #webdriver for browser interaction
from selenium.webdriver.common.by import By #by (type) 
from selenium.webdriver.support.ui import WebDriverWait, Select #wait module
from selenium.webdriver.support import expected_conditions as EC #used with wait for condition
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options 



#initializations
driver_path = '/Users/Billy/Applications/chromedriver'
profile_path = 'user-data-dir=/Users/Billy/Desktop/chromefile'
#profile_path = 'user-data-dir=/Users/Billy/Library/Application Support/Google/Chrome/'
option = webdriver.ChromeOptions()
option.add_argument(profile_path)
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option) #start up chrome browser
wait = WebDriverWait(browser, 5) #default wait time of "browser", 5 sec

#go to link
def goto(link):
	browser.get(link)
	
#for single item with no color variation(e.x. chopsticks, sake)
def getItemNoColor(name):
	wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name)))
	browser.find_element_by_partial_link_text(name).click()

#for single item with color variation(e.x. box logo hoodie, black)
def getItemWithColor(name, colors=[]):
	
	#(method2)
	#click on first element that matches item description
	#then search for color within next page
	#this method search element by xpath, effecient but wont work if xpath is changed
	wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name)))
	browser.find_element_by_partial_link_text(name).click()#go to product
	wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-style-name]")))#wait for page to load
	colorlist = browser.find_elements_by_xpath("//a[@data-style-name]")
	for color in colorlist:
		if any(word in color.get_attribute('data-style-name') for word in colors):
			color.click()
			break
	

	#goes through items on the page and gets correct items, then from those items get the matching color
	'''
	wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name)))
	products = browser.find_elements_by_class_name('inner-article')
	narrowlist = []#empty list used for narrowed product

	#narrow down search result to desire item
	for product in products:
		if name in product.text:
			narrowlist.append(product)

	#select desire color, then click on that product
	for item in narrowlist:
		if any(color in item.text for color in colors):
		 	item.click()
		 	break
	'''

def getItemWithColorMain(name, colors=[]):
	wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name)))
	products = browser.find_elements_by_class_name('inner-article')
	narrowlist = []#empty list used for narrowed product

	#if products list returns empty
	if not products:
		raise Exception('no such element') 

	#narrow down search result to desire item
	for product in products:
		if name in product.text:
			narrowlist.append(product)

	#select desire color, then click on that product
	for item in narrowlist:
		if any(color in item.text for color in colors):
		 	item.click()
		 	break

#get size for item
def getSize(size='Medium'):
	try:
		wait.until(EC.presence_of_element_located((By.NAME, 's')))
		Select(browser.find_element_by_name('s')).select_by_visible_text(size)
	except:
		pass

#click add to cart
def addToCart():
	wait.until(EC.presence_of_element_located((By.ID, 'add-remove-buttons')))
	browser.find_element_by_name('commit').click()

#click checkout
def checkout():
	wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'checkout')))
	browser.find_element_by_partial_link_text('checkout').click()

#BEGIN
#EDIT HERE AND USE FUNCTiONS FOR THE BOT
goto('http://www.supremenewyork.com/shop/all/sweatshirts')

#refresh until item is found
while True:
	try:
		browser.find_element_by_partial_link_text('Stone')
	except NoSuchElementException:
		print('looking...')
		browser.implicitly_wait(1.5)
		browser.refresh()
	else:
		break
try:
	getItemWithColorMain('Stone', ['Black'])
except:
		try:
			getItemWithColor('Stone', ['Black'])
		except:
			pass


getSize('Medium')
addToCart()
checkout()