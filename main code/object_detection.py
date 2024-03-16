import cv2
import numpy as np

def identify_object_with_bounding_box(image_path, lower_bound, upper_bound):
    image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the color range using NumPy arrays
    lower_bound = np.array(lower_bound, dtype=np.uint8)
    upper_bound = np.array(upper_bound, dtype=np.uint8)

    # Create a mask using the color range
    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate bounding box
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h

        if 600 <  area < 800:

            # Draw bounding box on the original image
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            print(f"Width: {w}, Height: {h}, Area: {area}")

    cv2.imshow('Object with Bounding Box', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = './newframe/preprocessed_image_gaussian_blur.jpg'
lower_rgb = [50, 50, 50]  
upper_rgb = [150, 150, 150] 

identify_object_with_bounding_box(image_path, lower_rgb, upper_rgb)