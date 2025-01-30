# /// script
# requires-python = "==3.12"
# dependencies = [
#     "torch",
#     "torchaudio",
#     "torchvision",
#     "transformers",
# ]
# ///

from transformers import pipeline

pipe = pipeline("fill-mask", model="Lianglab/PharmBERT-uncased")
