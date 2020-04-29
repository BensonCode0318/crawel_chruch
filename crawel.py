from bs4 import BeautifulSoup as bs
import json,requests



def main():
    for i in range(1,13):
        url = 'https://taipei.catholic.org.tw/taipei/chi/load_church/' + str(i)
        html = requests.get(url)
        soup = bs(html.text,'lxml')
        href = [i['href'] for i in soup.select('.TAB_CONTENT a')]
        for chruch_url in href:
            get_chruch_content(chruch_url)
        
def get_chruch_content(url):
    html = requests.get(url)
    soup = bs(html.text,'lxml')
    



if __name__ == "__main__":
    main()