import streamlit as st
import os
from PIL import Image
from model_helper import predict

st.title("Vehicle Damage Detection")
st.write("Upload an image of a vehicle to detect damage")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Save temporarily if needed for model processing
        image_path = "temp_file.jpg"
        image.save(image_path)
        
        # Add a button to trigger detection
        if st.button("Detect Damage"):
            with st.spinner("Analyzing image..."):
                # Your model prediction code here
                prediction = predict(image_path)
                # Placeholder result
                st.success("Analysis Complete!")
                st.info(f"Predicted Class is {prediction}")
                
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
    finally:
        # Clean up temporary file
        if 'image_path' in locals() and os.path.exists(image_path):
            os.remove(image_path)

# Add some instructions
st.sidebar.header("Instructions")
st.sidebar.write("1. Upload a clear image of the vehicle")
st.sidebar.write("2. Supported formats: JPG, JPEG, PNG")
st.sidebar.write("3. Click 'Detect Damage' to analyze")