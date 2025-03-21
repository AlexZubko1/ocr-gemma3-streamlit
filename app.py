import streamlit as st
from PIL import Image
import io
import time
from ollama_utils import OllamaClient

# Page configuration
st.set_page_config(
    page_title="Gemma OCR Assistant",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .success-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        margin: 1rem 0;
    }
    .error-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        color: #721c24;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Ollama client
@st.cache_resource
def get_ollama_client(base_url):
    return OllamaClient(base_url=base_url)

# Header
st.title("🔍 Experimental OCR Assistant")
st.markdown("""
This application uses Gemma 3B's multimodal capabilities to analyze images and extract text.
Upload an image and optionally provide a custom prompt to guide the analysis.
""")

# Sidebar with instructions
with st.sidebar:
    st.header("📝 Instructions")
    st.markdown("""
    1. Upload an image containing text
    2. (Optional) Provide a custom prompt
    3. Click 'Analyze Image' to process
    
    **Example Prompts:**
    - Extract and list all text from the image
    - Describe the layout and formatting of text
    - Analyze the context and meaning of the text
    """)
    
    # Ollama server configuration
    st.header("⚙️ Configuration")
    ollama_url = st.text_input(
        "Ollama Server URL", 
        value="http://localhost:11434",
        help="URL of the Ollama server. Change this if Ollama is running on a different machine."
    )

# Initialize the client with the specified URL
client = get_ollama_client(ollama_url)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Image Upload")
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading image: {str(e)}")
            image = None
    
    custom_prompt = st.text_area(
        "Custom Prompt (optional)",
        placeholder="Enter a custom prompt to guide the analysis...",
        help="Leave empty to use the default prompt for general text extraction and analysis."
    )

with col2:
    st.subheader("Analysis Results")
    if uploaded_file is not None and st.button("Analyze Image"):
        with st.spinner("Processing image..."):
            try:
                # Start timer
                start_time = time.time()
                
                # Process the image
                result = client.analyze_image(image, custom_prompt)
                
                # Calculate processing time
                processing_time = time.time() - start_time
                
                # Display results
                st.markdown("### Results:")
                st.write(result)
                
                # Display processing time
                st.info(f"⏱️ Processing time: {processing_time:.2f} seconds")
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")

# Footer
st.markdown("---")
st.markdown("*Powered by Gemma 3B and Ollama*")
