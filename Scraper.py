import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import os
import re
import urllib

def page_parser(page_url):
    data = urlopen(page_url)
    page_result = bs(data, 'html.parser')
    return page_result

def image_finder(page_result):
    image_urls = []
    parent_div = page_result.find_all('div', class_='Atcj9b')
    for images in parent_div:
        image = (images.find("img")).get('src')
        image = image.split("=")[0] + "=w2560-h1440-rw"
        image_urls.append(image)
    return image_urls

def sanitize_folder_name(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def image_downloader(image_urls):
    sub_folder = sanitize_folder_name(title)
    path = os.path.join('images', sub_folder)
    os.makedirs(path, exist_ok=True)

    for i, image_url in enumerate(image_urls):
        print(f"Downloaddding image {i+1}")
        file_name = f"image_{i+1}.png"
        file_path = os.path.join(path, file_name)
        try:
            urllib.request.urlretrieve(image_url, file_path)
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")

os.makedirs('images', exist_ok=True)
base_url = "https://play.google.com"
q = input("Enter search query: ")
url = "https://play.google.com/store/search?q=" + urllib.parse.quote(q)
data= urlopen(url)
result = bs(data , 'html.parser')
links = result.find_all('a', class_="Si6A0c")


for i , a_tag in enumerate(links):
    href = a_tag.get('href')
    print(f"\nExtracting Link {i+1}:")
    if href.startswith('/store/apps/details'):
        full_url = base_url + href
        page_data = page_parser(full_url)
        title = page_data.find('span', class_='AfwdI').text
        print(f"App Title: {title}")
        images = image_finder(page_data)
        print(f"Number of images found: {len(images)}")
        image_downloader(images)