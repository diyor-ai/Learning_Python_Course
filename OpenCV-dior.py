"""

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read frame
    frame = cv2.flip(frame, 1)  # Mirror the frame

    # Draw Text (Blue)
    cv2.putText(frame, "Mukhammaddiyor", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Clean up
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read frame
    frame = cv2.flip(frame, 1)  # Mirror the frame

    # Draw Center Circle (Blue)
    h, w, _ = frame.shape
    cv2.circle(frame, (w // 2, h // 2), 12, (255, 0, 0), -1)

    cv2.imshow('Practice', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Clean up
cv2.destroyAllWindows()

import cv2

img = cv2.imread("test.jpg")

if img is None:
    print("Error: Unable to read the image, please check the image path!")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original Image", img)
    cv2.imshow("Gray Image", gray_img)

    cv2.imwrite("gray_image.jpg", gray_img)  # Fixed: imwrite, not write
    print("Grayscale image saved as: gray_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


import cv2
import numpy as np

img = cv2.imread("test.jpg")

if img is None:
    print("Error: Image not found! Please check the path.")
    exit()

height, width = img.shape[:2]
split_x = width // 3  # col position

# from col0 to col split_x
left_color = img[:, :split_x]

# right side grayscale
right_gray = cv2.cvtColor(img[:, split_x:], cv2.COLOR_BGR2GRAY)

# B-G-R → convert one channel to three channels
right_gray = cv2.cvtColor(right_gray, cv2.COLOR_GRAY2BGR)

combined_img = np.hstack((left_color, right_gray))

cv2.imshow("Split-Color-Grayscale", combined_img)
cv2.imwrite("split_result.jpg", combined_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img = cv2.imread("test.jpg")

if img is None:
    print("Error: Unable to read the image, please check the image path!")
else:
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

    cv2.imshow("Original Image", img)
    cv2.imshow("Blurred Image", blurred_img)

    cv2.imwrite("blurred_image.jpg", blurred_img)
    print("Blurred image saved as: blurred_image.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
import cv2

img = cv2.imread("test.jpg")

if img is None:
    print("Error: Unable to read the image, please check the image path!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshold(image, threshold, white intensity, BINARY mode)
    _, binary_img = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)  # receive return value but not use

    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Image", binary_img)

    cv2.imwrite("binary_image.jpg", binary_img)
    print("Binary image saved as: binary_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()