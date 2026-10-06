# Video AI Summarizer

## Overview

This project implements an AI-powered video summarization application using **Streamlit, Langflow, and Google Gemini**. The application allows users to upload a video and generate an AI-based summary or provide a custom request to analyze the video in a specific way.

The project combines a **Streamlit frontend** with a **Langflow workflow** and Google's Gemini video analysis capabilities. Videos are uploaded to the Gemini File API and analyzed using the Gemini Interactions API.

Instead of relying on manual video review, the application provides an interactive workflow for extracting important information and generating structured responses from video content.

---

## Execution Environment

- Language: Python
- Frontend: Streamlit
- Workflow Orchestration: Langflow
- AI Model: Google Gemini
- Google AI SDK: Google GenAI SDK
- HTTP Client: Requests
- Execution Mode: Local application

The application is designed to run locally, with Streamlit providing the user interface and Langflow handling the video summarization workflow.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/hussainiadnan185-ux/video-summarization-agentic-ai.git
cd video-summarization-agentic-ai
```

2. Make sure Python 3.12 is installed.

3. Install and configure Langflow in a Python 3.12 environment.

4. Import the included Langflow workflow:

```text
Video-Summarizer.json
```

5. Configure the **Video Summarizer** component with your own Google Gemini API key.

6. Create the Streamlit secrets file:

```text
.streamlit/secrets.toml
```

7. Use the structure provided in:

```text
.streamlit/secrets.toml.example
```

8. Add the required local configuration:

- Langflow URL
- Langflow Flow ID
- Langflow API key
- Video Summarizer component ID

9. Install the required dependencies:

```bash
pip install -r requirements.txt
```

10. Start Langflow in one terminal:

```bash
langflow run
```

Langflow will run at:

```text
http://localhost:7860
```

11. Start Streamlit in another terminal:

```bash
streamlit run app.py
```

12. Upload a video through the Streamlit interface and provide an optional custom request.

The generated summary will be displayed in the application and can also be downloaded as a Markdown file.

---

## Supported Video Formats

The application supports the following video formats:

- MP4
- MOV
- AVI
- MPEG
- MPG

Uploaded videos are temporarily stored locally during processing.

---

## Video Summarization Workflow

The application follows an end-to-end video analysis workflow:

1. User uploads a video through the Streamlit interface.
2. Streamlit temporarily saves the uploaded video locally.
3. Streamlit sends the local video path to the Langflow workflow.
4. Langflow passes the video path to the custom **Video Summarizer** component.
5. The component uploads the video to the Gemini File API.
6. The application waits for Gemini to finish processing the uploaded video.
7. The Gemini Interactions API analyzes the video.
8. A structured summary or custom response is generated.
9. Langflow returns the generated response to Streamlit.
10. Streamlit displays the result to the user.
11. The temporary uploaded video is deleted after processing.

---

## Default Summary

When no custom request is provided, the application generates a structured summary containing:

- Overview
- Main Topics
- Key Points
- Important Details
- Key Takeaways

The generated summary is based only on the content of the uploaded video.

---

## Custom Video Analysis

The application also supports user-defined requests.

Examples include:

```text
Who is the person in this video? Answer only that.
```

```text
List only the main topics discussed.
```

```text
Summarize this video in 5 bullet points.
```

When a custom request is provided, it takes priority over the default structured summary format.

This allows the application to be used for more specific video analysis tasks rather than only general summarization.

---

## Langflow Workflow

The Langflow workflow consists of:

```text
Chat Input
     ↓
Video Summarizer
     ↓
Chat Output
```

The custom **Video Summarizer** component handles:

- Local video file validation
- Gemini API authentication
- Video upload
- Video processing status checks
- Gemini video analysis
- Retry handling for temporary service availability errors
- Summary generation
- Returning the result as a Langflow message

---

## AI Model

The application uses:

```text
gemini-3.5-flash-lite
```

The model is used for analyzing uploaded video content and generating summaries or responses based on user requests.

The implementation uses the **Google GenAI SDK** and the Gemini File API together with the Gemini Interactions API.

---

## Project Structure

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

### Main Files

- `app.py`  
  Streamlit frontend responsible for video upload, user requests, communication with Langflow, and displaying generated summaries.

- `custom-component/video_summarizer.py`  
  Custom Langflow component responsible for uploading videos to Gemini, waiting for video processing, executing the video analysis request, and returning the generated response.

- `Video-Summarizer.json`  
  Exported Langflow workflow that can be imported into a Langflow installation.

- `requirements.txt`  
  Contains the Python dependencies required by the Streamlit application.

- `.streamlit/secrets.toml.example`  
  Example configuration file showing the required local secrets and configuration values.

- `.gitignore`  
  Prevents sensitive files, virtual environments, temporary uploads, and other local files from being committed.

---

## Outputs

### Generated Summary

The application displays the generated video analysis directly in the Streamlit interface.

For standard requests, the output contains:

- Overview
- Main Topics
- Key Points
- Important Details
- Key Takeaways

For custom requests, the output follows the user's requested format.

### Downloadable Output

Generated summaries can be downloaded as:

```text
summary.md
```

This allows the generated analysis to be saved and used outside the application.

---

## Security

API keys and local secrets are intentionally excluded from the repository.

The following files should never be committed:

```text
.streamlit/secrets.toml
.env
```

The actual Streamlit secrets file is excluded through `.gitignore`.

Temporary uploaded videos are also excluded from version control.

The repository contains only the example secrets configuration:

```text
.streamlit/secrets.toml.example
```

No actual API keys are included in the repository.

---

## Key Features

- AI-powered video summarization
- Video preview before processing
- Multiple video format support
- Custom video analysis requests
- Langflow-based workflow orchestration
- Gemini File API integration
- Gemini Interactions API integration
- Retry handling for temporary Gemini service errors
- Structured summary generation
- Markdown summary download
- Temporary video file cleanup
- Local secret management

---

## Limitations

- Langflow must be running locally for the Streamlit application to work.
- The application is currently designed for local use.
- Video processing time depends on video length and Gemini processing time.
- Gemini free-tier usage limits apply.
- Uploaded videos are temporarily stored locally during processing.
- Video processing can take several minutes depending on the uploaded video and service availability.
- The application currently relies on the configured Gemini model and API availability.

---

## Future Improvements

Potential improvements include:

- Add support for additional video formats.
- Add configurable summary styles and lengths.
- Add timestamps for important events or topics.
- Add support for extracting key moments from videos.
- Improve the user interface and progress indicators.
- Add persistent storage for generated summaries.
- Add automated evaluation of summary quality.
- Support additional Gemini models.
- Deploy the application for remote access.

---

## Tools & Technologies

- **Python** — Application development and backend logic
- **Streamlit** — Interactive web interface
- **Langflow** — Visual workflow orchestration
- **Google Gemini** — AI-powered video analysis and summarization
- **Google GenAI SDK** — Gemini API integration
- **Requests** — Communication between Streamlit and Langflow
- **Jupyter / VS Code** — Development and testing environment

---

