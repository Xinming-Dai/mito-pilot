import cv2
import numpy as np
from typing import Tuple

def pad_image(image:np.ndarray, target_size:Tuple[int]=(2048, 2048), color:int=0) -> np.ndarray:
    """
    Use padding to fit the images into a uniform canvas size while maintaining the original aspect ratio.

    Args:
        image: image. 
        target_size: the target size of the image.

    Returns:
        image with target size.
    """
    h, w = image.shape
    delta_w = target_size[1] - w
    delta_h = target_size[0] - h
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    padded_img = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return padded_img

def resize_image(image:np.ndarray, target_size:Tuple[int]=(512, 512)) -> np.ndarray:
    """
    Resize images into a uniform canvas size.

    Args:
        image: image. 
        target_size: the target size of the image.

    Returns:
        image with target size.
    """
    resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    return resized_image