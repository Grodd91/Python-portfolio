import requests
import time

def visit_website(url, num_visits, interval):
    for i in range(num_visits):
        print(f"Visiting {url} - Visit #{i+1}")
        response = requests.get(url)
        
        # You can add any processing or analysis of the response here
        
        time.sleep(interval)

# Example usage
url = "https://www.xyz.com"
num_visits = 10
interval = 10  # seconds

visit_website(url, num_visits, interval)
