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

# Create a WebDriverWait instance to wait up to 30 seconds for the presence of the 'body' element. 
# Make sure that the page has loaded completely before proceeding.
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

try:
    # Check if the <h1> element exists on the page.
    sock_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/main/div/section[2]/div[1]/div[3]/div/div[1]/header/div/h1')))
    
    # Get the text content of the <h1> element.
    sock_name = sock_name_element.text

    # Print the name of the socks.
    print("Name of the socks:", sock_name)

except Exception as e:
    # Handle any exceptions that might occur during the above operations.
    print(f"Error: {e}")

finally:
    # Close the browser, making sure  it is closed regardless of success(try) or failure(fail).
    driver.quit()

