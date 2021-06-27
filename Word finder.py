from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

print("Enter the word you want to find the meaning of:\n")

while True:
    word = input()

    try:
        my_url = "https://www.dictionary.com/browse/" + word + "?s=t"
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")

        container = page_soup.findAll("div", {"class": "css-l5qngi-OrderedContentListContainer e1hk9ate0"})

        print(container[0].div.span.text)

    except:
        print("Word does not exist")
