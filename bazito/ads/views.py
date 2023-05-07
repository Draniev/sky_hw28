import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import AdsModel


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
