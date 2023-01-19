from pytube import YouTube
import os


class Mp3Download:

    def __init__(self):
        pass

    def Download(self, url, dst):

        yt = YouTube(url)

        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path=dst)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


class Mp4Download:

    def __init__(self):
        pass

    def Download(self, url, dst, resolution):

        yt = YouTube(url)
        resolution = yt.streams.get_by_resolution(resolution)
        resolution.download(dst)
