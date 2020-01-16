from bs4 import BeautifulSoup
import requests

url = "https://smilefood.od.ua/products/pizza"

response = requests.get(url)
contents = response.text

soup = BeautifulSoup(contents, 'lxml')
prod_list = soup.find_all('li', {'class': 'catalogue-products__item'})

general_arrey = []

for row in prod_list:
    partial_dict = {}

    product_name = row.find_all("span", {'class': 'title'})[0].text
    product_price = row.find_all("span", {'data-preview-price': 'true'})[0].text
    product_description = row.find_all('div', {'class': 'product-text'})[0].text
    product_image = row.find_all('img')[0].attrs['src']

    partial_dict.update(
        {'name': product_name,
        'price': product_price,
        'description': product_description,
        'image': product_image}
        )

    general_arrey.append(partial_dict)

print(general_arrey)

