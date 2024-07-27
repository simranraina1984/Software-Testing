from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Navigate to Flipkart home page
driver.get("https://www.flipkart.com/")

# Wait for the search input field to be available
search_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))
)

# Enter the search query "chess"
search_input.send_keys("चेस")

# Click the search button
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

# Wait for the search results page to load
search_results = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='_1HmYoV _35HD7C']"))
)

# Print the number of search results
print(f"Found {len(search_results)} search results for 'chess'")

# Close the browser
driver.quit()