import datetime
import http

from ninja import NinjaAPI
from ninja import Path, Query
from ninja.pagination import paginate, PageNumberPagination

from typing import List


from django.http import HttpResponse, HttpResponseRedirect

from .schema import Item, TaskSchema, Filters, PathDate
from .schema import UserOut, UserIn, User, UserSchema
from .schema import EmployeeIn, EmployeeOut
from .schema import DepartmentIn

from flask import Flask, jsonify

from .model import Task
from .model import Employee, Department
from .schema import Token, Message
api = NinjaAPI()

@api.get('')
def testing(request):
    return jsonify({'Hello': 'World!'})

@api.get("/hello", url_name="user_list")
def hello(request):
    return "Hello world"

@api.get("/test")
def test(request):
    return HttpResponse(200)

@api.get("/items/{int:item_id}")
def read_item(request, item_id: int):
    return {"item_id": item_id}

@api.get("/events/{year}/{month}/{day}")

def events(request, date: PathDate = Path(...)):
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
def events(request, filters: Filters = Query(...)):
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
def create(request, item: Item):
    return item

@api.get("/tasks", response=List[TaskSchema])
def tasks(request):
    queryset = Task.objects.select_related("owner")
    return list(queryset)

@api.post("/task")
def create_task(request, task: TaskSchema):
    return task

@api.post("/users/", response=UserOut)
def create_user(request, data: UserIn):
    user = User(username=data.username)
    user.set_password(data.password)
    user.save()
    return user

@api.post("/employees")
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}

@api.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    return qs

@api.post("/department")
def create_department(request, data: DepartmentIn):
    department = Department.objects.create(**data.dict())
    return {"dd" : department.id}


#pagnation test
@api.get('/users', response=List[UserSchema])
@paginate(PageNumberPagination)
def list_users(request):
    '''
    pagenation tutorial from ninja fromwork
    :param request:
    :return:
    '''
    return User.objects.all()



