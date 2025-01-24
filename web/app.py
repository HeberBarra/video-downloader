from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory

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
