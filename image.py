import numpy as np
import cv2

def get_images(pipeline):
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data()) # uint16
    color_image = np.asanyarray(color_frame.get_data()) # uint8

    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    image_size = depth_colormap.shape

    return [color_image, depth_colormap], image_size