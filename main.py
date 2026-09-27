from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import  torch
import matplotlib.pyplot as plt
model_name = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
image_path = "cat.jpg"
image = Image.open(image_path).convert("RGB")
inputs = processor(images=image, return_tensors="pt").to(device)
outputs = model.generate(**inputs)
caption = processor.decode(outputs[0], skip_special_tokens=True)
plt.figure(figsize=(6,6))
plt.imshow(image)
plt.axis("off")
plt.title(caption, fontsize=14, color="black")
plt.show()
print("Image caption: ", caption)