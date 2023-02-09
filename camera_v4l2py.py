import v4l2py
from base_camera import BaseCamera


class Camera(BaseCamera):
    """Requires python-v4l2capture module: https://github.com/gebart/python-v4l2capture"""

    video_source = 1

    @staticmethod
    def frames():
        camera = v4l2py.Device.from_id(Camera.video_source)
        with camera:
            capture = v4l2py.VideoCapture(camera)
            capture.set_format(640, 480, "MJPG")
            with capture as stream:
                yield from stream

