# Shopping-JCircle

# 購物網站-吉嗑就圓 使用指南

## 版本說明

**Version 0726 :** 初版(首次上傳版本)

**Version 1221  :** 二版(資料庫優化: 正規化1NF~BCNF / 商品分類欄位優化 / 首頁隨機商品顯示優化) 

## 網站技術說明

1. 以**Vue.js** 進行前端編寫，搭配**CSS、Html**進行頁面及各種功能製作，透過**Axios**向後端發送請求，以Vue.component搭載頁面，透過Vue.Router完成頁面路由轉發。
2. 以**Django**透過**RESTful API**方式進行API進行後端處理邏輯編寫，同時搭配**MySQL**數據庫進行數據操作，最後將處理結果返回到頁面進行渲染。
3. 在**AWS雲端伺服器**上，將Django編寫的後端代碼透過**uWSGI**進行代理，同時搭配**nginx**進行Vue.js前端代碼的掛載，來完成整體項目在伺服器上的佈署。
4. 透過**串接綠界金流API**，實現信用卡線上付款及超商代碼繳費付款功能，增加付款繳費的便利性。
5. 透過**v-if**、**v-bind** 方式，來選擇調整頁面中即時小窗的顯示，或是調整不同狀態訂單顯示，來增加用戶使用網頁時的便利性。
6. 透過**Python裝飾器**應用，來減少後端驗證用戶登入所需要編寫的代碼，增加整體效能以及便利性。

## 網站介面說明

### 一、上方導覽區

1. 註冊

```
輸入相對應資料進行個人帳號註冊，正常註冊時，皆為一般會員註冊，特定情況才會由官方進行賣場會員資格開通。

```

1. 登入

```
輸入會員帳號與密碼，點擊登入後，傳送數據到後端，與數據庫內部數據比對，核對正確則顯示登入正確，同時後端返回透過帳號
與特定Key加密的token，儲存在網頁中，作為登入狀態紀錄。

```

1. 搜尋列

```
輸入關鍵字，按下按鈕，透過關鍵字搜尋現有數據庫，於視窗中顯示商品，點擊詳細內容，可以於視窗中顯示商品詳細資料。

```

1. 購物車圖示

```
可以進入購物車總覽頁面，顯示當前加入購物車商品，以及數量、金額等資訊，可點選結帳進入結帳頁面。

```

1. 導覽列

```
點擊不同項目進入不同頁面，一般用戶皆會顯示首頁、我的帳戶及我的訂單三種選項，只有賣場用戶會多一個我的賣場選項。
在未登入情況下點擊首頁以外的其他項目，會自動導向用戶登入畫面。

```

### 二、首頁

1. 網頁麵包屑

```
會隨著頁面變換而變換，

```

1. 商品分類導覽

```
點擊商品種類，於視窗中顯示選擇的商品種類的商品。

```

1. 商品跑馬燈

```
從目前上架的商品中隨機顯示4樣出來，每15秒會進行一次替換。

```

1. 購物車預覽/瀏覽紀錄

```
未登入狀態下，只會顯示瀏覽紀錄，最多顯示三個瀏覽紀錄，點擊詳細內容，可以於視窗中顯示商品詳細資料。
登入狀態下，才會有購物車內容預覽，在瀏覽商品時，可以同時知道購物車中有甚麼商品跟目前商品總金額為多少，可以不用為了
查看購物車內容而切換頁面。

```

### 三、商品相關頁面

1. 商品總覽

```
將關鍵字搜尋或是選擇到商品分類的商品，一併顯示在區塊中，提供給用戶瀏覽，點擊詳細內容則可以直接進入到商品詳細頁面。

```

1. 商品詳細內容

```
顯示商品名稱、圖片、內容、金額、數量以及付款方式，可以點擊加減符號調整數量，最後按下加入購物車，將商品加入購物車內。

```

### 四、購物車

1. 購物車總覽

```
顯示當前加入購物車商品，以及數量、金額等資訊，可點選結帳進入結帳頁面。

```

1. 購物車結帳

```
顯示訂單編號、成立時間、訂購商品的相關資訊以及費用的明細，輸入相關訂購人資訊，點擊結帳，創立訂單並進入確認結帳頁面。

```

1. 確認結帳

```
再次顯示訂單資料與訂購人資訊，給訂購人確定訂單資訊無誤，點擊確認送出，將資料送到綠界金流公司，同時頁面會導向綠界金流
信用卡/超商代碼繳費頁面  (由選擇的繳費方式決定)，確認完付款資訊後，點擊回到店家頁面按鈕，會導回”我的訂單頁面”。

```

### 五、我的帳戶

1. 資料顯示

```
顯示用戶名稱、生日、性別、電話、信箱以及頭像。

```

1. 資料修改

```
點擊各項資料旁的修改，會跳出相關修改資料的輸入框，輸入完畢點擊提交，送出資料，即可完成修改。
頭像部分，選擇檔案好之後，點擊上傳，便可以修改頭像。

```

### 六、我的訂單

1. 訂單總覽

```
顯示一般用戶在結帳之後，成功創立的訂單，會顯示訂單編號、狀態、時間、內容以及金額，可以點擊詳細內容觀看內容。
另外，依照各種不同訂單狀態進行分類，讓用戶更了解哪一筆訂單處於什樣的訂單狀態。

```

1. 訂單詳細內容

```
顯示訂單相關資訊，並於下方顯示訂購商品的清單。那只有一般用戶在訂單狀態處於待繳款的時候，如果反悔下訂，可以點擊刪除訂單。
當一般用戶付款，綠界公司會傳送驗證碼到後端伺服器進行驗證，確認付款正確會回傳結果給綠界公司，同時改變訂單狀態到下一階段。
付款完成後，就由賣場用戶進行出貨及到貨追蹤，同時進行修改訂單狀態，告訴一般用戶目前商品運送狀態如何。
同時有一個訂單留言板，提供給一般用戶及賣家之間做訊息溝通使用。

```

### 七、我的賣場

1. 賣場總覽

```
上方訂單管理顯示目前賣場擁有的訂單資料，點擊詳細內容可以觀看訂單詳細資料。
下方則顯示賣場目前上架的商品資料，點擊商品管理，可以進入賣場商品上架頁面。

```

1. 訂單詳細內容

```
功能與"訂單詳細內容頁面"一樣，只是觀看網頁的權限由一般用戶轉變為賣場用戶。

```

1. 賣場商品上架

```
上方可以觀看目前上架商品，可以點擊商品下方按鈕，進行修改或是刪除。
下方可以上傳商品圖片，以及輸入商品相關資訊，進行新的商品上架。

```

1. 賣場商品修改

```
將想要修改的商品資料輸入到那項資料旁邊的輸入框，在點擊確定修改，送出修改資料，完成修改。
```