import os
import re
import sys

from converter import converter
from downloader.downloader import Downloader


def validate_url(url: str) -> bool:
    regex_pattern = re.compile(
        r'^((?:https?:)?//)?((?:www|m)\.)?(youtube(?:-nocookie)?\.com|youtu.be)(/(?:[\w\-]+\?v=|embed/|live/|v/)?)([\w\-]+)(\S+)?$'
    )
    return regex_pattern.match(url) is not None


def get_url() -> str | None:
    for value in sys.argv:
        if '--url' in value:
            url = '='.join(value.split('=')[1:])

            if validate_url(url):
                return url

            print('Invalid URL... Please type a valid one...')

    while True:
        url = input('Video URL: ')

        if url == '':
            print('Please type something...')
            continue

        if not validate_url(url):
            print('Please type a valid URL')
            continue

        return url


def move_file(video_filepath: str):
    if video_filepath.endswith('.mp4'):
        os.rename(video_filepath, f'videos/{video_filepath}')
        return

    if video_filepath.endswith('.mp3'):
        os.rename(video_filepath, f'music/{video_filepath}')
        return


def create_result_directories():
    result_directories = ['videos', 'music']

    for directory in result_directories:
        if not os.path.isdir(directory):
            os.makedirs(directory)


def main():
    url: str = get_url()
    filenames: list[str]
    create_result_directories()

    downloader = Downloader()
    downloader.download(url)

    filenames = downloader.filename_collector.filenames.copy()

    if '--convert-mp3' in sys.argv:
        for filename in downloader.filename_collector.filenames:
            filenames.append(converter.mp3_converter(filename))

    for filename in filenames:
        move_file(filename)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Terminating program...')
