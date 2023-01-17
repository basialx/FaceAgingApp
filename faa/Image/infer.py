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

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

@torch.no_grad()

def make_image_older(image): # gdzies do 35 linii
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('Image/pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    transTensor = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    i = Image.open(image)
    img = i.convert('RGB')
    img = transTensor(img).unsqueeze(0)
    aged_face = model(img)
    aged_face1 = model(img)
    aged_face2 = model(img)
    aged_face3 = model(img)

    aged_face1 = (aged_face.squeeze().permute(1, 2, 0).detach().numpy() + 1.0) / 2.0
    plt.imshow(aged_face1)
    plt.savefig('path')
    aged_face = model(aged_face)
    aged_face2 = (aged_face.squeeze().permute(1, 2, 0).detach().numpy() + 1.0) / 2.0
    plt.imshow(aged_face2)
    plt.savefig('path')
    aged_face = model(aged_face)
    aged_face3 = (aged_face.squeeze().permute(1, 2, 0).detach().numpy() + 1.0) / 2.0
    plt.imshow(aged_face3)
    plt.savefig('path')

    return aged_face

def display_image(image, path):
    plt.imshow(image)
    plt.savefig(path)


if __name__ == '__main__':
    img = Image.open("adriana.jpg")

    img = make_image_older(img)
