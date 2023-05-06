from django.http import JsonResponse
from django.shortcuts import render


def page_ads(request):
    return JsonResponse({'Status': 'ADS'}, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)
