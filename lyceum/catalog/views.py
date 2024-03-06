from django.http import HttpResponse


def item_list(request):
    return HttpResponse('<h2>Список Элементов</h2>')


def item_detail(request, pk):
    return HttpResponse('<h2>Подробно Элемент</h2>')
