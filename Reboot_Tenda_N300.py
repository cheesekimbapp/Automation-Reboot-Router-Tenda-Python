from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Tenda N300 router's web interface
driver.get("IP/URL ROUTER")

# Wait for the page to load, then find the password field
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-password"))
)

# Enter the default password
password.send_keys("PASSWORD-ROUTER")

# Find the login button and click it
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "save"))
)
login_button.click()

# Wait for the page to load, then find the Administration link by its ID and click it
admin_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "system"))
)
driver.execute_script("arguments[0].click();", admin_link)

# Wait for the page to load, then find the Reboot button by its ID and click it
reboot_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "reboot"))
)
driver.execute_script("arguments[0].click();", reboot_button)

# Handle the confirmation alert
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
except NoAlertPresentException:
    print("No alert present")

# Close the browser
driver.quit()
