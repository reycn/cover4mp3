#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import songs
import search
import update


def main(dir='./songs'):
    file_list = songs.list_dir(dir)
    for i in file_list:
        url = search.get_cover(i)
        file_path = './songs/' + str(i) + '.mp3'
        cover_path = file_path + '.jpg'
        try:
            # print(file_path)
            # update.update_cover(file_path, url)
            update.download_cover(file_path, url)
            update.resize_img(cover_path)
            update.add_metadata_to_song(file_path, cover_path)
            print(str(i), 'Success!')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        main()
    finally:
        print('\nDone!')
