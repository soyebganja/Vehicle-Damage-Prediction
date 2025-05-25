from PIL import Image
from torchvision import transforms, models
from torch import nn
import torch

trained_model = None
class_name = ['Front Breakage', 'Front Crushed', 'Front Normal', 'Rear Breakage', 'Rear Crushed', 'Rear Normal']

class CarClassifierEfficientNet(nn.Module):
    def __init__(self, num_classes=6):
        super().__init__()
        self.model = models.resnet50(weights='DEFAULT')

        for param in self.model.parameters():
            param.requires_grad = False

        # unfreeze layer4 and fc layer
        for param in self.model.layer4.parameters():
            param.requires_grad = True

        self.model.fc = nn.Sequential(
            nn.Dropout(p=0.2),
            nn.Linear(self.model.fc.in_features, num_classes)
        )

    def forward(self, xb):
        return self.model(xb)

def predict(image_path):
  image = Image.open(image_path).convert("RGB")
  transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
  ])
  image_tensor =  transform(image).unsqueeze(0)

  global trained_model

  if trained_model is None:
    trained_model = CarClassifierEfficientNet()
    trained_model.load_state_dict(torch.load("model/resnet_model.pth"))
    trained_model.eval()

  with torch.no_grad():
      output = trained_model(image_tensor)
      _, predicted_index = torch.max(output, 1)
      return class_name[predicted_index.item()]