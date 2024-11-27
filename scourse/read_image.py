import os
import tifffile as tiff
import matplotlib.pyplot as plt
import numpy as np
from typing import List


def sort_image_files(dir_path: str) -> List[str]:
    """
    Return the list of file names sorted by the the cell number. 

    Args:
        dir_path: the path contains the image. 

    Returns:
        A list of file names.
    """
    file_list = os.listdir(dir_path)
    cell_name = [int(file.split('_')[1].split('.')[0]) for file in file_list]
    sorted_indexes = np.argsort(cell_name)
    sorted_list = [file_list[i] for i in sorted_indexes]
    return sorted_list

def image_preview(dir_path:str, vmax:int=1000, number_shows:int=4) -> None:
    """
    Display raw image or segmented image.

    Args:
        dir_path: 
            the path contains the image. 
        vmax: 
            vmax is used in conjunction with norm to normalize luminance data.
        number_shows: 
            the number of images that the user intends to show.

    Returns:
        None.
    """
    i = 0
    seg_tifs = list()
    sorted_list = sort_image_files(dir_path)

    for file in sorted_list:
        if file.endswith('.tif'):
            image_file_name = os.path.join(dir_path, file)
            seg_tifs.append(tiff.imread(image_file_name))
            i = i + 1
        if i == number_shows:
            break

    # display masks from test dataset
    nrow = int(number_shows/2)
    fig, axes = plt.subplots(nrow, 2, figsize=(5, 5))
    axes = axes.ravel()  # flatten the axes array

    for i in range(number_shows):
        axes[i].imshow(seg_tifs[i], cmap='gray', vmin=0, vmax=vmax)
        axes[i].axis('off')
        axes[i].set_title(sorted_list[i])

    fig.tight_layout()
    return None

def get_images(dir_path:str, image_names:str=None) -> List[np.ndarray]:
    """
    Return the list of file names sorted by the the cell number. 

    Args:
        dir_path: the path contains the image. 
        image_names: 
            optional. If it is none, image list will return all the images in the folder.

    Returns:
        the list of image data.
    """
    seg_tifs = list()
    if not image_names:  
        image_names = sort_image_files(dir_path)

    for file in image_names:
        if file.endswith('.tif'):
            image_file_name = os.path.join(dir_path, file)
            seg_tifs.append(tiff.imread(image_file_name))

    return seg_tifs

def match_image(dir_path:str, cell_name: List[int], pattern: List[str] = ["mito1_", "_0000.tif"]) -> List[str]:
    """
    Return the list of file names matches the cell names in the data set. 

    Args:
        dir_path: 
            the path contains the image. 
        cell_name: 
            a list of cell names in the data set. 
        pattern:
            file name patter. It's used to generate file names. The default pattern will generate "mito1_cellname__0000.tif".

    Returns:
        A list of file names.
    """
    file_list = os.listdir(dir_path)
    image_cell_name = set([int(file.split('_')[1].split('.')[0]) for file in file_list])
    file_names = list()

    for name in cell_name:
        if name in image_cell_name:
            file_names.append(pattern[0] + str(name) + pattern[1])
            image_cell_name.remove(name)

    return file_names
