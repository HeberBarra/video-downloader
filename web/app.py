from os import environ

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from yt_dlp.utils import ExtractorError
from waitress import serve

from converter import converter
from downloader import downloader
from url_validator import url_validator


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video', methods=['POST'])
def video():
    error: str | None = None
    video_url = request.form.get('video-url')

    if not url_validator.validate_url(video_url):
        error = 'Invalid URL'

    video_downloader = downloader.Downloader()
    video_downloader.download(video_url)

    files = video_downloader.filename_collector.filenames.copy()
    if 'download-mp3' in request.form:
        for file in video_downloader.filename_collector.filenames:
            files.append(converter.mp3_converter(file))

    print(app.root_path)
    downloader.sort_downloaded_files(files)

    if len(files) == 0:
        return redirect(url_for('index', error=error))

    target_file: str = files[-1]
    if target_file.endswith('.mp3'):
        return send_from_directory('../music', target_file, as_attachment=True)
    else:
        return send_from_directory('../videos', target_file, as_attachment=True)


@app.errorhandler(ExtractorError)
def handle_invalid_url(e):
    error = 'Invalid video URL'
    return render_template('index.html', error=error)


app.register_error_handler(500, handle_invalid_url)


if __name__ == '__main__':
    if 'BEHIND_PROXY' in environ:
        serve(app, host='0.0.0.0', port=5000)

    app.run()
