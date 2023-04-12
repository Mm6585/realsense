import cv2
import image
import pipeline as pl

if __name__ == "__main__":
    pipeline = pl.create_pipeline()
    try:
        while (True):
            color_image, depth_iamge = image.get_images(pipeline)  # images[0=color_image, 1=depth_image], size=(480, 640, 3)

            cv2.imshow('color_image', color_image)
            cv2.imshow('depth_image', depth_iamge)
            key = cv2.waitKey(1)
            if (key == 27):
                break
    finally:
        pl.stop_pipeline(pipeline)
        cv2.destroyAllWindows()