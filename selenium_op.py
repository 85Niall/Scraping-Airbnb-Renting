from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait


class SeleniumOP:
	def __init__(self):
		self.chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
		self.options = webdriver.ChromeOptions()
		self.options.add_experimental_option('detach', True)
		self.service = Service(self.chrome_driver_path)
		self.driver = webdriver.Chrome(service=self.service, options=self.options)
		self.driver.implicitly_wait(5)
		# self.current_page = self.driver.find_element(By.XPATH, '/html/body')

	def click_next_page(self, page):
		self.driver.get(page)
		try:
			# True: a[class='l1j9v1wn c1ytbx3a dir dir-ltr']
			button_next_pg = self.driver.find_element(By.CSS_SELECTOR, "a[class='l1j9v1wn c1ytbx3a dir dir-ltr']")
			button_next_pg.click()
			return True
		except ec.NoSuchElementException:
			# False: button[class='l1j9v1wn c1ytbx3a dir dir-ltr']
			return False

	def add_from(self, google_forms, ad_name, ad_title, price, link):
		self.driver.get(google_forms)
		try:
			input_ad_name = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i1']")
			input_ad_name.send_keys(str(ad_name))
			input_ad_title = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i5']")
			input_ad_title.send_keys(str(ad_title))
			input_price = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i9']")
			input_price.send_keys(str(price))
			input_link = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i13']")
			input_link.send_keys(str(link))
			button_submit = self.driver.find_element(By.CSS_SELECTOR, "span[class='NPEfkd RveJvd snByac']")
			button_submit.click()
			return True
		except ec.NoSuchElementException:
			return False
		except ec.WebDriverException:
			print('ChromeDriver only supports characters in the BMP')
			print(ad_name)
			print(ad_title)
			print(price)
			print(link)
			return False
