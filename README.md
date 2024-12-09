
# 🌟 Visual Assistance AI

Empowering Vision through Artificial Intelligence.

## **Overview**
Visual Assistance AI is a powerful application designed to assist visually impaired individuals by analyzing images and providing detailed insights through generative AI, text extraction, and personalized task guidance.

## **Features**
- **Scene Understanding**: Generates comprehensive scene descriptions using Google Generative AI.
- **Text Extraction**: Extracts text from images using Tesseract OCR.
- **Object Detection**: Identifies objects and their characteristics in images.
- **Task Assistance**: Offers practical, context-specific advice for navigation and interaction.
- **Text-to-Speech**: Converts text into speech for auditory assistance.

## **Technologies Used**
- **Streamlit**: Interactive web app framework.
- **Google Generative AI**: For detailed scene analysis and object detection.
- **Tesseract OCR**: Text extraction from images.
- **OpenCV**: Image processing.
- **Pyttsx3**: Text-to-speech conversion.
- **Python**: Core programming language.

## **Set Up (Only important)**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Additional dependencies:
   - Install the Py-Tesseract from https://github.com/UB-Mannheim/tesseract/wiki
     
3. Set up Google Generative AI API key:
   - Replace `YOUR_API_KEY` in the code with your API key.

## 🚀 **How It Works**
1. Upload an image in the supported formats (PNG, JPG, JPEG).
2. View the generated scene analysis, extracted text, and identified objects.
3. Listen to the extracted text using the text-to-speech feature.
4. Get personalized task recommendations based on the uploaded image.
