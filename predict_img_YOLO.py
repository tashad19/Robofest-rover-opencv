import os
from ultralytics import YOLO
from PIL import Image

DIR = os.path.join('.', 'images')
img_path = os.path.join(DIR, 'bike.png')

# Load a model
# model = YOLO(model_path)  # load a custom model
model = YOLO("yolov8n.pt")

# Run inference on 'bike.png' with arguments
results = model(img_path)


# Show the results
for r in results:
    im_array = r.plot(conf=True, boxes=True, labels=True)  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image