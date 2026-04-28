'''Packages & Debugging
(1) Pyhton Packages & Core Package
(2) Package Manager & External Package
(3) Debugging
'''
from PIL import Image
import turtle
print("===== Pyhton Packages & Core Package ===== ")
''' Pyhton Packages/Modules: core , file and External '''
# core Packages

# # Core
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(150)

# turtle.done()

print("-----------")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content", content)
finally:
    my_file.close()

# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)
print("done")


print("===== Package Manager & External Package ===== ")
''' Package Manager: pip pipenv npm yarn composer brew '''
# External Package > https://pypi.org/

with Image.open("material/kittenCoder.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
