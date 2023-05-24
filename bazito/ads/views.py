import json

from ads.models import AdsModel, CatModel
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(ListView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = self.object_list
        response = []

        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author.username,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': ad.category.name,
                # 'image': ad.image,
            })
        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = AdsModel
    fields = ['name', 'author_id', 'price',
              'description', 'category_id', 'is_published']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        AdsModel.objects.create(
            name=ad_data['name'],
            author_id=ad_data['author_id'],
            price=ad_data['price'],
            description=ad_data['description'],
            is_published=ad_data['is_published'],
            category_id=ad_data['category_id'],
        )
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = AdsView
    fields = ['name', 'price', 'description', 'category_id', 'is_published']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        self.object.name = ad_data['name']
        self.object.price = ad_data['price']
        self.object.description = ad_data['description']
        self.object.category_id = ad_data['category_id']
        self.object.is_published = ad_data['is_published']
        self.object.save()
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = AdsModel
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        try:
            ad = self.get_object()
            response = {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author.username,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': ad.category.name,
            }
        except AdsModel.DoesNotExist:
            return JsonResponse({"error": "Not found"},
                                status=404)

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CatsView(ListView):
    model = CatModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        categories = self.object_list
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


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = CatModel
    fields = ['name']

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        CatModel.objects.create(name=cat_data['name'])
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CatUpdateView(UpdateView):
    model = CatModel
    fields = ['name']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)

        self.object.name = cat_data['name']
        self.object.save()
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteView(DeleteView):
    model = CatModel
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CatDetailView(DetailView):
    model = CatModel

    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
            response = {
                'id': cat.id,
                'name': cat.name,
            }
        except CatModel.DoesNotExist:
            return JsonResponse({"error": "Not found"},
                                status=404)

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)
