from django.shortcuts import render
import json
from addresstest.models import address_info

def test(request):
    # for i in range(len(address_point)):
    #     address_longitude.append(address_point[i].longitude)
    #     address_latitude.append(address_point[i].latitude)
    #     address_data.append(address_point[i].data)
    # return render(request, 'address.html',
    #               {'address_longitude': json.dumps(address_longitude),
    #                'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)})
    if request.method == "POST":
        address = request.POST
        #向数据库添加 POST 来的点
        address_longitude = int(address.get("address_longitude"))
        address_latitude = int(address.get("address_latitude"))
        address_info.objects.create(longitude = address_longitude, latitude = address_latitude)
        #向模板传递数据点列表
        address_point = address_info.objects.all()
        address_longitude_list = []
        address_latitude_list = []
        for i in range(len(address_point)):
            address_longitude_list.append(address_point[i].longitude)
            address_latitude_list.append(address_point[i].latitude)
        list(address_longitude_list)
        list(address_latitude_list)
        return render(request, 'address.html', {'address_longitude': address_longitude_list, 'address_latitude': address_latitude_list})
    else:
        address_point = address_info.objects.all()
        address_longitude_list = []
        address_latitude_list = []
        for i in range(len(address_point)):
            address_longitude_list.append(address_point[i].longitude)
            address_latitude_list.append(address_point[i].latitude)
        return render(request, 'address.html', {'address_longitude': address_longitude_list, 'address_latitude': address_latitude_list})