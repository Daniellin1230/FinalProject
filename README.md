# 開放平台軟體期末Project

## 專題介紹  
這個專題能夠讓使用者查詢有哪些音樂排行榜，利用查詢得到的id能夠再去每個排行榜，得到裡面的所有歌曲與網址，點網址就可以到kkbox的網站進行試聽，最後還可以利用歌手去搜尋歌曲，並附上歌曲的連結，利用連結去試聽。


## 創建過程
- 動機發想  
我自己很喜歡在網路上聽歌，因此就想找音樂相關的api，就找到kkbox的open api，探索後發現裡面有非常多的功能的api，而很多人聽歌時不知道聽甚麼都會從排行榜找，因此我就實作了排行榜的功能，可以從得到的排行榜連結去試聽歌曲，如果想從歌手去找音樂，也能透過搜尋的api來達成。
- 程式建構  
程式語言: Python  
需要的Python Packages: http, requests, json  
利用的APIs: KKBOX


## code詳解
- 一開始必須先去kkbox open api的網站創建帳號，取得id及密碼，  
接著進到程式裡，利用kkbox token的API，設定網址、標題、參數，把剛剛得到的id及密碼放到參數裡，  
接著就可以利用API去得到許可憑證，後面都需要用到許可憑證去使用其他API。
![image](https://github.com/Daniellin1230/FinalProject/blob/main/picture/2.PNG)        

- 接下來要取得排行榜資料，先取得許可憑證，接著要輸入kkbox 排行榜的API，  
設定好標頭跟參數，就可以向API取得排行榜的資料，接著輸出排行榜的id及名稱。
![image](https://github.com/Daniellin1230/FinalProject/blob/main/picture/5.PNG)    

- 接著要利用id搜尋排行榜上的歌，也是先取得憑證、排行榜歌曲API，設定標頭、參數，  
就可以向API請求資料，輸出歌名網址，透過網址可以上KKBOX的網站去試聽。
![image](https://github.com/Daniellin1230/FinalProject/blob/main/picture/6.PNG)

- 最後用歌手搜尋歌單，取得API，設定參數，再把搜尋歌手名稱設定到API裡面，  
就可以順利取得API資料，輸出歌單。
![image](https://github.com/Daniellin1230/FinalProject/blob/main/picture/7.PNG)

## 結果
利用搜尋到的網址，就可以到KKBOX的網站進行試聽  
![image](https://github.com/Daniellin1230/FinalProject/blob/main/picture/8.PNG)

## 參考網站
- https://docs-zhtw.kkbox.codes/#overview
