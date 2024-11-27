Author: Mia Dai
# Image Data
1. Picture data are 16 bit. Unlike standard 8-bit images, which can show 256 levels of brightness (0–255), a 16-bit image has a much larger range of 65,536 levels (0–65,535). This allows for a lot more detail and subtle gradations in intensity. However, typical image viewers are optimized for 8-bit images and may not automatically adjust for the higher range in 16-bit images, causing the image to appear very dark or even black. This means that, in the context of a 16-bit range, these pixels have very low intensity relative to the maximum possible value. Also the positive ones are usually <1000. As a result, they are not easily visible when the image is displayed without adjustments.
2. The image matrices are {(2048, 2048), (512, 512), (1024, 1024)}. The value of integer pixel is in the range of 0–65,535.
3. FIJI (an image processing software) allows you to adjust the display range, or "thresholding" values, to bring out details in the image. By setting the display to focus on the lower intensity range where the positive signals are (e.g., 0–1,000), you can make these subtle details visible. This adjustment effectively scales the brightness levels to better match what you’re trying to visualize, making it easier to see the relevant features.
4. To show observable raw images, set vmax = 1000. To show observable segmented images, set vmax = 1. The key idea is to find the maximum pixel value of the image.

