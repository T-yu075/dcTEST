import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
#   只做API get -> 把get到的結果丟json -> owari



def channel_video5():
    pass

def channel_viedo_live():
    DEVELOPER_KEY = ''
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    # channel_infor = []  # save apiget
    channel_live = []
    yt_video = "https://www.youtube.com/watch?v="
    # with open('./search_infor.json') as inforJS:  #   bot用
    with open('../search_infor_forTEST.json') as inforJS:   #   __main__用

        data = json.load(inforJS)
        inforJS.close()

    for channel_count in range(len(data["search_url"])):

        print(data["channel_dare"][channel_count])
        request = youtube.search().list(
            part= "snippet",
            order= "date",
            type= "video",
            eventType="live",
            channelId= data["search_url"][channel_count]
        ).execute()
        print(f"{request}\n")
        if int(request["pageInfo"]["totalResults"]) != 0:
            # print(request["items"][0]["id"]["videoId"])
            print(f'{yt_video}{request["items"][0]["id"]["videoId"]}')
            channel_live.append(f'{yt_video}{request["items"][0]["id"]["videoId"]}')
        # channel_infor.append(request)
    print(channel_live)
    return channel_live

    print("owari~")


def channel_viedo_upcoming():
    with open('./package.json', 'r') as tttt:
        packD = json.load(tttt)
        DEVELOPER_KEY = packD["YTapi_token"]
        tttt.close()
    
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    send_tuuchi = []  # save apiget
    free_chat_list = []
    # taikichU = []
    mou_tuuchi = []

    with open('./search_infor.json') as inforJS:
    # with open('../search_infor_forTEST.json') as inforJS:
        data = json.load(inforJS)
        inforJS.close()
        free_chat_list.append(data["free_chat_aru"])
        print(free_chat_list)

    with open('./dynamic_taiki.json', 'r') as dynamicc:
        taikichU = json.load(dynamicc)
        dynamicc.close()



    for channel_count in range(len(data["search_url"])):
        channel_FreeChat = ''.join(free_chat_list[0][channel_count])
        print(data["channel_dare"][channel_count])
        request = youtube.search().list(
            part= "snippet",
            order= "date",
            type= "video",
            eventType="upcoming",
            channelId= data["search_url"][channel_count]
        ).execute()
        # print(f"{request}\n")
        if int(request["pageInfo"]["totalResults"]) != 0:
            totalResu = int(request["pageInfo"]["totalResults"])

            for num in range(totalResu):
                # print(f"num = {num}")
                have_send = False
                taikiID = request["items"][num]["id"]["videoId"]
                # print(channel_FreeChat)
                if channel_FreeChat != taikiID:

                    # print(request["items"][num]["id"]["videoId"])
                    for dy_check_num in range(len(taikichU)):
                        print(f"taikiSTR: {taikichU[dy_check_num]}")
                        print(f"taikiID: {taikiID}")
                        if taikichU[dy_check_num] == taikiID:

                            have_send = True
                            break
                    if have_send == False:
                        print(f"* Haven't send")
                        send_tuuchi.append(taikiID)
                        mou_tuuchi.append(taikiID)

            #   因為有可能不+FC就會有2個待機室 *要等有實驗對象出來再測json!
            #     print(request["items"][num]["id"]["videoId"])
            #     send_tuuchi.extend(request["items"][num]["id"]["videoId"])
        # send_tuuchi.append(request)

    with open('./dynamic_haisin.json', 'r') as haisinn:
        haisinnchU = json.load(haisinn)
        haisinn.close()
    for aaa in range(len(taikichU)):
        ima_haisin = False
        for bbb in range(len(haisinnchU)):
            if taikichU[aaa] == haisinnchU[bbb]:
                ima_haisin = True
                break
        if ima_haisin == False: mou_tuuchi.append(taikichU[aaa])
    # send_tuuchi.append(taikichU)
    print(f"send: {send_tuuchi}")
    print(f"taikichu: {mou_tuuchi}")

    with open('./dynamic_taiki.json', 'w') as dynamicc:
        json.dump(mou_tuuchi, dynamicc)
        dynamicc.close()
    return send_tuuchi


if __name__=="__main__":
    # send = []
    # send.append('VEsVdmsTYyE')
    # send.append('iX6VmSL1YOA')
    #
    # with open('../dynamic_taiki.json', 'w') as dynamicc:
    #     json.dump(send, dynamicc)
    #     dynamicc.close()


    # channel_viedo_live()
    channel_viedo_upcoming()
