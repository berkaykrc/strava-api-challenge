from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as r
segments = []
leader_board_names = []
leader_boards = []


@api_view()
def source(request):

    # import ipdb;ipdb.set_trace()
        segments_explore = 'https://www.strava.com/api/v3/segments/explore?'
        bounds = '&bounds=40.771394267343176, 26.488085546875027, 41.598195829044954, 31.607714453125027'  # istanbul
        access_token = '&access_token=37d4400d9157c0d7b0237e5a5568d9af41272462'  # access
        endpoint = segments_explore + bounds + access_token

        try:
            data1 = r.get(endpoint).json()
            for segment_id in data1["segments"]:
                segments.append(segment_id["id"])
                print(segment_id["id"])

            leader_board = 'https://www.strava.com/api/v3/segments/'
            query = '/leaderboard?&per_page=50'
            firstid = segments[0]
            endpoint2 = leader_board + str(firstid) + query + access_token
            data2 = r.get(endpoint2).json()
            for leader_board_name in data2["entries"]:
                leader_board_names.append(leader_board_name["athlete_name"])
            return Response(leader_board_names)

        except Exception as x:
            print("Your exception", x)
