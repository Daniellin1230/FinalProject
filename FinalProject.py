import http
import requests
import json
# 取得Token
def get_access_token():
    #API網址    
    url = "https://account.kkbox.com/oauth2/token" 
    
    #標頭
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "account.kkbox.com"
    }

    #參數
    data = {
        "grant_type": "client_credentials",
        "client_id": "69fbb5e71ccaa65eeabcf44fc836f246",
        "client_secret": "d7faf2523f4ed5d4262d0cf92ef9c75a"
    }

    access_token = requests.post(url, headers=headers, data=data)#像api請求憑證
    #print(access_token.text)
    return access_token.json()["access_token"]

def get_charts():
    
    access_token = get_access_token()    #取得存取憑證
    url = "https://api.kkbox.com/v1.1/charts" #取得音樂排行榜列表API網址
    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token  #帶著存取憑證
    }
    #參數
    params = {
        "territory": "TW"  #台灣領域  
    }
    response = requests.get(url, headers=headers, params=params) #向api發出請求得到資烙
    result = response.json()["data"]    
    for item in result:       
        print(item["id"], item["title"])
get_charts()

def get_charts_tracks(chart_id):
    
    access_token = get_access_token()    #存取憑證 
    
    url = "https://api.kkbox.com/v1.1/charts/" + chart_id + "/tracks"#取得音樂排行榜列表中的歌曲API網址
    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }
    #參數
    params = {
        "territory": "TW"  #台灣領域
    }
    response = requests.get(url, headers=headers, params=params)
    #print(response.text)
    result = response.json()["data"]
    
    for item in result:
        print([item["name"], item["url"]])

def singer():
    access_token = get_access_token()#取得憑證
    conn = http.client.HTTPSConnection("api.kkbox.com")#連接到kkbox

    headers = {
        'accept': "application/json",
        'authorization': "Bearer "+access_token 
        }


    print("輸入查詢歌手(only english name): ")
    singer = input()
    print("-----------------------------------------------------------------------------------")
    offeset=1
      
    url="/v1.1/search?q="+singer+"&type=track&territory=TW&offset="+str(offeset)+"&limit=50" #取得查詢api
    conn.request("GET", url, headers=headers) #對api發出請求
    
    res = conn.getresponse() #得到api的資料
    
    data = res.read()                  #
    str123=str(data, "utf-8")          #將bytes的資料改成json
    json123 = json.loads(str123)       #
    for i in range(50):    
        print(json123["tracks"]["data"][i]["name"], "  ",json123["tracks"]["data"][i]["url"])
        print("-----------------------------------------------------------------------------------")
    #print(data.decode("utf-8"))
    

print("===========================================")
try:
    chart_id = input("請貼上想聽的音樂排行榜ID: ")
    get_charts_tracks(chart_id)
except KeyError:
    print("請貼上正確的音樂排行榜ID")

print("===========================================")
singer()
