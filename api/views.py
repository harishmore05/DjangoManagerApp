from django.http import JsonResponse

# Create your views here.
def home(request):
	return JsonResponse({'info': 'Django Testing', 'name': 'Harish'})