from ultralytics import YOLO
import os

def detect_from_video(video_path: str, save_dir: str = "runs/detect", model_path: str = "yolov8n.pt") -> str:
    # Load the YOLOv8 model
    model = YOLO(model_path)

    # Run detection
    results = model.predict(
        source=video_path,
        save=True,
        save_txt=True,
        conf=0.3,
        project=save_dir,
        name="cctv_output",
        exist_ok=True
    )

    # Return the path to the saved output directory
    return os.path.join(save_dir, "cctv_output")
