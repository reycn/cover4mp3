#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import requests


from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.id3 import ID3, APIC, TPE1, TIT2, TALB, error
from PIL import Image


def resize_img(file_path, max_size=(640, 640), quality=90):
    try:
        img = Image.open(file_path)
    except IOError:
        print('Can\'t open image:', file_path)
        return

    if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
        img.thumbnail(max_size, Image.ANTIALIAS)
        img.save(file_path, quality=quality)

# def update_cover(mp3_name, pic_url):


def add_metadata_to_song(file_path, cover_path):
    # If no ID3 tags in mp3 file
    try:
        audio = MP3(file_path, ID3=ID3)
    except HeaderNotFoundError:
        print('Can\'t sync to MPEG frame, not an validate MP3 file!')
        return

    if audio.tags is None:
        print('No ID3 tag, trying to add one!')
        try:
            audio.add_tags()
            audio.save()
        except error as e:
            print('Error occur when add tags:', str(e))
            return

    # Modify ID3 tags
    id3 = ID3(file_path)
    # Remove old 'APIC' frame
    # Because two 'APIC' may exist together with the different description
    # For more information visit:
    # http://mutagen.readthedocs.io/en/latest/user/id3.html
    if id3.getall('APIC'):
        id3.delall('APIC')
    # add album cover
    id3.add(
        APIC(
            # 3 is for UTF8, but here we use 0 (LATIN1) for 163, orz~~~
            encoding=0,
            mime='image/jpeg',  # image/jpeg or image/png
            type=3,             # 3 is for the cover(front) image
            data=open(cover_path, 'rb').read()
        )
    )
    id3.save(v2_version=3)


def download_cover(mp3_name, pic_url):
    # edit the ID3 tag to add the title, artist, artwork, date, and genre
    req = requests.get(pic_url)
    # imagedata = Image.open(BytesIO(req.content))
    # imagedata = open('a.jpg', 'rb').read()
    # print(im)
    f = open(mp3_name+'.jpg', 'wb')
    f.write(requests.get(pic_url).content)
    f.close()
    # print(mp3_name+'.jpg')
    return(mp3_name+'.jpg')

if __name__ == '__main__':
    # TESTING!!!!!!!!!!!!111
    print('TESTING!!!!!!!!!!!!!!!!!!!!!!')
    dir_path = './songs/'
    mp3_name = '凡人歌_李宗盛'
    mp3_path = dir_path + mp3_name + '.mp3'

    download_cover(mp3_path,
                   'http://p3.music.126.net/ggnyubDdMxrhpqYvpZbhEQ==/3302932937412681.jpg')
    resize_img(mp3_path + '.jpg')
    add_metadata_to_song(mp3_path, mp3_path + '.jpg')
