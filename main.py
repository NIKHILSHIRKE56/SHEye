from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import shutil, uuid, os
from cctv_detect import detect_from_video

app = FastAPI()

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_ext = file.filename.split(".")[-1]
    video_id = str(uuid.uuid4())
    temp_path = f"uploads/{video_id}.{file_ext}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        output_dir = detect_from_video(temp_path)
        output_path = os.path.join(output_dir, os.path.basename(temp_path))

        if os.path.exists(output_path):
            return FileResponse(output_path, media_type="video/mp4", filename="detected_output.mp4")
        else:
            return JSONResponse(status_code=500, content={"error": "Processed video not found."})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
