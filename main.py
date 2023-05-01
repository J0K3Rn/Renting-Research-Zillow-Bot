from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# CHANGE ME
ZILLOW_LINK = ""
GOOGLE_FORM = ""

if ZILLOW_LINK == "" or GOOGLE_FORM == "":
    print("Please update ZILLOW_LINK and GOOGLE_FORM in main.py!")
    exit(1)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

soup = BeautifulSoup(requests.get(ZILLOW_LINK, headers=headers).content, "html.parser")

data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
    .contents[0]
    .strip("!<>-")
)

# uncomment this to print all data:
# with open('out.txt', 'w') as f:
#     f.write(json.dumps(data, indent=4))
#json.dumps(data, indent=4)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for result in data["cat1"]["searchResults"]["listResults"]:
    try:
        address = result["address"]
        price = result["unformattedPrice"]
        beds = result["beds"]
        baths = result["baths"]
        area = result["area"]
        # None inputs cause issues with Google Forms
        if area == None:
            area = "n/a"
        url = result["detailUrl"]

        print(f"{address} {price} {beds} {baths} {area} {url}")

        driver.get(GOOGLE_FORM)
        time.sleep(5)

        address_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_input.send_keys(address)

        price_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_input.send_keys(price)

        beds_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        beds_input.send_keys(beds)

        baths_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
        baths_input.send_keys(baths)

        area_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
        area_input.send_keys(area)

        url_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input")
        url_input.send_keys(url)

        time.sleep(2)

        submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")
        submit_button.click()

        time.sleep(5)
    except:
        # Due to some inputs not being valid
        pass
