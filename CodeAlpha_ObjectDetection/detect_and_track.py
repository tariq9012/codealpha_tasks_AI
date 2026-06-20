"""
CodeAlpha - Task 4: Object Detection and Tracking
Author: Tariq Jamil Khan

Real-time object detection (YOLOv8) + multi-object tracking (ByteTrack,
a SORT-family algorithm) on a webcam feed or a video file.

Usage:
    python detect_and_track.py --source 0              # webcam
    python detect_and_track.py --source path/to/video.mp4
    python detect_and_track.py --source path/to/video.mp4 --save
"""

import argparse
import cv2
from ultralytics import YOLO


def parse_args():
    parser = argparse.ArgumentParser(description="Object Detection and Tracking")
    parser.add_argument("--source", type=str, default="0",
                         help="Video source: '0' for webcam, or a path to a video file")
    parser.add_argument("--model", type=str, default="yolov8n.pt",
                         help="YOLOv8 model weights (auto-downloads if not present)")
    parser.add_argument("--conf", type=float, default=0.4,
                         help="Confidence threshold for detections")
    parser.add_argument("--tracker", type=str, default="bytetrack.yaml",
                         help="Tracker config: 'bytetrack.yaml' or 'botsort.yaml'")
    parser.add_argument("--save", action="store_true",
                         help="Save the output video to runs/track/")
    return parser.parse_args()


def main():
    args = parse_args()

    # source '0' means webcam, otherwise treat as a file path
    source = 0 if args.source == "0" else args.source

    print(f"Loading model: {args.model}")
    model = YOLO(args.model)

    print(f"Starting detection + tracking on source: {source}")
    print("Press 'q' to quit the live window.\n")

    # model.track() runs detection + tracking together.
    # 'persist=True' keeps track IDs consistent across frames.
    # 'stream=True' yields results frame-by-frame instead of loading it all in memory.
    results = model.track(
        source=source,
        conf=args.conf,
        tracker=args.tracker,
        persist=True,
        stream=True,
        save=args.save,
    )

    for result in results:
        frame = result.plot()  # draws boxes, labels, and track IDs on the frame

        cv2.imshow("CodeAlpha - Object Detection & Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
    print("\nDone. If --save was used, check the 'runs/track/' folder for the output video.")


if __name__ == "__main__":
    main()
