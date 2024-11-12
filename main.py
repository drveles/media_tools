from toolkit.video import ProcessVideo
from toolkit.photo import ProcessPhoto
from toolkit.audio import ProcessAudio

if __name__ == "__main__":
    some_video = ProcessVideo("./sources/house.mp4")
    some_video.extract_audio()
    some_video.convert_to_x264()
    some_video.convert_to_x265()
    some_video.compress_video_to_480()
    some_video.compress_video_to_720()

    some_photo = ProcessPhoto("./sources/test.png")
    some_photo.all_format_to_png()
    some_photo.all_format_to_jpg()

    some_audio = ProcessAudio("./sources/tatarka.mp3")
    some_audio.all_format_to_mp3()
    some_audio.all_format_to_compressed_mp3()