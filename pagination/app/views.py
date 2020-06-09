import csv
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def csv_dict_reader():
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as f:
        data = list()
        for row in csv.DictReader(f):
            data.append({x: row[x] for x in ["Name", "Street", "District"]})
    return data


def bus_stations(request):
    data = csv_dict_reader()
    paginator = Paginator(data, 10)
    current_page = int(request.GET.get("page", 1))
    page_object = paginator.get_page(current_page)
    next_page, prev_page = None, None
    if page_object.has_next():
        next_page = page_object.next_page_number()
    else:
        next_page = current_page
    if page_object.has_previous():
        prev_page = page_object.previous_page_number()
    else:
        prev_page = current_page
    return render_to_response('index.html', context={
        'bus_stations': page_object,
        'current_page': current_page,
        'prev_page_url': f'{reverse(bus_stations)}?page={prev_page}',
        'next_page_url': f'{reverse(bus_stations)}?page={next_page}',
    })


