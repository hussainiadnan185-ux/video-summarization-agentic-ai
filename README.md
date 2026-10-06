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
