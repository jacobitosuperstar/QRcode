import qrcode
from PIL import Image
import qrcode.image.svg

def generate_qr(url:str) -> None:
    """Function that takes and URL and returns a QR code with the content in
    SVG format.
    """
    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
        image_factory=qrcode.image.svg.SvgImage,
    )
    qr.add_data(url)
    qr.make(fit=True)
    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )
    # .convert("RGB")
    image.save("./qr_code.svg")

if __name__ == '__main__':
    link_to_post = ''
    generate_qr(link_to_post)
