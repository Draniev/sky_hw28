import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from categories.models import CatModel


@csrf_exempt
def page_categories(request):
    if request.method == "GET":
        categories = CatModel.objects.all()
        response = []
        for item in categories:
            response.append({
                'id': item.id,
                'name': item.name
            })
        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)

    elif request.method == 'POST':
        cat_data = json.loads(request.body)
        cat = CatModel.objects.create(
            name=cat_data['name'],
        )
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


def page_cat_by_id(request, pk: int):
    if request.method == "GET":
        try:
            ad = CatModel.objects.get(pk=pk)
            response = {
                'id': ad.id,
                'name': ad.name,
                }
        except CatModel.DoesNotExist:
            return JsonResponse({"error": "Not found"},
                                status=404)

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)
