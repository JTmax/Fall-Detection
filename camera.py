import pyrealsense2 as rs
import numpy as np
import cv2

# constants
d = 0


# configure depth stream
pipe = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
colorizer = rs.colorizer() # white to black
colorizer.set_option(rs.option.color_scheme, 3)

# start streaming
pipe.start(config)

try:
    while True:

        # wait for a coherent pair of frames
        frames = pipe.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            continue

        # convert image to numpy array and colorize
        image = np.asanyarray(colorizer.colorize(depth_frame).get_data())

        # save image
        filename = 'Fall-Data/Custom/Fall/original/Fall10/file_%d.png'%d
        cv2.imwrite(filename, image)

        # show image
        cv2.namedWindow('Realsense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Realsense', image)
        cv2.waitKey(1)
        d += 1

finally:

    # stop streaming
    pipe.stop()
