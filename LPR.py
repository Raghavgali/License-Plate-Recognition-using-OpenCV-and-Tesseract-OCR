import cv2
import imutils
import pytesseract

# Set the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"Path_to_Tesseract_file"

# Read the image file
image = cv2.imread('Path_of_the_car_image_to_be_detected')
# Resize the image
image = imutils.resize(image, width=500)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter for noise reduction
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# Find edges using the Canny edge detector
edged = cv2.Canny(gray, 170, 200)

# Find contours based on edges
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

# Initialize variable for the number plate contour
number_plate_cnt = None

# Loop over contours to find the best possible approximate contour of the number plate
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        number_plate_cnt = approx
        break

# Draw the selected contour on the original image
cv2.drawContours(image, [number_plate_cnt], -1, (0, 255, 0), 3)

# Extract the region of interest (ROI) for the number plate
x, y, w, h = cv2.boundingRect(number_plate_cnt)
number_plate_roi = gray[y:y + h, x:x + w]

# Save the cropped image
cv2.imwrite('Cropped Image.png', number_plate_roi)

# Use Tesseract to convert the cropped image into a string
text = pytesseract.image_to_string(number_plate_roi, lang='eng')
print("Number Plate:", text)

# Display the final image with the detected number plate
cv2.imshow("Final Image With Number Plate Detected", image)
cv2.waitKey(0)
