import cv2
import numpy as np
import csv

def identify_object_with_bounding_box(image_path, csv_writer, lower_bound, upper_bound):
    image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the color range using NumPy arrays
    lower_bound = np.array(lower_bound, dtype=np.uint8)
    upper_bound = np.array(upper_bound, dtype=np.uint8)

    # Create a mask using the color range
    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the center of the image
    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    for contour in contours:
        # Calculate bounding box
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h

        if 400 < area < 1000:
            # Get the region of interest (ROI) within the bounding box
            roi = image[y:y+h, x:x+w]

            # Calculate the average RGB value of the ROI
            average_rgb = np.mean(roi, axis=(0, 1))

            if (110 <= average_rgb[0] <= 136) and (100 <= average_rgb[1] <= 120) and (75 <= average_rgb[2] <= 113):
                # Draw bounding box on the original image
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Calculate angle between object and center of the image
                angle = np.degrees(np.arctan2(center_y - (y + h / 2), center_x - (x + w / 2)))

                # Write information to CSV file
                csv_writer.writerow([image_path, x, y, w, h, area, angle])

                print(f"Frame: {image_path}, X: {x}, Y: {y}, Width: {w}, Height: {h}, Area: {area}, Angle: {angle}")

    cv2.imwrite(f'./boundedimg/bounded_{image_path.split("/")[-1]}', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

lower_rgb = [50, 50, 50]
upper_rgb = [150, 150, 150]

output_csv_path = './boundedimg/object_info_all.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Frame", "X", "Y", "Width", "Height", "Area", "Angle"])

    for i in range(0, 550):
        if i < 10:
            print(i)
            input_image_path = f"./newframe/pgbi_frame_000{i}.jpg"
        elif i < 100:
            print(i)
            input_image_path = f"./newframe/pgbi_frame_00{i}.jpg"
        else:
            print(i)
            input_image_path = f"./newframe/pgbi_frame_0{i}.jpg"

        identify_object_with_bounding_box(input_image_path, csv_writer, lower_rgb, upper_rgb)
