from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")    ###### See Note Below

driver.get("https://www.python.org/")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")

elem.clear()

elem.send_keys("pycon")

elem.send_keys(Keys.RETURN)

assert "No results found"  not in driver.page_source

driver.quit()    ##### this will close the browser