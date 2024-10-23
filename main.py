import qrcode
data = "edtechbymeera"
qr = qrcode.QRCode(version=1, box_size = 59, border=2)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color= "gold", back_color= "red")
img.save("myQRCode.png")

import qrcode
from PIL import Image
logo = Image.open("mylogo.png")
QRCode = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
QRCode.add_data("My code camp")
QRCode.make()
QRImg = QRCode.make_image().convert("RGB")
pos = ((QRImg.size[0] - logo.size[0]) // 2, (QRImg.size[1] - logo.size[1]) // 2)
QRImg.paste(logo,pos)
QRImg.save("qrcode-logo.png")




