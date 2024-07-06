
import argparse
from inferctl.yolo import add_yolo_subparser
from inferctl.resnet import add_resnet_subparser

def main():
    parser = argparse.ArgumentParser(description="Inference CLI App")
    subparsers = parser.add_subparsers(dest='command')

    # Add subparsers for different models
    add_yolo_subparser(subparsers)
    add_resnet_subparser(subparsers)

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()