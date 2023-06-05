from pytube import YouTube
import time
import re


def download_video(url):

    p = re.compile("https://youtu.be/*")
    o = re.compile("https://www.youtube.com/*")
    if p.match(url) or o.match(url):
        yt = YouTube(url)
        __import__('pprint').pprint(yt.streams)
        print('Video Downloaded Successfully')
        title = "sample.mp4"
        yt.streams.get_by_itag(140).download(filename=title)
        time.sleep(1)
        return title
    else:
        print('Invalid URL')
        return None


if __name__ == '__main__':
    url = input('Enter the URL of the video: ')
    download_video(url)
