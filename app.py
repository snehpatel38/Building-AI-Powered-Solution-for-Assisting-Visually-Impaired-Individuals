import streamlit as st
import google.generativeai as genai
import cv2
import pytesseract
import numpy as np
from PIL import Image
import io
import pyttsx3

# Configuration and Setup
genai.configure(api_key="Your GENAI API Key")
model = genai.GenerativeModel('gemini-1.5-flash')

class VisualAssistanceApp:
    def __init__(self):
        # Text-to-Speech Engine
        self.tts_engine = pyttsx3.init()
    
    def analyze_scene(self, image):
        """
        Generate comprehensive scene description using Generative AI
        
        Args:
            image (PIL.Image): Uploaded image for analysis
        
        Returns:
            str: Detailed scene description
        """
        try:
            response = model.generate_content([
                "Provide a comprehensive, detailed description of this scene. "
                "Focus on key elements, colors, objects, and spatial relationships. "
                "Describe the scene as if explaining it to someone who cannot see.", 
                image
            ])
            return response.text
        except Exception as e:
            return f"Scene analysis error: {str(e)}"
    
    def extract_text(self, image):
        """
        Extract text from image using OCR
        
        Args:
            image (PIL.Image): Image for text extraction
        
        Returns:
            str: Extracted text
        """
        # Convert PIL Image to OpenCV format
        open_cv_image = np.array(image)
        open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR
        
        # Perform OCR
        text = pytesseract.image_to_string(open_cv_image)
        return text
    
    def detect_objects(self, image):
        """
        Detect and highlight objects in the image
        
        Args:
            image (PIL.Image): Image for object detection
        
        Returns:
            tuple: Annotated image and object descriptions
        """
        # Note: Would replace with actual object detection model in production
        response = model.generate_content([
            "Identify and list all distinct objects in this image. "
            "Provide their locations and any notable characteristics.", 
            image
        ])
        return response.text
    
    def personalized_task_assistance(self, image):
        """
        Provide context-specific, task-oriented guidance based on image content
        
        Args:
            image (PIL.Image): Uploaded image for task analysis
        
        Returns:
            dict: Personalized task recommendations and insights
        """
        try:
            # Prompt for detailed, task-oriented analysis
            response = model.generate_content([
                "Analyze this image and provide personalized, practical guidance. "
                "Consider the following aspects:\n"
                "1. Identify specific objects or items in the image\n"
                "2. Suggest potential daily tasks or activities related to these objects\n"
                "3. Provide step-by-step guidance or safety tips\n"
                "4. Highlight any potential challenges for a visually impaired person\n"
                "5. Offer practical advice for interaction or navigation\n"
                "Provide a comprehensive, helpful, and empathetic response.", 
                image
            ])
            
            # Parse the response into a structured format
            task_insights = {
                "identified_objects": [],
                "potential_tasks": [],
                "safety_tips": [],
                "navigation_advice": []
            }
            
            # Basic parsing of the generated text (could be enhanced with more advanced NLP)
            response_text = response.text
            
            # Simple parsing to extract different types of information
            if "Identified Objects:" in response_text:
                task_insights["identified_objects"] = response_text.split("Identified Objects:")[1].split("Potential Tasks:")[0].strip().split("\n")
            
            if "Potential Tasks:" in response_text:
                task_insights["potential_tasks"] = response_text.split("Potential Tasks:")[1].split("Safety Tips:")[0].strip().split("\n")
            
            if "Safety Tips:" in response_text:
                task_insights["safety_tips"] = response_text.split("Safety Tips:")[1].split("Navigation Advice:")[0].strip().split("\n")
            
            if "Navigation Advice:" in response_text:
                task_insights["navigation_advice"] = response_text.split("Navigation Advice:")[1].strip().split("\n")
            
            return task_insights
        
        except Exception as e:
            return {"error": f"Task assistance analysis error: {str(e)}"}
    
    def speak_text(self, text):
        """
        Convert text to speech
        
        Args:
            text (str): Text to be spoken
        """
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

def main():
    st.title("🌟 Visual Assistance AI")
    st.subheader("Empowering Vision through Artificial Intelligence")
    
    # Initialize the application
    app = VisualAssistanceApp()
    
    # Image Upload
    uploaded_image = st.file_uploader(
        "Upload an Image", 
        type=['png', 'jpg', 'jpeg'], 
        help="Upload an image for comprehensive analysis"
    )
    
    # Only proceed if an image has been uploaded
    if uploaded_image is not None:
        # Convert uploaded file to PIL Image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Analyze Scene
        st.subheader("🔍 Scene Understanding")
        scene_description = app.analyze_scene(image)
        st.write(scene_description)
        
        # Text Extraction and Speech
        st.subheader("📝 Text Extraction")
        extracted_text = app.extract_text(image)
        st.text_area("Extracted Text", extracted_text, height=100)
        
        if st.button("🔊 Read Extracted Text"):
            app.speak_text(extracted_text)
        
        # Object Detection
        st.subheader("🚧 Object Detection")
        object_details = app.detect_objects(image)
        st.write(object_details)
        
        # Personalized Task Assistance
        st.subheader("🤝 Personalized Task Assistance")
        task_insights = app.personalized_task_assistance(image)
        
        if "error" in task_insights:
            st.error(task_insights["error"])
        else:
            # Display task insights in an organized manner
            if task_insights["identified_objects"]:
                st.markdown("**Identified Objects:**")
                for obj in task_insights["identified_objects"]:
                    st.text(obj)
            
            if task_insights["potential_tasks"]:
                st.markdown("**Potential Tasks:**")
                for task in task_insights["potential_tasks"]:
                    st.text(task)
            
            if task_insights["safety_tips"]:
                st.markdown("**Safety Tips:**")
                for tip in task_insights["safety_tips"]:
                    st.text(tip)
            
            if task_insights["navigation_advice"]:
                st.markdown("**Navigation Advice:**")
                for advice in task_insights["navigation_advice"]:
                    st.text(advice)

if __name__ == "__main__":
    main()