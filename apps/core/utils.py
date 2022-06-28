import tempfile

from django.core.files.images import ImageFile
from django.core.files.temp import NamedTemporaryFile

import tinify
from decouple import config
from PIL import Image


def optimize_image(image: ImageFile, width: int, height: int, method: str) -> ImageFile:
    """Optimizes images with tinify see https://tinypng.com/developers/reference/python.

    Expects env.TINYFY_API_KEY to be set with the appropriate API key

    Args:
        image (ImageFile): The un optimized image
        width (int): Final width of image
        height (int): Final height of image
        method (str): Method used for resizing -> thumb | scale | fit | cover

    Raises:
        tinify.AccountError: Related to API key of account API usage limits.
        tinify.ClientError: Incorrect or unsupported image file provided.
        tinify.ServerError: Temporary issue with the Tinify API.
        tinify.ConnectionError: A network connection error occurred.
        Exception: If an exception unrelated to Tinify occurs.

    Returns:
        ImageFile: an instance of django.core.files.images.ImageFile
    """

    if image.width <= width and image.height <= height:
        print("Image already optimal, no need to waste API resources :)")
        return image

    try:
        API_KEY = config("TINYFY_API_KEY")
        if not API_KEY:
            raise Exception("Tinify API key missing")
        tinify.key = API_KEY
        image = tinify.from_buffer(image)
        image_bytes = image.resize(method=method, width=width, height=height).to_buffer()

    except tinify.AccountError as e:
        print("Verify your API key and account limit.")
        raise (e)

    except tinify.ClientError as e:
        print("Check your source image and request options.")
        raise (e)

    except tinify.ServerError as e:
        print("Temporary issue with the Tinify API.")
        raise (e)

    except tinify.ConnectionError as e:
        print("A network connection error occurred.")
        raise (e)

    except Exception as e:
        print("Something else went wrong, unrelated to the Tinify API.")
        raise (e)

    image = NamedTemporaryFile(delete=False)
    image.write(image_bytes)
    image.flush()
    optimized_image = ImageFile(image)
    return optimized_image


def get_test_image_file(width: int, height: int) -> str:
    """Creates a temporary image for testing models with ImageField

    Returns:
        str: file path representing the location of the temporary image
    """
    image_file_path = NamedTemporaryFile(delete=False)
    Image.new("RGB", (width, height), "white").save(image_file_path, "png")
    return image_file_path.name
