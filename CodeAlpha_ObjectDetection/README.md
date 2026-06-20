# 🎯 Object Detection and Tracking — CodeAlpha AI Internship (Task 4)

Real-time object detection and multi-object tracking using YOLOv8 and
ByteTrack (a SORT-family tracking algorithm), running on a webcam feed
or a video file.

## ✨ Features
- Real-time video input from webcam **or** a video file (OpenCV)
- Object detection using **YOLOv8** (pre-trained on the COCO dataset — 80 object classes)
- Each frame is processed and bounding boxes + class labels are drawn
- Multi-object tracking with **ByteTrack** (SORT-family algorithm) — each
  object gets a persistent ID as it moves across frames
- Optional: save the annotated output video to disk

## 🛠 Tech Stack
- **Detection model:** YOLOv8 (via the `ultralytics` library)
- **Tracking:** ByteTrack (`bytetrack.yaml`, built into `ultralytics`) —
  same SORT-family lineage as classic SORT/Deep SORT
- **Video handling:** OpenCV

## 🚀 How to Run

1. Clone this repo and move into the folder:
   ```bash
   git clone <your-repo-link>
   cd CodeAlpha_ObjectDetection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(First run will also auto-download the YOLOv8 nano weights, `yolov8n.pt`, ~6MB)*

3. Run on your webcam:
   ```bash
   python detect_and_track.py --source 0
   ```

   Or run on a video file:
   ```bash
   python detect_and_track.py --source path/to/video.mp4 --save
   ```

4. Press **`q`** to quit the live preview window. If `--save` was used,
   check the `runs/track/` folder for the output video.

## ⚙️ Optional Arguments
| Argument     | Default            | Description                                  |
|--------------|---------------------|-----------------------------------------------|
| `--source`   | `0` (webcam)        | `0` for webcam, or a path to a video file     |
| `--model`    | `yolov8n.pt`         | YOLOv8 weights (n/s/m/l/x — bigger = more accurate, slower) |
| `--conf`     | `0.4`                 | Minimum confidence to keep a detection        |
| `--tracker`  | `bytetrack.yaml`      | Tracking algorithm: `bytetrack.yaml` or `botsort.yaml` |
| `--save`     | off                   | Save the annotated output video               |

## 📂 Project Structure
```
CodeAlpha_ObjectDetection/
├── detect_and_track.py   # Main detection + tracking script
└── requirements.txt
```

## 📌 Task Requirements Covered
- [x] Real-time video input (webcam or video file) via OpenCV
- [x] Pre-trained detection model (YOLOv8)
- [x] Per-frame detection with bounding boxes
- [x] Object tracking with a SORT-family algorithm (ByteTrack)
- [x] Labels and tracking IDs displayed in real time

---
**Internship:** CodeAlpha — Artificial Intelligence
**Author:** Tariq Jamil Khan
