from django.http import JsonResponse
from django.shortcuts import render

from categories.models import CatModel


def page_categories(request):
    categories = CatModel.objects.all()
    response = []
    for item in categories:
        response.append({
            'id': item.id,
            'name': item.name
        })
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)


def page_cat_by_id(request, pk: int):
    if request.method == "GET":
        try:
            ad = CatModel.objects.get(pk=pk)
            response = {
                'id': ad.id,
                'name': ad.name,
                }
        except AdsModel.DoesNotExist:
            return JsonResponse({"error": "Not found"},
                                status=404)

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)
