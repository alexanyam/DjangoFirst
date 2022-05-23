from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item
import string
# Create your views here.


name = 'Александр'
surname = 'Морозов'
surname1 = 'Владимирович'
fio = surname + ' '+ name[0]+'. '+surname1[0]+'.'
email = 'alexanyam@gmail.com'
phone = '+7 499 123 45 67'

items = [
    {"id": 1, "name": "Кроссовки abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Coca-cola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"},
]


def home(request):
    pag = ['<h1>Изучаем django</h1>', f'<strong>Автор</strong>: <i>{fio}</i>']
    # return HttpResponse(pag)
    return render(request, "index.html")

def about(request):
    info = [f'Имя: <strong>{name} </strong><br>',
            f'Отчество: <strong>{surname1} </strong><br>',
            f'Фамилия: <strong>{surname} </strong><br>',
            f'Телефон: <strong>{phone} </strong><br>',
            f'Email: <strong>{email} </strong>'
    ]
    return HttpResponse(info)


def item_page(request, id):
    # for item in items:
    #     if item['id'] == num:
    #         info = f"Товар: {item['name']}"
    #         return HttpResponse(info)
    # return HttpResponse('Товар не найден !')
    #    return HttpResponse(items[num-1]['name'])
    items = Item.objects.get(pk=id)
    return render(request, "item_page.html", {"items": items})

# def items_list(request):
#     info = '<lo>'
#     for item in items:
#         info += f"<li> <a href='\item\{item['id']}'> {item['name']} </a></li><br>"
#     info += '</lo>'
#     return HttpResponse(info)

def items_list(request):
    items = Item.objects.all()
    context = {
        "items" : items
    }
    # d = {"name": []}
    # e = items.copy()
    # for c in e:
    #     if alf == "No" or c["name"][0] == alf:
    #         d.append({"item": c["name"]})
    #     # else:
    #     #     print(c["Country"][0], c["Country"])
    return render(request, "items.html", {"items": items})
    # # return HttpResponse(c)
