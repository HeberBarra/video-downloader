from yt_dlp.postprocessor.common import PostProcessor


class FilenameCollector(PostProcessor):
    def __init__(self):
        super(FilenameCollector, self).__init__()
        self.filenames = []

    def run(self, information):
        self.filenames.append(information['filepath'])
        return super().run(information)
