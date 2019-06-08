import pyqrcode

def generate_qr():
    link_to_post = 'https://drive.google.com/file/d/1rCXu2iKENDXPyzmvo-E8HU8rroOe1p5_/view?usp=sharing'
    url = pyqrcode.create(link_to_post)
    url.png('url.png', scale=8)
    #print("Printing QR code")
    #print(url.terminal())

if __name__ == '__main__':
    generate_qr()
