import ffmpeg
from .all_media import ProcessMedia


class ProcessPhoto(ProcessMedia):
    def __init__(self, path):
        super().__init__(path)

    def all_format_to_png(self):
        output_pattern = f"{self._output_path}_%03d.png"
        try:
            ffmpeg.input(self._source_path).output(output_pattern, vcodec="png").run(
                cmd="./ffmpeg"
            )
        except Exception as e:
            print(f"Error converting video to PNG: {e}")

    def all_format_to_jpg(self):
        output_pattern = f"{self._output_path}_%03d.jpg"
        try:
            ffmpeg.input(self._source_path).output(output_pattern, vcodec="mjpeg").run(
                cmd="./ffmpeg"
            )
        except Exception as e:
            print(f"Error converting video to JPG: {e}")
