from PIL import Image 

# open colour image
image_file = Image.open("image.jpg") 

# convert image to black and white
image_file = image_file.convert('1') 

#another way you can rewrite this line
#image_file = Image.open("image.jpg").convert("L")

image_file.save('image.jpg')
