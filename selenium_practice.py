from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

driver.get('https://main--gilded-kulfi-04b536.netlify.app/')

driver.implicitly_wait(0.5)

title = driver.title

# slow so that i can see what is happening
time.sleep(2)


# Find the dropdown element by its ID
dropdown = Select(driver.find_element(By.ID, "dropdown"))

# Select an option by its visible text
dropdown.select_by_visible_text("Option 2")

time.sleep(2)


# Get the selected option
selected_option = dropdown.first_selected_option
assert selected_option.text == "Option 2"

driver.quit()
