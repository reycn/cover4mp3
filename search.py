#!/usr/bin/env python3
# -*- coding: utf8 -*-
import requests
import auth
import json


def get_cover(music_name):
    url = auth.BASE_URL + '/api/search/get'
    data = {
        's': music_name,
        'type': 10,
        'offset': 0,
        'total': 'true',
        # 'limit': limit
    }
    req = requests.post(url, headers=auth.headers, data=data)
    cover_url = req.json()['result']['albums'][0]['blurPicUrl']
    cover_url.replace(' ', '')
    # print(cover_url)
    return(cover_url)


if __name__ == '__main__':

    music_name = 'something just like this'
    print(get_cover(music_name))

    # TESTING!!!!!!!!!!!!111
    print('TESTING!!!!!!!!!!!!!!!!!!!!!!')
