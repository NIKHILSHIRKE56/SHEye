import streamlit as st
import json
import os
from datetime import datetime
from PIL import Image

LOG_FILE = "dashboard/incident_log.json"

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="SHEye Dashboard", layout="wide")
    st.title("👁️ SHEye Real-Time Incident Dashboard")

    logs = load_logs()

    if not logs:
        st.warning("No incidents logged yet.")
        return

    for log in reversed(logs):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"### ⚠️ {log['event']}")
            st.markdown(f"**Time:** {log['timestamp']}")
            if os.path.exists(log["video_path"]):
                st.video(log["video_path"])

        with col2:
            if os.path.exists(log["snapshot"]):
                st.image(log["snapshot"], caption="Detection Snapshot", use_column_width=True)

        st.markdown("---")

if __name__ == "__main__":
    main()
