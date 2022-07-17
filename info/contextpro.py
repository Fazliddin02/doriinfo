from .models import Category

def view_all(request):
	cat = Category.objects.all()


	context = {
	'cat':cat
	}

	return context
 