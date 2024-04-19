# Webpage Downloader

This is a Python program that allows you to download an entire webpage and its associated resources (CSS files, JavaScript files, images) for offline viewing. It utilizes the `requests` library for making HTTP requests and the `BeautifulSoup` library for parsing HTML content.

## Installation

1. Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Install the required dependencies by running the following command:
pip install requests beautifulsoup4



## Usage

1. Open the `webpage_downloader.py` file in a text editor.

2. Modify the `url` variable in the `main` function with the URL of the webpage you want to download.

3. Run the program by executing the following command: python WebPageDownloader.py

4. The program will download the webpage and save it in a folder named after the domain name. The main HTML file will be saved as `index.html` within the folder.

5. All the associated resources (CSS files, JavaScript files, images) referenced by the webpage will be downloaded and saved in the same folder.

6. Once the program finishes, you will see a message indicating that the page download is completed.





