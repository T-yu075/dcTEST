import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
#   抓
def channel_viedo5():
    DEVELOPER_KEY = 'AIzaSyCNeYjG4cRWFYifYEoGRQmBDqOfR5BX_rs'
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    channel_infor = []  # save apiget
    json_channel = []   # save json_read

    with open('./search_infor.json') as inforJS:
        data = json.load(inforJS)
        inforJS.close()
    with open('./channel_infor.json') as channelR:
        data2 = json.load(channelR)
        json_channel.append(data2)
        channelR.close()
        # print(json_channel)


    for channel_url in data["search_url"]:
        json_channel = []
        print(channel_url)
        request = youtube.search().list(
            part= "snippet",
            order= "date",
            channelId= channel_url
        ).execute()
        # print(f"{request}\n")
        json_channel.append(request)
        channel_infor.append(request)
        # if json_channel ==
    apiget = json.dumps(channel_infor)

    with open('./channel_infor.json', "w") as channelJS:
            channelJS.write(apiget)
            channelJS.close()

    print("owari~")

if __name__=="__main__":
    channel_viedo5()