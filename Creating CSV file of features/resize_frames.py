import cv2

def resize_image(input_path, output_path, new_width, new_height):
    image = cv2.imread(input_path)

    resized_image = cv2.resize(image, (new_width, new_height))

    # Save the resized image
    cv2.imwrite(output_path, resized_image)


new_width = 800  
new_height = 600  

for i in range(000,700):
    if i < 10:
        print(i)
        input_image_path = f"./frames/frame_000{i}.jpg"
        output_image_path = f"./newframe/resized_frame_000{i}.jpg"
    elif i < 100:
        print(i)
        input_image_path = f"./frames/frame_00{i}.jpg"
        output_image_path = f"./newframe/resized_frame_00{i}.jpg"
    else:
        input_image_path = f"./frames/frame_0{i}.jpg"
        output_image_path = f"./newframe/resized_frame_0{i}.jpg"

    resize_image(input_image_path, output_image_path, new_width, new_height)