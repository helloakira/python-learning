from PIL import Image
import os


for file in os.listdir('./origin'):
    if not file.endswith('.py'):
        print(file)
        image_file = Image.open(os.path.join('origin', file))
        image_file = image_file.convert('L')
        (filename, extension) = os.path.splitext(file)
        image_file.save(os.path.join('result', filename + '_grey.png'))
