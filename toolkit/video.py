import ffmpeg
from all_media import ProcessMedia


class ProcessVideo(ProcessMedia):
    def __init__(self, path):
        super().__init__(path)

    def extract_audio(self):
        ffmpeg.input(self._source_path).output(
            self._output_path, acodec="libshine"
        ).run(cmd="./ffmpeg")

    def convert_to_x264(self):
        pass

    def convert_to_x265(self):
        pass

    def compress_video_to_720(self):
        pass

    def compress_video_to_480(self):
        pass


if __name__ == "__main__":
    some_video = ProcessVideo("./sources/tatarka.mp4")
    some_video.extract_audio()
