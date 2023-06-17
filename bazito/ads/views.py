from ads.models import AdsModel, CatModel, SelModel
from ads.permissions import IsModerator, IsOwner, ReadOnly
from ads.serializers import (AdsCreateSerializer, AdsSerializer, CatSerializer,
                             SelCreateSerializer, SelViewSerializer)
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import status, viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CatViewSet(viewsets.ModelViewSet):
    queryset = CatModel.objects.all()
    serializer_class = CatSerializer
    permission_classes = [ReadOnly | IsOwner | IsModerator]


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
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsCreateSerializer
    permission_classes = [IsOwner | IsModerator]


class AdDeleteView(DestroyAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsOwner | IsModerator]


class AdDetailView(RetrieveAPIView):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]


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


class SelViewSet(viewsets.ModelViewSet):
    queryset = SelModel.objects.all()
    serializer_class = SelViewSerializer
    permission_classes = [ReadOnly | IsOwner | IsModerator]
    # permission_classes = [IsOwner]

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.username
        serializer = SelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        request.data['owner'] = request.user.username
        instance = self.get_object()
        # serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer = SelCreateSerializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
