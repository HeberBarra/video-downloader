from yt_dlp import YoutubeDL

from downloader.filename_collector import FilenameCollector
from downloader.no_url_provided import NoURLProvided


class Downloader(YoutubeDL):
    _download_options = {'format': 'mp4/best'}

    filename_collector: FilenameCollector

    def __init__(self):
        super().__init__(self._download_options)
        self.filename_collector = FilenameCollector()
        self.add_post_processor(self.filename_collector)

    def download(self, url: str = None) -> bool:
        if url is None:
            raise NoURLProvided

        return super().download([url]) != 1
