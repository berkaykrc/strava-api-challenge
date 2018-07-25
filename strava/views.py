import collections
import itertools

import requests as r
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def source(request):
    segments = []
    all_names = []
    segments_explore = 'https://www.strava.com/api/v3/segments/explore?'
    bounds = '&bounds=40.771394267343176, 26.488085546875027, 41.598195829044954, 31.607714453125027'  # istanbul
    access_token = '&access_token=37d4400d9157c0d7b0237e5a5568d9af41272462'  # access
    endpoint = segments_explore + bounds + access_token

    try:
        data1 = r.get(endpoint).json()
        for segment_id in data1["segments"]:
            segments.append(segment_id["id"])

        leader_board = 'https://www.strava.com/api/v3/segments/'
        query = '/leaderboard?&per_page=50'

        for each in segments:
            endpoint2 = leader_board + str(each) + query + access_token
            data2 = r.get(endpoint2).json()
            leaderboard_names = []
            for names in data2["entries"]:
                leaderboard_names.append(str(names["athlete_name"]))
            all_names.append(leaderboard_names)
        # ipdb.set_trace()
        return Response([
            item
            for item, count in collections.Counter(
                itertools.chain.from_iterable(all_names)
            ).items()
            if count > 1
        ])

        '''[name for name, count in Counter(chain(all_names)).items() if count > 1]'''
    except Exception as x:
        print("Your Exception is :", x)
