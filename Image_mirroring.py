from PIL import Image

# to open an image named obtained.png
img = Image.open("obtained.png")

# transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#save to a new file
transposed_img.save('complete.png')
print("flipping done")
