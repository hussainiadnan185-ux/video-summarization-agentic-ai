# 🎬 Video AI Summarizer

An AI-powered video summarization application built with **Streamlit, Langflow, and Google Gemini**.

Users can upload a video and either:

- Generate a structured summary of the video.
- Enter a custom request to analyze the video in a specific way.

## 🚀 Features

- Upload video files in MP4, MOV, AVI, MPEG, and MPG formats
- Preview uploaded videos in the Streamlit interface
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
```- Python
- Streamlit
- Langflow
- Google Gemini
- Google GenAI SDK
- Requests
📁 Project Structure
### 🛠️ Technologies

- Python
- Streamlit
- Langflow
- Google Gemini
- Google GenAI SDK
- Requests

### 📁 Project Structure

```text
video-summarization-agentic-ai/
│
├── app.py
├── Video-Summarizer.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── custom-component/
│   └── video_summarizer.py
│
└── .streamlit/
    └── secrets.toml.example
```

### ⚙️ Prerequisites

Before running the application, make sure you have:

- Python 3.12
- Langflow
- A Google Gemini API key
- A Langflow API key

### 🔧 Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/hussainiadnan185-ux/video-summarization-agentic-ai.git
cd video-summarization-agentic-ai
```

#### 2. Set Up Langflow

Install and configure Langflow in a Python 3.12 environment.

Import the included Langflow workflow:

```text
Video-Summarizer.json
```

into Langflow.

Configure the **Video Summarizer** component with your own Google Gemini API key.

#### 3. Configure Streamlit

Create the following file:

```text
.streamlit/secrets.toml
```

Use the structure shown in:

```text
.streamlit/secrets.toml.example
```

Add your:

- Local Langflow URL
- Langflow Flow ID
- Langflow API key
- Video Summarizer component ID

**Never commit `secrets.toml` to GitHub.**

#### 4. Install Dependencies

Install the required Streamlit dependencies:

```bash
pip install -r requirements.txt
```

#### 5. Run Langflow

Open a terminal in the project directory and run:

```bash
langflow run
```

Langflow will run at:

```text
http://localhost:7860
```

Keep this terminal running.

#### 6. Run Streamlit

Open another terminal in the project directory and run:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

### 🧪 Example Requests

The application supports both standard summaries and custom requests.

#### Standard Summary

Leave the request field empty.

The application generates a structured summary containing:

- Overview
- Main Topics
- Key Points
- Important Details
- Key Takeaways

#### Custom Request

Users can enter a specific request to control the type of analysis performed.

Examples:

```text
Who is the person in this video? Answer only that.
```

```text
List only the main topics discussed.
```

```text
Summarize this video in 5 bullet points.
```

When a custom request is provided, it takes priority over the default summary format.

### 🔐 Security

API keys and local secrets are intentionally excluded from the repository.

The following files should never be committed:

```text
.streamlit/secrets.toml
.env
```

Temporary uploaded videos and Python virtual environments are also excluded through `.gitignore`.

### ⚠️ Limitations

- Langflow must be running locally for the Streamlit application to work.
- Video processing time depends on video length and Gemini processing.
- Gemini free-tier usage limits apply.
- The application is currently designed for local use.
- Uploaded videos are temporarily stored during processing and deleted afterward.
