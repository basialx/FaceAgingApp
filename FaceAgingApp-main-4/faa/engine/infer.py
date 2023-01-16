import os
import random
from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt
import torch
from PIL import Image
from torchvision import transforms

from gan_module import Generator
parser = ArgumentParser()
parser.add_argument(
    '--image_dir', default='moje', help='The image directory')


@torch.no_grad()

def make_image_older(image, n): # gdzies do 35 linii
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    transTensor = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    img = image.convert('RGB')  # tutaj gdzies bedzie szlo  zdjecie z kamery
    img = transTensor(img).unsqueeze(0)
    aged_face = model(img)
    for i in range(n-1):
        aged_face = model(aged_face)
    aged_face = (aged_face.squeeze().permute(1, 2, 0).detach().numpy() + 1.0) / 2.0

    return aged_face

def display_image(image):
    plt.imshow(image)
    plt.show()


if __name__ == '__main__':
    img = Image.open("zdj/alan.jpg")

    img = make_image_older(img, 3)
    display_image(img)

