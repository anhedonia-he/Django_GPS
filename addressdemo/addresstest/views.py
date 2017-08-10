from django.shortcuts import render
import json
from addresstest.models import address_info

def test(request):
    address_point = address_info.objects.all()
    address_data = []
    # for i in range(len(address_point)):
    #     address_longitude.append(address_point[i].longitude)
    #     address_latitude.append(address_point[i].latitude)
    #     address_data.append(address_point[i].data)
    # return render(request, 'address.html',
    #               {'address_longitude': json.dumps(address_longitude),
    #                'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)})
    if request.method == 'GET':
        address = request.GET
        for address_longitude , address_latitude in address:
            return render(request, 'address.html', {'address_longitude': address_longitude, 'address_latitude': address_latitude})