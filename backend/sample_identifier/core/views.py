from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
from collections import Counter
from io import BytesIO
from PIL import Image


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES.get('image')

            # openCV logic here
            # print(uploaded_image)
            # print('hey')
            # colors = ["color1", "color2", "color3", "color4", "color5",
            #         "color6", "color7", "color8", "color9", "color10"]
            # image1 = cv2.imread(image)
            image_data = BytesIO(image.read())
            pil_image = Image.open(image_data)
            numpy_image = np.array(pil_image)
            # Resize the image to a smaller size for faster processing
            target_size = (100, 100)
            resized_image = cv2.resize(numpy_image, target_size)

            # Reshape the image to a list of RGB pixels
            pixels = resized_image.reshape((-1, 3))

            # Convert the pixel values to float32 for k-means clustering
            pixels = np.float32(pixels)

            # Define the criteria for the k-means algorithm
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

            # Perform k-means clustering to identify the most dominant colors
            _, labels, centers = cv2.kmeans(pixels, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

            # Convert the centers of the clusters to integers (RGB values)
            centers = np.uint8(centers)

            # Count the number of pixels in each cluster
            label_counts = Counter(labels.flatten())

            # Sort the colors by frequency
            sorted_colors = [centers[i] for i, _ in label_counts.most_common()]
            sorted_colors_json = [{'R': int(color[0]), 'G': int(color[1]), 'B': int(color[2])} for color in sorted_colors]
            # Return the sorted RGB values as a list
            # return sorted_colors
            print(sorted_colors_json)

            results = {
                "colors": sorted_colors_json
            }
            return JsonResponse(results)

    return JsonResponse({"error": "Invalid request"})

# @csrf_exempt
# def view_results(request):
