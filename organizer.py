from bs4 import BeautifulSoup

def organize():
    html = open('cv.html', 'rb', buffering=1)
    print(html.read())
    soup = BeautifulSoup(html.read(), 'html.parser')