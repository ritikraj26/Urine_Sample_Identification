import numpy as np
import cv2
from collections import Counter
from io import BytesIO
from PIL import Image

def analyze_image(image, num_clusters=10):
    try:
        # Convert the image data to a NumPy array
        image_data = BytesIO(image.read())
        pil_image = Image.open(image_data)
        numpy_image = np.array(pil_image)

        # Resize the image to the desired size for processing
        target_size = (100, 100)  # Adjust the size as needed
        resized_image = cv2.resize(numpy_image, target_size)

        # Reshape the image to a list of RGB pixels
        pixels = resized_image.reshape((-1, 3))

        # Convert the pixel values to float32 for k-means clustering
        pixels = np.float32(pixels)

        # Define the criteria for the k-means algorithm
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        # Perform k-means clustering to identify the most dominant colors
        _, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Convert the centers of the clusters to integers (RGB values)
        centers = np.uint8(centers)

        # Count the number of pixels in each cluster
        label_counts = Counter(labels.flatten())

        # Sort the colors by frequency
        sorted_colors = [centers[i] for i, _ in label_counts.most_common()]

        return sorted_colors
    except Exception as e:
        return None
