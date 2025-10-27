import sys

from src.converter import converter
from src.downloader import downloader
from src.url_validator.url_validator import validate_url


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


def main():
    url: str = get_url()
    filenames: list[str]

    video_downloader = downloader.Downloader()
    video_downloader.download(url)

    filenames = video_downloader.filename_collector.filenames.copy()

    if '--convert-mp3' in sys.argv:
        for filename in video_downloader.filename_collector.filenames:
            filenames.append(converter.mp3_converter(filename))

    downloader.sort_downloaded_files(filenames)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Terminating program...')
