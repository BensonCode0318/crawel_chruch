from bs4 import BeautifulSoup as bs
import json,requests



def main():
    arr = []
    for i in range(1,13):
        url = 'https://taipei.catholic.org.tw/taipei/chi/load_church/' + str(i)
        html = requests.get(url)
        soup = bs(html.text,'lxml')
        href = [i['href'] for i in soup.select('.TAB_CONTENT a')]
        for chruch_url in href:
            arr.append(get_chruch_content('https://taipei.catholic.org.tw/'+chruch_url))
    json_str = json.dumps(arr)
    print(json_str)
    with open('data.json','w+') as file:
        file.write(json_str)
        
def get_chruch_content(url):
    temp = 'https://taipei.catholic.org.tw'
    html = requests.get(url)
    soup = bs(html.text,'lxml')
    title = soup.select('.PAGE_TI')[0].text.replace(' ','').split() 
    title = ''.join(title) #remove title \n and space
    deanery = soup.select('.PATH :nth-child(3)')[0].text
    img = temp+soup.select('#img1')[0]['src']
    fa_img = temp+soup.select('.FATHER_IMG :nth-child(1)')[0]['src']
    secretary = soup.select('.FATHER_TEXT :nth-child(2)')[0].text
    fa_phone = soup.select('#s1')[0].text
    fa_tax = soup.select('#s2')[0].text
    fa_address = soup.select('#s3')[0].text
    fa_email = soup.select('#s4 a')[0].text
    fa_url = soup.select('#s5 a')[0].text
    chruch_weekdays = soup.select('#s6')[0].text
    chruch_weekend = soup.select('#s7')[0].text
    chruch_box = soup.select('.CHURCH_BOX')[0].text
    
    data = {
        'title':title,
        'deanery':deanery,
        'img':img,
        'secretary_img':fa_img,
        'secretary':secretary,
        'phone1':fa_phone,
        'tax':fa_tax,
        'address':fa_address,
        'email':fa_email,
        'web':fa_url,
        'chruch_weekdays':chruch_weekdays,
        'chruch_weekend':chruch_weekend,
        'chruch_box':chruch_box,
    }
    return data



if __name__ == "__main__":
    main() 