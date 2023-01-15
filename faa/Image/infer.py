#!/usr/bin/env python
import os
import random
from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt
import torch
from PIL import Image
from torchvision import transforms

from .gan_module import Generator
parser = ArgumentParser()
parser.add_argument(
    '--image_dir', default='/Applications/XAMPP/xamppfiles/htdocs/php1', help='The image directory')


@torch.no_grad()

def make_image_older(image, n): # gdzies do 35 linii
    args = parser.parse_args()
    image_paths = [os.path.join(args.image_dir, x) for x in os.listdir(args.image_dir) if
                   x.endswith('.png') or x.endswith('.jpg')]
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    transTensor = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    img = image.convert('RGB')
    img = transTensor(img).unsqueeze(0)
    aged_face = model(img)
    for i in range(n-1):
        aged_face = model(aged_face)
    aged_face = (aged_face.squeeze().permute(1, 2, 0).detach().numpy() + 1.0) / 2.0

    return aged_face

def display_image(image):
    plt.imshow(image)
    plt.savefig("/Applications/XAMPP/xamppfiles/htdocs/php1/galeria_po/zdj.png")


if __name__ == '__main__':
    img = Image.open("zdj/alan.jpg")

    img = make_image_older(img, 3)