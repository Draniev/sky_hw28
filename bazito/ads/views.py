import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ads.models import AdsModel


@csrf_exempt
def page_ads(request):
    if request.method == "GET":
        ads = AdsModel.objects.all()
        response = []

        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
            })
        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)

    elif request.method == 'POST':
        ad_data = json.loads(request.body)
        ad = AdsModel.objects.create(
            name=ad_data['name'],
            author=ad_data['author'],
            price=ad_data['price'],
            description=ad_data['description'],
            is_published=ad_data['is_published'],
            )
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


def page_ad_by_id(request, pk: int):
    if request.method == "GET":
        try:
            ad = AdsModel.objects.get(pk=pk)
            response = {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                }
        except AdsModel.DoesNotExist:
            return JsonResponse({"error": "Not found"},
                                status=404)

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)
