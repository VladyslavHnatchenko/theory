from secrets import token_urlsafe

DATABASE = {}


def shorten(url: str, nbytes: int=5) -> str:
    ext = token_urlsafe(nbytes=nbytes)
    if ext in DATABASE:
        return shorten(url, nbytes=nbytes)
    else:
        DATABASE.update({ext: url})
        return f'short.ly/{ext}'
