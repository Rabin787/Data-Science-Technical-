from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
 
# Settings 
URL      = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"
  
# Set up the browser 
def create_browser():   
    options = Options()
    options.headless = False         
    options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(options=options)
    return driver
 
# Login 
def login(driver):    
    print("Opening browser...")
    driver.get(URL)
    time.sleep(1)  # wait 1 second so the page fully loads 
    print(" Typing username and password...")
 
    # Find the username box and type into it
    # By.ID means we're finding the element by its id="username" in the HTML
    username_box = driver.find_element(By.ID, "username")
    username_box.clear()                # clear any existing text
    username_box.send_keys(USERNAME)    # type the username
 
    # Find the password box and type into it
    password_box = driver.find_element(By.ID, "password")
    password_box.clear()
    password_box.send_keys(PASSWORD)
 
    print("Clicking login button...")
 
    # Find and click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
 
    time.sleep(1)
 
    # Check if login worked 
    # After login, the page shows a green success message if it worked
    try:
        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        print(f"Login successful! Message: {success_message.text.strip()}")
        return True
    except:
        # If no success message, check for error message
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
            print(f"Login failed! Reason: {error_message.text.strip()}")
        except:
            print("Login failed for unknown reason.")
        return False 
 
# Extract data from the page after login 
def extract_data(driver):
    print("\n Extracting data from the page...") 
    extracted = {}

    # Get the page title 
    extracted["page_title"] = driver.title
    print(f"   Page title: {extracted['page_title']}")
 
    # Get the current URL 
    extracted["current_url"] = driver.current_url
    print(f"Current URL: {extracted['current_url']}")
 
    # Get the main heading on the page 
    try:
        heading = driver.find_element(By.TAG_NAME, "h2")
        extracted["heading"] = heading.text.strip()
        print(f"   Heading: {extracted['heading']}")
    except:
        extracted["heading"] = "Not found"
 
    # Get the paragraph text on the page
    try:
        paragraph = driver.find_element(By.TAG_NAME, "p")
        extracted["paragraph"] = paragraph.text.strip()
        print(f"Paragraph: {extracted['paragraph']}")
    except:
        extracted["paragraph"] = "Not found"
 
    # Get the logout button text (confirms we're logged in)
    try:
        logout_btn = driver.find_element(By.CSS_SELECTOR, "a.button")
        extracted["logout_button_text"] = logout_btn.text.strip()
        print(f"Logout button: {extracted['logout_button_text']}")
    except:
        extracted["logout_button_text"] = "Not found"
 
    # Record the time we extracted this data
    from datetime import datetime
    extracted["extracted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    return extracted
  
# Logout 
def logout(driver):
    """Clicks the logout button to cleanly end the session."""
    try:
        logout_btn = driver.find_element(By.CSS_SELECTOR, "a.button")
        logout_btn.click()
        time.sleep(1)
        print("\nLogged out successfully.")
    except:
        print("\nCould not find logout button.")
  
# Save extracted data to a file
def save_data(data):
    """Saves the extracted data as a JSON file so you can use it later."""
    filename = "extracted_data.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\nData saved to '{filename}'")
  
# Run everything
def main():
    print("=" * 50)
    print("   Selenium Login + Data Extraction Demo")
    print("=" * 50) 
    driver = create_browser() 
    try:
        # Login
        login_success = login(driver)
 
        if login_success:
            # Extract data
            data = extract_data(driver)
 
            # Save it
            save_data(data)
 
            # Logout
            logout(driver)
 
            print("\nAll done! Check 'extracted_data.json' for results.")
        else:
            print("\nStopping — login failed.")
 
    finally:
        time.sleep(2)
        driver.quit()
        print("Browser closed.") 
 
if __name__ == "__main__":
    main()