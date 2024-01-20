# Import the Selenium WebDriver module for browser automation.
from selenium import webdriver
# Import the 'By' class from Selenium to specify the mechanism used to locate elements.
from selenium.webdriver.common.by import By
# Import the 'WebDriverWait' class from Selenium for waiting until certain conditions are met before moving on.
from selenium.webdriver.support.ui import WebDriverWait
# Import the 'expected_conditions' module from Selenium to define the expected conditions for waiting.
from selenium.webdriver.support import expected_conditions as EC

# URL of the webpage I am scraping.
url = 'https://skims.com/products/mens-lounge-sock-army'
# Path to the ChromeDriver executable on my computer.
chrome_driver_path = '/Users/kadenhuber/Documents/Coding/chromedriver-mac-arm64/chromedriver'

# Configure Chrome options for the WebDriver and  include the path to the ChromeDriver executable on my computer.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

# Create a new instance of the Chrome WebDriver with the configured options set above.
driver = webdriver.Chrome(options=chrome_options)
# Set the  wait time to 10 seconds, allowing WebDriver to wait for elements before throwing an exception.
driver.implicitly_wait(10)

# Take the WebDriver to the specified URL.
driver.get(url)

# WebDriverWait to wait for the presence and visibility of the 'body' element.
# Make sure that the page has loaded completely before proceeding.
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

try:
    # Check if the "Join the Waitlist" button element exists on the page using its class name.
    waitlist_button_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn')))

    # If the button exists, print a message indicating its presence.
    print("NOOO! The socks are still on the waitlist.")

except Exception as e:
    # If the button does not exist, print a message indicating its absence.
    print(f"LETS GOOO! The socks are no longer on the waitlist.")

finally:
    # Close the browser, making sure  it is closed regardless of success(try) or failure(fail).
    driver.quit()

