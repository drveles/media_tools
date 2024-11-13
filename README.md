# Media Tools
A set of multimedia conversion tools for processing video, audio, and images.

This project provides convenient scripts to convert, compress, and format multimedia files using Python and FFmpeg.

## Features

- Video processing: Extract audio, compress, and convert videos to various formats.
- Audio processing: Convert audio files to multiple formats with optional compression.
- Image processing: Convert image files to PNG and JPG formats.

## Requirements

- Python 3.8+: Ensure Python is installed on your system. You can download it from python.org.
- FFmpeg: Required for media processing. Download FFmpeg and place the executable in the root folder of the project.

## Installation

Clone the repository:
``` sh
git clone https://github.com/yourusername/media-tools.git
cd media-tools
```

Set up a virtual environment:

``` sh
python3 -m venv venv
source venv/bin/activate 
```

Install dependencies:
``` sh
pip install -r requirements.txt
```

Download and place FFmpeg:
- Download FFmpeg from FFmpeg.org.
- Place the FFmpeg executable (e.g., ffmpeg.exe on Windows or ffmpeg on Linux/Mac) in the project’s root folder.

## Usage

1. Configure the files to convert:
    - Open main.py.
    - Specify the files to process in main.py by adding paths to ProcessVideo, ProcessPhoto, and ProcessAudio classes as shown:
    ``` python
    from toolkit.video import ProcessVideo
    from toolkit.photo import ProcessPhoto
    from toolkit.audio import ProcessAudio

    if __name__ == "__main__":
        video = ProcessVideo("./sources/house.mp4")
        audio = ProcessAudio("./sources/music.mp3")
        photo = ProcessPhoto("./sources/image.png")
    ```

2. Run the script:
    ``` sh
    python main.py
    ```

3. View the results:

    Processed files will be saved in the `results` folder.