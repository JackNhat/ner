import argparse

parser = argparse.ArgumentParser("train.py")

parser.add_argument("--train", help="train file", required=True)
parser.add_argument("--test", help="test file")

args = parser.parse_args()