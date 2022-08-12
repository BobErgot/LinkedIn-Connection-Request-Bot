import pandas
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from time import sleep


def check_exists_by_xpath(browser,xpath):
	try:
		browser.find_element(By.XPATH,xpath)
	except NoSuchElementException:
		return False
	return True


def check_exists(element,browser,sel):
	try:
		browser.find_element(element,sel)
	except NoSuchElementException:
		return False
	return True


def login(browser):
	url = "https://www.linkedin.com/"
	browser.get(url)
	username = browser.find_element(By.ID,"session_key") # Getting the login element
	username.send_keys("<Enter email id>") # Sending the keys for username
	password = browser.find_element(By.ID,"session_password") # Getting the password element
	password.send_keys("<Enter password") # Sending the keys for password
	browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click() # Getting the tag for submit button


def connection_request(browser, profile_url_list):
	for profile_url in profile_url_list:
		print(profile_url)
		if not profile_url or profile_url == '' or pandas.isnull(profile_url):
			print("Empty String\n")
			continue
		try:
			browser.get(profile_url)
		except InvalidArgumentException:
			print("Bad profile URL\n")
			continue
		sleep(10)
		xpath="//main[@id='main']/section[1]/div[2]/div[3]/div[1]/button[1]/span[contains(.,'Connect')]"
		connect_xpath="//main[@id='main']/section[1]/div[2]/div[3]/div[1]/button[1]"
		more_xpath="//main[@id='main']/section[1]/div[2]/div[3]/div[1]//button[contains(@aria-label, 'More actions')]"
		more_connect_xpath="//main[@id='main']/section[1]/div[2]/div[3]/div[1]//button[contains(@aria-label, 'More actions')]/parent::node()/div/div/ul//div/span[text()='Connect']"
		if check_exists_by_xpath(browser,xpath):
			browser.find_element(By.XPATH,connect_xpath).click()
			check_popup(browser)
			print("Connected\n")
		elif check_exists_by_xpath(browser, more_xpath):
			browser.find_element(By.XPATH,more_xpath).click()
			if check_exists_by_xpath(browser, more_connect_xpath):
				browser.find_element(By.XPATH,more_connect_xpath).click()
				check_popup(browser)
				print("Connected\n")
			else:
				print("No connection option under More button\n")
		else:
			print("No connection option under profile action flex\n")


def check_popup(browser):
	if check_exists(By.CSS_SELECTOR,browser,'[aria-label="Send now"]'):
		browser.find_element(By.CSS_SELECTOR,'[aria-label="Send now"]').click()
	elif check_exists(By.CSS_SELECTOR,browser,'[aria-label="Other"]'):
		browser.find_element(By.CSS_SELECTOR,'[aria-label="Other"]').click()
		browser.find_element(By.CSS_SELECTOR,'[aria-label="Connect"]').click()
		check_popup(browser)
	elif check_exists(By.CSS_SELECTOR,browser,'[aria-label="Connect"]'):
		browser.find_element(By.CSS_SELECTOR,'[aria-label="Connect"]').click()
		check_popup(browser)
	return


def main():
	# get profile url list from excel
	linkedin_database = pandas.read_csv("linkedin_database.csv")
	profile_url_list = list(linkedin_database.iloc[0:, 2])

	# connect python with webbrowser-firefox
	service = Service('geckodriver-v0.31.0-win64\\geckodriver.exe') # path to browser web driver
	browser = webdriver.Firefox(service=service)
	login(browser)
	connection_request(browser, profile_url_list)
	browser.quit()


# Driver's code
if __name__ == '__main__':
	main()