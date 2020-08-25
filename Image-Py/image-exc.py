from PIL import Image


mask_img = Image.open("mask.png")
(w, h) = mask_img.size

matrix_img = Image.open("word_matrix.png")
matrix_img = matrix_img.resize((w, h))

mask_img.putalpha(128)
matrix_img.putalpha(128)

matrix_img.paste(im=mask_img, box=(0, 0), mask=mask_img)
matrix_img.save("challenge.png")
print(h)
print(w)
