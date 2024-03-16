import cv2

def apply_gaussian_blur(image_path, output_path, kernel_size=(7, 7), sigma=1):
    original_image = cv2.imread(image_path)

    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(original_image, kernel_size, sigma)

    cv2.imwrite(output_path, blurred_image)

kernel_size = (7, 7)  
sigma = 1 

for i in range(000,700):
    if i < 10:
        print(i)
        input_image_path = f"./newframe/resized_frame_000{i}.jpg"
        output_image_path = f"./newframe/pgbi_frame_000{i}.jpg"
    elif i < 100:
        print(i)
        input_image_path = f"./newframe/resized_frame_00{i}.jpg"
        output_image_path = f"./newframe/pgbi_frame_00{i}.jpg"
    else:
        input_image_path = f"./newframe/resized_frame_0{i}.jpg"
        output_image_path = f"./newframe/pgbi_frame_0{i}.jpg"

    apply_gaussian_blur(input_image_path, output_image_path, kernel_size, sigma)