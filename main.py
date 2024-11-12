import time
import threading
from toolkit.video import ProcessVideo
from toolkit.photo import ProcessPhoto
from toolkit.audio import ProcessAudio


def video_process():
    some_video = ProcessVideo("./sources/house.mp4")
    some_video.extract_audio()
    some_video.convert_to_x264()
    some_video.convert_to_x265()
    some_video.compress_video_to_480()
    some_video.compress_video_to_720()


def audio_process():
    some_audio = ProcessAudio("./sources/tatarka.mp3")
    some_audio.all_format_to_mp3()
    some_audio.all_format_to_compressed_mp3()


def photo_process():
    some_photo = ProcessPhoto("./sources/test.png")
    some_photo.all_format_to_png()
    some_photo.all_format_to_jpg()


def multitreading_main():
    video_thread = threading.Thread(target=video_process)
    audio_thread = threading.Thread(target=audio_process)
    photo_thread = threading.Thread(target=photo_process)
    video_thread.start()
    audio_thread.start()
    photo_thread.start()
    video_thread.join()
    audio_thread.join()
    photo_thread.join()


def main():
    video_process()
    audio_process()
    photo_process()


if __name__ == "__main__":
    temp_time = time.time()
    multitreading_main()
    print("time taken in seconds:", round(time.time() - temp_time, 2))
