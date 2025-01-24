import os

from yt_dlp import YoutubeDL

from downloader.filename_collector import FilenameCollector
from downloader.no_url_provided import NoURLProvided


def sort_downloaded_files(files: list[str]):
    for file in files:
        if file.endswith('.mp4'):
            os.rename(file, f'videos/{file}')
            continue

        if file.endswith('.mp3'):
            os.rename(file, f'music/{file}')
            continue


class Downloader(YoutubeDL):
    _download_options = {'format': 'mp4/best'}
    _result_directories = {'videos', 'music'}

    filename_collector: FilenameCollector

    def __init__(self):
        super().__init__(self._download_options)
        self.filename_collector = FilenameCollector()
        self.add_post_processor(self.filename_collector)
        self.create_result_directories()

    def download(self, url: str = None) -> bool:
        if url is None:
            raise NoURLProvided

        return super().download([url]) != 1

    def create_result_directories(self):
        for directory in self._result_directories:
            if not os.path.isdir(directory):
                os.makedirs(directory)
