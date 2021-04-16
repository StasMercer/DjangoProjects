import datetime

import pytz
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, HttpResponse
from django.template.defaultfilters import date
from django.views.decorators.csrf import csrf_exempt

from .models import Table, Person


# Create your views here.
def render_main(request):
    data = []
    user = request.user
    if request.user.is_anonymous:
        user = None

    for table in Table.objects.all():

        table_obj = {'persons': [], 'name': ''}
        table_obj['name'] = table.table_name
        table_obj['id'] = table.id
        for person in table.persons.all():
            tz = pytz.timezone('Europe/Kiev')
            delta = datetime.datetime.now(tz) - person.time
            wait = {'days': delta.days, 'hours': datetime.timedelta(seconds=delta.seconds)}
            person.time_waits = wait
            person.time = date(person.time, 'd/m/Y H:m')
            table_obj['persons'].append(person)

        data.append(table_obj)
    print(user)
    return render(request, template_name='core/index.html', context={'data': data, 'user': user})


def add_in_queue(request):
    name = request.POST.get('name')
    table_id = request.POST.get('table_id')
    print(name, table_id)
    p = Person.objects.create(name=name)
    t = Table.objects.get(id=int(table_id))
    t.persons.add(p)
    return render_main(request)


def render_admin(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    print(username, password)
    user = authenticate(request=request, username=username, password=password)
    if user:
        login(request, user=user)
        print('user loged in ' + user.username)
        return render_main(request)
    else:
        return render(request, template_name='core/index.html', context={'error': 'user not found'})


def delete_from_queue(request):
    print(request.user)
    person_id = request.POST.get('person_id')
    table_id = request.POST.get('table_id')
    p = Person.objects.get(id=int(person_id))
    t = Table.objects.get(id=int(table_id))
    t.persons.remove(p)
    return render_main(request)


def logout_user(request):
    logout(request)
    return render_main(request)


@csrf_exempt
def mark_user(request):
    user_id = request.POST.get('id')
    bg_color = request.POST.get('bg_color')

    p = Person.objects.get(pk=user_id)
    p.color_class = bg_color
    p.save()
    return HttpResponse('ok', status=200)
