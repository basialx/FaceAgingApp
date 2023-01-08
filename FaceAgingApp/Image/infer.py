import os
import random
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import torch
from PIL import Image
from torchvision import transforms

from FaceAgingApp.settings import BASE_DIR
from gan_module import Generator
from .form import ImageForm
from .models import Image

@torch.no_grad()
def main():
    image_paths = Image.image.url
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    trans = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    nr_images = len(image_paths) if len(image_paths) < 6 else 6
    fig, ax = plt.subplots(2, nr_images, figsize=(20, 10))
    random.shuffle(image_paths)
    for i in range(nr_images):
        img = Image.open(image_paths[i]).convert('RGB') #tutaj gdzies bedzie szlo  zdjecie z kamery
        img = trans(img).unsqueeze(0)
        aged_face = model(img) #tu gdzeis petla w zaleznosci od lat
        #aged_face = model(aged_face)  # tu gdzeis petla w zaleznosci od lat
        #aged_face = model(aged_face)  # tu gdzeis petla w zaleznosci od lat
        #aged_face = model(aged_face)  # tu gdzeis petla w zaleznosci od lat
        aged_face = (aged_face.squeeze().permute(1, 2, 0).numpy() + 1.0) / 2.0
        ax[0].imshow((img.squeeze().permute(1, 2, 0).numpy() + 1.0) / 2.0)
        ax[1].imshow(aged_face)
    # plt.show()
    plt.savefig("media/image/")
    #plt.saveimg()


