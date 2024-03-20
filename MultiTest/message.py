import requests
#
# my_headers = {
#
# }

url = "https://vdept3.bdstatic.com/mda-nadbjpk0hnxwyndu/720p/h264_delogo/1642148105214867253/mda-nadbjpk0hnxwyndu.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1710834446-0-0-cd872a3d4eebb49f4a4f3de6ab1942c0&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=2846620178&vid=5423681428712102654&klogid=2846620178&abtest="

# my_params = {
#
# }
# res = requests.get(url, headers=my_headers, params=my_params)
res = requests.get(url)

# print(":::", res.content)

with open("美女视频.mp4", "wb") as file:
    file.write(res.content)