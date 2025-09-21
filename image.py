from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load pre-trained ResNet-50 model
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # ImageNet means
        std=[0.229, 0.224, 0.225]    # ImageNet stds
    )
])

def extract_features(image_path):
    image = Image.open(image_path).convert('RGB')
    img_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        features = model(img_tensor)
    return features.numpy()

def compute_similarity(img1_path, img2_path):
    features1 = extract_features(img1_path)
    features2 = extract_features(img2_path)
    similarity = cosine_similarity(features1, features2)[0][0]
    return similarity

# Example usage
# img1 = "DCI/DSC_0565.JPG"
# img2 = "DCI/DSC_0566.JPG"
def get_image_paths(img1, img2):
    score = compute_similarity(img1, img2)
    return (f"{score:.4f}")
    # print(f"Similarity score: {score:.4f}")


if __name__ == "__main__":
    # img1 = input("Enter the path to the first image: ")  # Replace with your image path
    # img2 = input("Enter the path to the second image: ")  # Replace with your image path

    img1 = "DCI/DSC_0565.JPG"
    img2 = "DCI/DSC_0566.JPG"

    score = compute_similarity(img1, img2)
    print(f"Similarity score: {score:.4f}")
