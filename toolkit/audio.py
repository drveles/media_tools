import ffmpeg
from .all_media import ProcessMedia


class ProcessAudio(ProcessMedia):
    def __init__(self, path):
        super().__init__(path)

    def all_format_to_mp3(self):
        output_path = f"{self._output_path}.mp3"
        try:
            ffmpeg.input(self._source_path).output(
                output_path, acodec="libmp3lame", audio_bitrate="192k"
            ).run(cmd="./ffmpeg")
        except Exception as e:
            print(f"Error converting audio to MP3: {e}")

    def all_format_to_compressed_mp3(self):
        output_path = f"{self._output_path}_compressed.mp3"
        try:
            ffmpeg.input(self._source_path).output(
                output_path, acodec="libmp3lame", audio_bitrate="96k"
            ).run(cmd="./ffmpeg")
        except Exception as e:
            print(f"Error converting audio to compressed MP3: {e}")
