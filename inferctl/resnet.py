# inferctl/resnet.py

import argparse
import torch
from torchvision import models, transforms
from PIL import Image

def classify_img(image_path):
    # Load the pretrained ResNet model
    model = models.resnet50(pretrained=True)
    model.eval()  # Set the model to evaluation mode

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert('RGB')
    image = preprocess(image)
    image = image.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        output = model(image)

    # Get the predicted class
    _, predicted_class = torch.max(output, 1)
    print(f'Predicted class: {predicted_class.item()}')

def add_resnet_subparser(subparsers):
    resnet_parser = subparsers.add_parser('resnet', help='Image Classification with ResNet')
    resnet_parser.add_argument('--input', type=str, help='Path to the input image', required=True)
    resnet_parser.set_defaults(func=handle_resnet_command)

def handle_resnet_command(args):
    classify_img(args.input)
