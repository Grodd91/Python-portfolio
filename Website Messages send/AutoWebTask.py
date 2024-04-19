from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Initialize Chrome browser
options = Options()
options.add_argument("--headless")  # Run in headless mode (without displaying the browser)
driver = webdriver.Chrome(options=options)

def login(username, password):
    # Open the login page
    driver.get("https://example.com/login")
    
    # Enter login credentials
    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    # Submit the login form
    password_input.send_keys(Keys.ENTER)

def send_message(receiver, message):
    # Open the messages page
    driver.get("https://example.com/messages")
    
    # Search for the receiver
    search_input = driver.find_element_by_id("search")
    search_input.send_keys(receiver)
    search_input.send_keys(Keys.ENTER)
    
    # Enter the message content
    message_input = driver.find_element_by_id("message")
    message_input.send_keys(message)
    
    # Send the message
    send_button = driver.find_element_by_id("send")
    send_button.click()

def perform_task(username, password, receiver, message):
    login(username, password)
    send_message(receiver, message)
    
    # Logout
    actions = ActionChains(driver)
    profile_button = driver.find_element_by_id("profile")
    actions.move_to_element(profile_button).perform()
    logout_button = driver.find_element_by_id("logout")
    actions.move_to_element(logout_button).click().perform()

def main():
    # User credentials
    username = "example_username"
    password = "example_password"
    
    # Message details
    receiver = "example_receiver"
    message = "Sample message"
    
    perform_task(username, password, receiver, message)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
