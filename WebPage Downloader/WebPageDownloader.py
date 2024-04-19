
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin

def download_page(url):
    # Downloading the web page content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Creating a folder to store the webpage
    parsed_url = urlparse(url)
    folder_name = parsed_url.netloc
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Saving the main page
    with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as f:
        f.write(str(soup))

    # Downloading and saving the resources of the page
    for link in soup.find_all("link"):
        if link.get("href"):
            download_resource(urljoin(url, link["href"]), folder_name)
    
    for script in soup.find_all("script"):
        if script.get("src"):
            download_resource(urljoin(url, script["src"]), folder_name)

    for img in soup.find_all("img"):
        if img.get("src"):
            download_resource(urljoin(url, img["src"]), folder_name)

def download_resource(url, folder_name):
    # Downloading the resource
    response = requests.get(url)
    resource_name = os.path.basename(urlparse(url).path)

    # Saving the resource in the folder
    with open(os.path.join(folder_name, resource_name), "wb") as f:
        f.write(response.content)

    print(f"Downloaded: {resource_name}")

def main():
    # URL of the webpage to download
    url = "https://www.example.com"

    # Downloading the webpage
    download_page(url)

    print("Page download completed.")

if __name__ == "__main__":
    main()
