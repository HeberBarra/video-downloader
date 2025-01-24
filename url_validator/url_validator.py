from re import compile


def validate_url(url: str) -> bool:
    regex_pattern = compile(
        r'^((?:https?:)?//)?((?:www|m)\.)?(youtube(?:-nocookie)?\.com|youtu.be)(/(?:[\w\-]+\?v=|embed/|live/|v/)?)([\w\-]+)(\S+)?$'
    )
    return regex_pattern.match(url) is not None
