import cv2
import image
import pipeline as pl

if __name__ == "__main__":
    color_vid_name = input('Input Color Video Name : ')
    depth_vid_name = input('Input Depth Video Name : ')

    width = 640
    height = 480
    fps = 30.0
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    color_writer = cv2.VideoWriter(color_vid_name, fourcc, fps, (width, height))
    depth_writer = cv2.VideoWriter(depth_vid_name, fourcc, fps, (width, height))
    
    pipeline = pl.create_pipeline()

    try:
        i = 0
        while (i < 100):
            images, sizes = image.get_images(pipeline)  # images[0=color_image, 1=depth_image], size=(480, 640, 3)
            color_writer.write(images[0])
            depth_writer.write(images[1])
            i += 1
            
    finally:
        pl.stop_pipeline(pipeline)
        color_writer.release()
        depth_writer.release()