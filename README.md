# 🎬 Video AI Summarizer

An AI-powered video summarization application built with **Streamlit, Langflow, and Google Gemini**.

Users can upload a video and either:
- Get a structured summary of the video.
- Enter a custom request to ask Gemini to analyze the video in a specific way.

## 🚀 Features

- Upload video files in MP4, MOV, AVI, MPEG, and MPG formats
- Video preview in the Streamlit interface
- AI-powered video analysis using Google Gemini
- Structured video summaries
- Custom requests for specific video analysis
- Temporary video file handling
- Download generated summaries as Markdown files

## 🏗️ Architecture

```text
Streamlit
    ↓
Langflow
    ↓
Gemini File API
    ↓
Gemini Interactions API
    ↓
Video Analysis / Summary
    ↓
Streamlit

## 🛠️ Technologies
- Python
- Streamlit
- Langflow
- Google Gemini
- Google GenAI SDK
- Requests
## 📁 Project Structure
video-summarization-agentic-ai/
│
├── app.py
├── Video-Summarizer.json
├── requirements.txt
├── .gitignore
│
├── custom-component/
│   └── video_summarizer.py
│
├── .streamlit/
│   ├── secrets.toml
│   └── secrets.toml.example
│
├── screenshots/
│   ├── langflow-workflow.png
│   ├── streamlit-upload.png
│   └── summary-output.png
│
└── uploads/

## ⚙️ Prerequisites
- Python 3.12
- Langflow
- A Google Gemini API key
- A Langflow API key
## 🔧 Setup
# 1. Clone the repository
git clone <your-github-repository-url>
cd video-summarization-agentic-ai
# 2. Create the Langflow environment
Install and configure Langflow in a Python 3.12 environment.
Import the included:
Video-Summarizer.json

flow into Langflow.
Add your own Gemini API key to the Video Summarizer component.
# 3. Configure Streamlit
Create:
.streamlit/secrets.toml

Use the structure shown in:
.streamlit/secrets.toml.example

Add your local Langflow URL, Flow ID, Langflow API key, and Video Summarizer component ID.
Never commit secrets.toml to GitHub.
# 4. Install Streamlit dependencies
pip install -r requirements.txt

# 5. Run Langflow
In one terminal:
langflow run

Langflow will run at:
http://localhost:7860

# 6. Run Streamlit
In another terminal:
streamlit run app.py

The Streamlit application will open in your browser.
## 🧪 Example Requests
The application supports both standard summaries and custom requests.
Standard summary
Leave the request field empty.
The application generates a structured summary containing:
- Overview
- Main Topics
- Key Points
- Important Details
- Key Takeaways
Custom request
Examples:
Who is the person in this video? Answer only that.

List only the main topics discussed.

Summarize this video in 5 bullet points.

The custom request takes priority over the default summary format.
## 🔐 Security
API keys and local secrets are intentionally excluded from the repository.
The following should never be committed:
.streamlit/secrets.toml
.env

Temporary uploaded videos and Python virtual environments are also excluded through .gitignore.
## ⚠️ Limitations
- Langflow must be running locally for the Streamlit application to work.
- Video processing time depends on video length and Gemini processing.
- Gemini free-tier usage limits apply.
- The application is currently designed for local use.
- Uploaded videos are temporarily stored during processing and deleted afterward.
