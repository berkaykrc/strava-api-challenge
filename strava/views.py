from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as r
# import ipdb


segments = []
duplicate_bikers = []
all_names = []


@api_view()
def source(request):

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

        kontrol = False
        for j in range(len(segments)):
            for i in range(len(segments)):
                for k in range(len(segments)):
                    for m in range(len(segments)):
                        if j != k and m != i:
                            if all_names[j][i] == all_names[k][m]:
                                for a in range(len(duplicate_bikers)):
                                    if all_names[j][i] == duplicate_bikers[a]:
                                        kontrol = True
                                if kontrol is False:
                                    duplicate_bikers.append(all_names[j][i])
                                else:
                                    kontrol = False
        return Response(duplicate_bikers)

    except Exception as x:
        print("Your Exception is :", x)
