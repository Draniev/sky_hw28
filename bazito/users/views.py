import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from users.models import UserModel, LocModel


@method_decorator(csrf_exempt, name='dispatch')
class UsersView(ListView):
    model = UserModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        # users = self.object_list
        cur_page = int(request.GET.get('page', 1))
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_objects = paginator.get_page(cur_page)

        response = []

        for user in page_objects:
            response.append({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'locations': list(map(str, user.locations.all())),
            })
        return JsonResponse({'items': response,
                             'page_number': page_objects.number,
                             'total_pages': paginator.num_pages,
                             'per_page': settings.TOTAL_ON_PAGE,
                             },
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = UserModel
    fields = ['username', 'first_name', 'last_name',
              'password', 'role', 'age', 'locations']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        locations = []
        for item in user_data['locations']:
            loc_obj = LocModel.objects.get_or_create(name=item)
            locations.append(loc_obj)

        UserModel.objects.create(
            username=user_data['username'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            password=user_data['password'],
            role=user_data['role'],
            age=user_data['age'],
            locations=locations,
        )

        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = UserModel
    fields = ['username', 'first_name', 'last_name',
              'password', 'role', 'age', 'locations']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.username = user_data['name']
        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.password = user_data['password']
        self.object.role = user_data['role']
        self.object.age = user_data['age']
        for item in user_data['locations']:
            loc_obj = LocModel.objects.get_or_create(name=item)
            self.object.locations.add(loc_obj)

        self.object.save()
        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = UserModel
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'Status': 'OK'},
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=201)
