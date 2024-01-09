# License Plate Recognition with OpenCV and Tesseract OCR

This project implements License Plate Recognition (LPR) using OpenCV and the Tesseract OCR engine. It detects license plates in images, extracts the region of interest, and uses Tesseract for character recognition.

## Introduction

Welcome to the License Plate Recognition project! This open-source solution leverages computer vision techniques to identify and extract license plate information from images using OpenCV. Tesseract OCR is employed for accurate text recognition within the detected license plate region.

## Features

- License Plate Detection: Utilizes contour detection to identify potential license plate regions.
- Character Recognition: Employs Tesseract OCR for accurate character recognition on the extracted license plate region.
- Image Preprocessing: Includes grayscale conversion, bilateral filtering for noise reduction, and Canny edge detection.
- User-friendly: Provides an easy-to-understand Python script for license plate recognition.

## Requirements

Ensure you have the following dependencies installed:
- OpenCV
- imutils
- pytesseract
- Tesseract OCR (Make sure to set the path to the Tesseract executable in the script)
