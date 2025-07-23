# capture.py

from PIL import ImageGrab

def capture_screen(region=None) -> str:
    try:
        if not region:
            region = (100, 100, 800, 1080)
        image_path = "captured_image.jpg"
        screenshot = ImageGrab.grab(bbox=region)
        screenshot.save(image_path)
        return image_path
    except Exception as e:
        print("Error capturing screen:", e)
        raise

def encode_image_to_base64(image_path: str) -> str:
    try:
        with open(image_path, "rb") as f:
            return f.read().encode("base64").decode("utf-8")
    except Exception as e:
        print("Error encoding image:", e)
        raise
