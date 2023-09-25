from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_image = request.FILES.get('image')

            # openCV logic here
            print(uploaded_image)
            print('hey')
            colors = ["color1", "color2", "color3", "color4", "color5",
                    "color6", "color7", "color8", "color9", "color10"]
            results = {
                "colors": colors
            }

            return JsonResponse(results)

    return JsonResponse({"error": "Invalid request"})

# @csrf_exempt
# def view_results(request):
