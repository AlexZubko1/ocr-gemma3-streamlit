# Gemma OCR Assistant

A Streamlit application that leverages the multimodal capabilities of Gemma 4B to perform OCR and image analysis. The application runs locally and connects to an Ollama instance to process images and extract text.

## Features

- Image upload and processing
- Custom prompt input for tailored analysis
- Clean and intuitive user interface
- Real-time text extraction and analysis
- Detailed explanations of image content

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Gemma3 4B model pulled in Ollama

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running with Gemma3 4B model:
```bash
ollama pull gemma3:4b
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload an image containing text

4. (Optional) Enter a custom prompt to guide the analysis

5. Click "Analyze Image" to process

## Custom Prompts

You can customize the analysis by providing specific prompts. Example prompts:

- "Extract and list all text from the image"
- "Describe the layout and formatting of text"
- "Analyze the context and meaning of the text"
- "Focus on specific sections or types of text"

## Notes

- The application expects Ollama to be running on port 11434 (default)
- Supported image formats: PNG, JPG, JPEG
- For best results, ensure images are clear and text is readable 