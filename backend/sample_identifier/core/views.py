from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .image_utils import analyze_image


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            sorted_colors = analyze_image(image)
            
            # serializing the data
            sorted_colors_json = [{'R': int(color[0]), 'G': int(color[1]), 'B': int(color[2])} for color in sorted_colors]

            print(sorted_colors_json)

            results = {
                "colors": sorted_colors_json
            }
            return JsonResponse(results)

    return JsonResponse({"error": "Invalid request"})

