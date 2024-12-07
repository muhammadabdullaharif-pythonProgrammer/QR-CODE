import qrcode
from PIL import Image

# Define the URL for the QR code
url = "https://www.linkedin.com/in/muhammad-abdullah-arif-919ab6337/"

# Create a QR Code object with customization options
qr = qrcode.QRCode(
    version=1,  # Version controls the size of the QR code (1 is 21x21, and it grows with higher numbers)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction (H is 30% recovery capability)
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border size (minimum is 4)
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image
img.save("LinkedIn_Profile.png")

print("QR code has been created and saved as 'LinkedIn_Profile.png'")
