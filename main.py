import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('result.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['name'],
                        data['address'],
                        data['contact'],
                        data['phone'],
                        data['fax'],
                        data['mail'],
                        data['member'],
                        data['telex'],
                        data['website'],
                        data['subsidary'],
                        data['management'],
                        data['business'],
                        data['import_product'],
                        data['export_product'],
                        data['sub_product']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', class_='list').find_all('td')

    for td in tds:
        link = 'http://www.icchk.org.hk/' + td.find('a').get('href')
        driver = webdriver.Chrome(executable_path='/Users/serg/Downloads/chromedriver')
        driver.get(link)
        html = driver.page_source
        company_page = BeautifulSoup(html, 'lxml')
        trs = company_page.find('div', class_='details').find('table').find('tr').find('table').find_all('tr')
        name = ' '.join((trs[1].find_all('td')[1].text).split())
        address = ' '.join((trs[2].find_all('td')[1].text).split())
        contact = ' '.join((trs[3].find_all('td')[1].text).split())
        phone = ' '.join((trs[4].find_all('td')[1].text).split())
        fax = ' '.join((trs[5].find_all('td')[1].text).split())
        mail = ' '.join((trs[6].find_all('td')[1].text).split())
        member = ' '.join((trs[7].find_all('td')[1].text).split())
        telex = trs[8].find_all('td')[1].text
        website = trs[10].find_all('td')[1].text
        subsidary = trs[12].find_all('td')[1].text
        management = ' '.join((trs[14].find_all('td')[1].text).split())

        business = trs[16].find_all('td')[1]
        result1 = []
        for i in business:
            result1.append(i)
        business = result1[2].strip()

        import_product = trs[18].find_all('td')[1]
        result2 = []
        for i in import_product:
            print('11111111111111111')
            print(i)
            result2.append(i)
        import_product = result2[1].strip()

        export_product = trs[20].find_all('td')[1]
        result3 = []
        for i in export_product:
            result3.append(i)
        export_product = result3[1].strip()

        sub_product = trs[22].find_all('td')[1]
        result4 = []
        for i in sub_product:
            result4.append(i)
        sub_product = result4[1].strip()

        data = {'name': name,
                'address': address,
                'contact': contact,
                'phone': phone,
                'fax': fax,
                'mail': mail,
                'member': member,
                'telex': telex,
                'website': website,
                'subsidary': subsidary,
                'management': management,
                'business': business,
                'import_product': import_product,
                'export_product': export_product,
                'sub_product': sub_product}
        write_csv(data)


def main():
    for i in range(1, 37):
        url = 'http://www.icchk.org.hk/business_directory.php?page={}&companyname=&membertype=&char='.format(i)
        get_data(get_html(url))


if __name__ == '__main__':
    main()
