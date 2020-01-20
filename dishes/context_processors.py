from dishes.models import Size
from dishes.models import Order

def sizes(request):
    return {
       "sizes": Size.objects.all()
    }

def orders():
	return {
	"orders" : Order.objects.all()
	}