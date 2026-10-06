import uuid
from pathlib import Path

import requests
import streamlit as st

st.set_page_config(page_title="Video AI Summarizer", page_icon="🎬")

st.title("🎬 Video AI Summarizer")
st.caption("Powered by Gemini 3.5 Flash Lite")


def get_secret(name, default=None):
    try:
        return st.secrets[name]
    except Exception:
        return default


LANGFLOW_URL = get_secret("LANGFLOW_URL", "http://localhost:7860").rstrip("/")
FLOW_ID = get_secret("LANGFLOW_FLOW_ID")
API_KEY = get_secret("LANGFLOW_API_KEY")
COMPONENT_ID = get_secret("LANGFLOW_COMPONENT_ID")

if not (FLOW_ID and API_KEY and COMPONENT_ID):
    st.error("Missing settings. Fill in .streamlit/secrets.toml.")
    st.stop()


UPLOAD_DIR = Path(__file__).resolve().parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


if "summary" not in st.session_state:
    st.session_state.summary = None


video = st.file_uploader(
    "Upload a video",
    type=["mp4", "mov", "avi", "mpeg", "mpg"],
)

if video:
    st.video(video)


user_request = st.text_input(
    "Your request (optional)",
    placeholder="Summarize in 5 bullet points",
)


if st.button("Summarize Video"):
    if video is None:
        st.warning("Please upload a video first.")

    else:
        saved_path = (
            UPLOAD_DIR
            / f"{uuid.uuid4().hex}{Path(video.name).suffix}"
        )

        saved_path.write_bytes(video.getbuffer())

        payload = {
            "input_value": user_request.strip() or "Summarize this video.",
            "input_type": "chat",
            "output_type": "chat",
            "tweaks": {
                COMPONENT_ID: {
                    "video_path": str(saved_path)
                }
            },
        }

        headers = {
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
        }

        try:
            with st.spinner("Summarizing... this can take a few minutes."):
                response = requests.post(
                    f"{LANGFLOW_URL}/api/v1/run/{FLOW_ID}?stream=false",
                    headers=headers,
                    json=payload,
                    timeout=900,
                )

            if response.status_code != 200:
                st.error(f"Langflow returned HTTP {response.status_code}")
                st.code(response.text[:2000])

            else:
                data = response.json()

                try:
                    summary = (
                        data["outputs"][0]["outputs"][0]
                        ["results"]["message"]["text"]
                    )
                except (KeyError, IndexError, TypeError):
                    summary = None

                if summary:
                    st.session_state.summary = summary
                else:
                    st.error(
                        "Could not find the summary in Langflow's response."
                    )
                    with st.expander("Raw response"):
                        st.json(data)

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot reach Langflow. Is 'langflow run' still running?"
            )

        except requests.exceptions.Timeout:
            st.error("Timed out waiting for Langflow.")

        finally:
            saved_path.unlink(missing_ok=True)


if st.session_state.summary:
    st.subheader("Summary")
    st.markdown(st.session_state.summary)

    st.download_button(
        "Download summary (.md)",
        st.session_state.summary,
        file_name="summary.md",
    )