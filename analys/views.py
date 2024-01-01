from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from materials.models import (Materials)
from django.http import JsonResponse
from django.shortcuts import render
import json

# This function return view for new analys page
@login_required
@csrf_exempt
def new_analys(request):
  return render(request, 'pages/analys/new.html', { 'segment': 'analys' })

# View to return a list of materials as JSON.
@login_required
@csrf_exempt
def materials_list(request):
    # Fetching all material objects from the database
    materials = Materials.objects.all().values('material_key', 'material_name')

    # Converting the queryset to a list of dicts
    materials_list = list(materials)
    
    # Returning the list as JSON
    return JsonResponse(materials_list, safe=False)

# This function give material name and return detail of material
@login_required
@csrf_exempt
def materials_detail(request):
  ''' check if request is post its valid request else return bad request '''
  if request.method == 'POST':
    data = json.loads(request.body)
    material_name = data.get('material_name')
    material_object = Materials.objects.filter(material_name=material_name)
    detail = {}
    for data in material_object:
      detail['material_key'] = data.material_key
      detail['material_name'] = data.material_name
      detail['material_color'] = data.material_color
      detail['material_unit'] = data.material_unit

    return JsonResponse({'status': detail, 'success': True})

  else:
    return JsonResponse({'status':'درخواست نامعتبر است', 'success': False})