from bs4 import BeautifulSoup as bs
import json,requests



def main():
    for i in range(1,13):
        url = 'https://taipei.catholic.org.tw/taipei/chi/load_church/' + str(i)
        html = requests.get(url)
        soup = bs(html.text,'lxml')
        href = [i['href'] for i in soup.select('.TAB_CONTENT a')]
        json_data = '['
        for chruch_url in href:
            json_data += get_chruch_content('https://taipei.catholic.org.tw/'+chruch_url)+','
        json_data = json_data.strip(',')
        json_data += ']'
    json_str = json.dumps(json_data)
    with open('data.json','w+') as file:
        file.write(json_str)
        
def get_chruch_content(url):
    temp = 'https://taipei.catholic.org.tw'
    html = requests.get(url)
    soup = bs(html.text,'lxml')
    title = soup.select('.PAGE_TI')[0].text.replace(' ','').split()
    title = ''.join(title)
    deanery = soup.select('.PATH :nth-child(3)')[0].text
    img = temp+soup.select('#img1')[0]['src']
    fa_img = temp+soup.select('.FATHER_IMG :nth-child(1)')[0]['src']
    fa_name = soup.select('.FATHER_TEXT :nth-child(2)')[0].text
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
        'fa_img':fa_img,
        'fa_name':fa_name,
        'fa_phone':fa_phone,
        'fa_tax':fa_tax,
        'fa_address':fa_address,
        'fa_email':fa_email,
        'fa_url':fa_url,
        'chruch_weekdays':chruch_weekdays,
        'chruch_weekend':chruch_weekend,
        'chruch_box':chruch_box,
    }
    return json.dumps(data)



if __name__ == "__main__":
    main()