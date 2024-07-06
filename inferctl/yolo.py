# inferctl/yolo.py

import argparse
import cv2
from ultralytics import YOLO

def detect_objects(image_path, output_path, model_type):
    # Load the YOLO model
    model = YOLO(model_type)

    # Read the input image
    img = cv2.imread(image_path)

    # Perform object detection
    results = model(img)

    # Draw bounding boxes and labels on the image
    for result in results[0].boxes:
        x1, y1, x2, y2 = result.xyxy[0]
        conf = result.conf[0]
        cls = result.cls[0]
        label = f"{model.names[int(cls)]} {conf:.2f}"
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(img, label, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the output image
    cv2.imwrite(output_path, img)
    print(f"Output saved to {output_path}")

def detect_video(video_path, model_type):
    model = YOLO(model_type)
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for result in results[0].boxes:
            x1, y1, x2, y2 = result.xyxy[0]
            conf = result.conf[0]
            cls = result.cls[0]
            label = f"{model.names[int(cls)]} {conf:.2f}"
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def add_yolo_subparser(subparsers):
    yolo_parser = subparsers.add_parser('yolo', help='YOLO Object Detection')
    yolo_parser.add_argument('--selected_model', type=str, choices=['yolov8s.pt', 'yolov5s.pt'], help='Choose the model you want to use', required=True)
    yolo_parser.add_argument('--mode', type=str, choices=['image', 'video'], help='Mode: image or video', required=True)
    yolo_parser.add_argument('--input', type=str, help='Path to the input image or video', required=True)
    yolo_parser.add_argument('--output', type=str, help='Path to save the output image (only required for image mode)', required=False)
    yolo_parser.set_defaults(func=handle_yolo_command)

def handle_yolo_command(args):
    if args.mode == 'image':
        if not args.output:
            print("Output path is required for image mode")
            return
        detect_objects(args.input, args.output, args.selected_model)
    elif args.mode == 'video':
        detect_video(args.input, args.selected_model)
