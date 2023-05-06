from django.http import JsonResponse
from django.shortcuts import render


def page_categories(request):
    return JsonResponse({'Status': 'CAT'}, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)
