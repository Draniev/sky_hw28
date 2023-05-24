import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import AdsModel, CatModel


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
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

    def post(self, request):
        ad_data = json.loads(request.body)
        AdsModel.objects.create(
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


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
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


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
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

    def post(self, request):
        cat_data = json.loads(request.body)
        CatModel.objects.create(name=cat_data['name'])
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CatDetailView(DetailView):
    model = CatModel
    
    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
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
