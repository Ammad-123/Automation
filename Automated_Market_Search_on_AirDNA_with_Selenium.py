from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the URL of AirDNA.co
url = "https://www.airdna.co/"

# Specify the markets you want to search
markets =  ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
 # Add more markets as needed

# Initialize Chrome WebDriver
driver = webdriver.Firefox()

# Open AirDNA.co
driver.get(url)

# Wait for the page to load
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button.css-q9ts5p[type='button']")


# Click the button
button.click()

# # Find the search input field and enter each market
# search_input = driver.find_element(By.ID, "search-bar-input")
search_input = driver.find_element(By.CSS_SELECTOR, ".css-1w481i8")

for market in markets:
    # Clear the search input field
    search_input.clear()
    
    # Enter the market
    search_input.send_keys(market)
    
    # Press Enter to perform the search
    search_input.send_keys(Keys.RETURN)
    
    # Wait for the search results to load
    time.sleep(3)  # Adjust as needed
    
    # You can add further actions here, such as scraping the data from the search results

# Close the browser window
driver.quit()
