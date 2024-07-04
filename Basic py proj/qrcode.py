import pyqrcode
from pyqrcode import QRCode
string="https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
url=pyqrcode.create(string)
url.svg("myyoutube.svg",scale=8)