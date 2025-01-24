<h1 align="center">
  <img src="logo.svg" style="width: 20rem" alt="logo do projeto"><br/>
  Video Downloader
</h1>

![GitHub License](https://img.shields.io/github/license/HeberBarra/video-downloader?logo=github)
![Project Top Language](https://img.shields.io/github/languages/top/HeberBarra/video-downloader?logo=python&label=Python)

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD43B)

A simple program written in python for downloading YouTube videos as MP4, and optionally convert them using ffmpeg.

<h2>Usage</h2>
Requires poetry
To be able to use this program you'll need to install it's dependencies can be installed using the following command:

```poetry install --without dev --no-root```

CLI: Simply run the main.py file and enter the URL for the video that you wish to be downloaded:

```poetry run python -m main```

WEB (DEVEL SERVER): Start the web server using the following command:

```poetry run flask --app web/app.py run```

<h2>License</h2>

This project is under [MIT - Massachusetts Institute of Technology](https://choosealicense.com/licenses/mit/). A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
