import qrcode


qr = qrcode.QRCode(
    version=1, #The version parameter is an integer from 1 to 40 that controls the size of the QR Code.
    error_correction=qrcode.constants.ERROR_CORRECT_L, #The error_correction parameter controls the error correction used for the QR Code.
    box_size=10, #The box_size parameter controls how many pixels each “box” of the QR code is.
    border=4, #The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
)
qr.add_data('https://github.com/Abdulaziz-Asiri/AZ-007') #write out the data here link/anything
qr.make(fit=True) #Set to None and use the fit parameter when making the code to determine this automatically.

img = qr.make_image(fill_color="black", back_color="white") #control color of QRCode image.
img.save("My_GitHub.png") #save the QRCode image with naming.
