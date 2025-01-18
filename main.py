from PIL import ImageGrab

def capture_screen(region=None) -> str:
    """
    Captures a screenshot of a specific region (or full screen) and saves it as a file.
    :param region: Tuple (x1, y1, x2, y2) defining the region to capture.
    :return: Path to the saved image file.
    """
    try:
        # Define the default region: (x1, y1, x2, y2)
        if not region:
            region = (100, 100, 800, 600)  # Example region coordinates

        # Capture the screenshot
        screenshot = ImageGrab.grab(bbox=region)

        # Save the screenshot
        image_path = "captured_image.jpg"
        screenshot.save(image_path)
        print(f"Screenshot saved to {image_path}")
        return image_path
    except Exception as e:
        print(f"Error capturing screen: {e}")
        raise

if __name__ == "__main__":
    # Example usage: Capture a specific region of the screen
    region_coordinates = (500, 150, 950, 1000)  # Adjust as needed
    capture_screen(region=region_coordinates)

