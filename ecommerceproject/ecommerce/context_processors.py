from ecommerce.models import category
def menulink(request):
    links=category.objects.all()
    return dict(links=links)