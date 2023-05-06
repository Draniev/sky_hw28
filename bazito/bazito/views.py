from django.http import JsonResponse


def page_index(request):
    return JsonResponse({'Status': 'OK'}, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)
