import qrcode 
# img=qr.make("")
# img.save("pihu.png")
from PIL import Image
#import qrcode.constants
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://www.google.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("pihu__.png")