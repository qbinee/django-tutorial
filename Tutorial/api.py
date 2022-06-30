import datetime
from ninja import NinjaAPI
from ninja import Path, Query
from django.http import HttpResponse, HttpResponseRedirect
from . import schema
api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/test")
def test(request):
    return HttpResponse(200)

@api.get("/items/{int:item_id}")
def read_item(request, item_id: int):
    return {"item_id": item_id}

@api.get("/events/{year}/{month}/{day}")

def events(request, date: schema.PathDate = Path(...)):
    """
    path 는 path parm 이다. 더럽히지 않기 위해서 이를 클레스로 정리한게 schema
    """
    return {"date": date.value()}

weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]


@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    return weapons[offset: offset + limit]

@api.get("/weapons/search")
def search_weapons(request, q: str, offset: int = 0):
    """
    :param request:
    :param q:
    :param offset:
    :return:
    """
    results = [w
               for w in weapons
               if q in w.lower()]
    print(q, results)
    return results[offset: offset + 10]


@api.get("/filter")
def events(request, filters: schema.Filters = Query(...)):
    """
    :param request: query 를 숨기는 것이 가능하다
    :param filters:
    :return:
    """
    if filters.limit < 100:
        return HttpResponse(200)
    else:
        return HttpResponse(400)


@api.post("/items")
def create(request, item: schema.Item):
    return item
