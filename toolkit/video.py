import ffmpeg
from .all_media import ProcessMedia


class ProcessVideo(ProcessMedia):
    def __init__(self, path):
        super().__init__(path)

    def extract_audio(self):
        ffmpeg.input(self._source_path).output(
            f"{self._output_path}.mp3", acodec="libshine"
        ).run(cmd="./ffmpeg")

    def convert_to_x264(self):
        ffmpeg.input(self._source_path).output(
            f"{self._output_path}_x264.mp4", vcodec="libx264"
        ).run("./ffmpeg")

    def convert_to_x265(self):
        ffmpeg.input(self._source_path).output(
            f"{self._output_path}_x265.mp4", vcodec="libx265"
        ).run("./ffmpeg")

    def need_compress(self, height: int) -> bool:
        probe = ffmpeg.probe(
            self._source_path,
            v="error",
            select_streams="v:0",
            show_entries="stream=height",
            cmd="./ffmpeg"
        )
        video_height = int(probe["streams"][0]["height"])
        if video_height > height:
            return True
        else:
            print(f"Compression {self._source_file_name} to {height} not needed")
            return False

    def compress_video_to_720(self):
        try:
            ffmpeg.input(self._source_path).output(
                f"{self._output_path}_720.mp4", vcodec="libx264", vf="scale=-1:720"
            ).run(cmd="./ffmpeg")
        except Exception as e:
            print(e)

    def compress_video_to_480(self):
        try:
            ffmpeg.input(self._source_path).output(
                f"{self._output_path}_480.mp4", vcodec="libx264", vf="scale=-1:480"
            ).run("./ffmpeg")
        except Exception as e:
            print(e)
