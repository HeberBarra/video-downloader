import subprocess


def mp3_converter(video_filepath: str) -> str:
    base_filename = '.'.join(video_filepath.split('.')[:-1])
    ffmpeg_command = [
        'ffmpeg',
        '-i',
        f'{base_filename}.mp4',
        '-b:a',
        '320K',
        f'{base_filename}.mp3',
    ]
    subprocess.run(ffmpeg_command)

    return f'{base_filename}.mp3'
