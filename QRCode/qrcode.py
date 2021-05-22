import pyqrcode

# .PNG
source = "www.github.com/diablo/"
url = pyqrcode.create(source)
url.png('qrcode.png', scale = 8)
url.show()

# .SVG
# source = "www.github.com/CorvoDev/"
# url = pyqrcode.create(source)
# url.svg('qrcode.svg', scale = 8)
# url.show()
