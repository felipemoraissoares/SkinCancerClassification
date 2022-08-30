import io

import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

def transform_image(image_bytes):
    norm_mean = (0.76310134, 0.5456841, 0.57007784)
    norm_std = (0.14092982, 0.1526007, 0.16996273)
    my_transforms = transforms.Compose([transforms.Resize(224),
                                        transforms.RandomHorizontalFlip(),
                                        transforms.RandomVerticalFlip(),transforms.RandomRotation(20),
                                        transforms.ColorJitter(brightness=0.1, contrast=0.1, hue=0.1),
                                        transforms.ToTensor(), transforms.Normalize(norm_mean, norm_std)])

    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes).to(device)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return predicted_idx

classe = [
    'Queratose Actinica',
    'Carcinoma',
    'Queratose Seborreica ',
    'Dermatofibroma',
    'Nevo Melanotico',
    'Lesão Vascular',
    'Melanoma',
]

if torch.cuda.is_available():
  device = torch.device('cuda')
else:
  device = torch.device('cpu')
print(device)

model_ft = torch.load('densenet_model')
model = model_ft.to(device)
model.eval()

def abrir_img(path):
    with open(path, 'rb') as f:
        image_bytes = f.read()
        print('abriu')
        tipo = get_prediction(image_bytes=image_bytes)
        print(tipo, classe[int(tipo)])
        resultado = classe[int(tipo)]
        return resultado





