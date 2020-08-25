from PIL import Image

macinthosh_image = Image.open("example.jpg")

print(macinthosh_image.size)
print(macinthosh_image.format_description)
print(macinthosh_image.filename)


# Cropped Image
pencils_image = Image.open("pencils.jpg")
# pencils_image.show()
croped_iamge = pencils_image.crop((0, 0, 500, 300))
# croped_iamge.show()

macinthosh_image.paste(im=croped_iamge, box=(0, 0))

macinthosh_image = macinthosh_image.resize((300, 500))
macinthosh_image = macinthosh_image.rotate(90)

# macinthosh_image.show()

red_img = Image.open("red_color.jpg")
# red_img.show()

blue_img = Image.open("blue_color.png")
purple_img = Image.open("purple.png")

red_img.putalpha(128)
purple_img.putalpha(128)

red_img.paste(im=purple_img, box=(0, 0), mask=purple_img)
red_img.show()

red_img.save("new_img.png")
