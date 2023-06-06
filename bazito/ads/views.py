from ads.models import AdsModel, CatModel
from ads.serializers import AdsCreateSerializer, AdsSerializer, CatSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)


class CatViewSet(viewsets.ModelViewSet):
    queryset = CatModel.objects.all()
    serializer_class = CatSerializer


class AdsView(ListAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        q_obj = None

        cat_filter = request.GET.getlist('cat', None)
        if cat_filter:
            q_obj = Q(category__in=cat_filter)

        text_filter = request.GET.getlist('text', None)
        if text_filter:
            for text in text_filter:
                if q_obj:
                    q_obj &= Q(name__icontains=text) | Q(
                        description__icontains=text)
                else:
                    q_obj = Q(name__icontains=text) | Q(
                        description__icontains=text)

        loc_filter = request.GET.get('loc', None)
        if loc_filter:
            if q_obj:
                q_obj &= Q(author__locations__name__icontains=loc_filter)
            else:
                q_obj = Q(author__locations__name__icontains=loc_filter)

        price_from_filter = request.GET.get('price_from', None)
        if price_from_filter:
            if q_obj:
                q_obj &= Q(price__gte=price_from_filter)
            else:
                q_obj = Q(price__gte=price_from_filter)

        price_to_filter = request.GET.get('price_to', None)
        if price_to_filter:
            if q_obj:
                q_obj &= Q(price__lte=price_to_filter)
            else:
                q_obj = Q(price__lte=price_to_filter)

        if q_obj:
            self.queryset = self.queryset.filter(q_obj)
        return super().get(request, *args, **kwargs)


class AdCreateView(CreateAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsCreateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer


class AdDetailView(RetrieveAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdImageUpdateView(UpdateView):
    model = AdsView
    fields = ['image']

    def post(self, request, *args, **kwargs):
        # ad_data = json.loads(request.body)

        self.object.image = request.FILES['image']
        self.object.save()
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)
