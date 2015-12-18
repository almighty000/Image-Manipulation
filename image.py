from PIL import Image 

# open colour image
image_file = Image.open("image.jpg") 

# convert image to black and white
image_file = image_file.convert('1') 

image_file.save('image.jpg')
