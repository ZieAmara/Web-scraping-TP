from selenium import webdriver

# Start the session
driver = webdriver.Chrome()

# Take action on browser
driver.get("http://selenium.dev")

# Close the session
driver.quit()
