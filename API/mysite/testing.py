from API.mysite.api.models import Bird, test_import

test_import()
queryset = Bird.objects.all().order_by('name')

print(queryset)
