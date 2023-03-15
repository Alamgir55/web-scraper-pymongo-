from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    r = requests.get("https://www.bing.com/images/search", params=params)
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    # print(r.content)
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    links = soup.findAll("a", {"class": "iusc"})
    # print(links)

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting", item.attrs['href'])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./images_src/", + title, img.format)
            except:
                print("Could not save image.")
        except:
            print("Could not save Image")

    StartSearch()


StartSearch()
