import os
import time

from google import genai
from lfx.custom.custom_component.component import Component
from lfx.io import MessageTextInput, Output, SecretStrInput, StrInput
from lfx.schema.message import Message


class VideoSummarizerComponent(Component):
    display_name = "Video Summarizer"
    description = "Summarize a local video with Gemini."
    documentation = "https://docs.langflow.org/components-custom-components"
    icon = "file-video"
    name = "VideoSummarizerComponent"

    inputs = [
        StrInput(
            name="video_path",
            display_name="Video File Path",
            info="Absolute path to a local video file.",
            value="",
            required=True,
        ),
        SecretStrInput(
            name="api_key",
            display_name="Google Gemini API Key",
            info="Your Gemini API key.",
            required=True,
        ),
        StrInput(
            name="model_name",
            display_name="Gemini Model",
            value="gemini-3.5-flash-lite",
            required=True,
        ),
        MessageTextInput(
            name="user_request",
            display_name="Request (optional)",
            info="Connect Chat Input here, or leave empty.",
            required=False,
        ),
    ]

    outputs = [
        Output(
            display_name="Summary",
            name="summary",
            method="summarize_video",
        ),
    ]

    def _retry(self, func, attempts=5):
        for i in range(attempts):
            try:
                return func()
            except Exception as e:
                busy = getattr(e, "code", None) == 503 or "503" in str(e)

                if not busy or i == attempts - 1:
                    raise

                time.sleep(10 * (2 ** i))

    def summarize_video(self) -> Message:
        video_path = self.video_path.strip()

        if not video_path:
            raise ValueError("Please enter a video file path.")

        if not os.path.isfile(video_path):
            raise ValueError(f"Video file not found: {video_path}")

        key = self.api_key

        if hasattr(key, "get_secret_value"):
            key = key.get_secret_value()

        if not key:
            raise ValueError("Please provide your Gemini API key.")

        client = genai.Client(api_key=key)

        # Upload the video
        try:
            uploaded_file = client.files.upload(file=video_path)

        except Exception as e:
            raise RuntimeError(
                f"VIDEO UPLOAD FAILED: {type(e).__name__}: {e}"
            ) from e

        # Wait for Gemini to process the video
        start_time = time.time()
        timeout_seconds = 600

        while True:
            try:
                uploaded_file = client.files.get(
                    name=uploaded_file.name
                )

            except Exception as e:
                raise RuntimeError(
                    f"VIDEO STATUS CHECK FAILED: {type(e).__name__}: {e}"
                ) from e

            state = str(uploaded_file.state).upper()

            if "ACTIVE" in state:
                break

            if "FAILED" in state:
                raise RuntimeError(
                    "Gemini failed while processing the uploaded video."
                )

            if time.time() - start_time > timeout_seconds:
                raise TimeoutError(
                    "Video processing timed out after 10 minutes."
                )

            time.sleep(2)

        # Build the prompt
        extra = str(self.user_request or "").strip()

        if extra:
            prompt = f"""
Answer the user's request using only the content of this video.

User request:
{extra}

Follow the user's request exactly.
Do not provide additional information that was not requested.
Do not invent facts.
"""

        else:
            prompt = """
Summarize this video accurately using only its content.

Organize the answer into:

1. Overview
2. Main Topics
3. Key Points
4. Important Details
5. Key Takeaways

Use clear headings and bullet points.
Do not invent facts.
"""

        # Ask Gemini to analyze the video
        try:
            interaction = self._retry(
                lambda: client.interactions.create(
                    model=self.model_name,
                    input=[
                        {
                            "type": "video",
                            "uri": uploaded_file.uri,
                            "mime_type": uploaded_file.mime_type,
                        },
                        {
                            "type": "text",
                            "text": prompt,
                        },
                    ],
                )
            )

        except Exception as e:
            raise RuntimeError(
                f"INTERACTIONS VIDEO SUMMARY FAILED: {type(e).__name__}: {e}"
            ) from e

        summary = interaction.output_text

        if not summary:
            raise RuntimeError(
                "Gemini returned an empty video summary."
            )

        self.status = summary

        return Message(text=summary)