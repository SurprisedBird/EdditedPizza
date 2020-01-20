from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.decorators import task
from dishes.models import Order, Size, Dish
from celery.schedules import crontab

URL = "https://smilefood.od.ua/products/pizza"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@task(name="add_pizza_to_basket")
def add_pizza_to_order(count, pizza_id, size):
    pizza = Dish.objects.get(id=pizza_id)
    size = Size.objects.get(name=dish_size)

    instance_pizza = pizza.create_instance_dish(count, size)
    order, created = Order.objects.get_or_create()
    order.pizzas.add(instance_pizza)

@periodic_task(
	run_every=(crontab(day_of_week='sunday')), name="parser", ignore_result=True)

def parser():
	response = requests.get(URL)
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

