# [Teachable Machine 快速建立第一個 AI 模型](https://teachablemachine.withgoogle.com/?utm_source=chatgpt.com)

Teachable Machine 是 Google 推出的免費 AI 訓練平台。

不需要：

- Python
- TensorFlow
- GPU
- 程式設計

只要透過瀏覽器即可完成：

```
收集資料
↓
訓練模型
↓
測試模型
↓
匯出模型
```

因此非常適合：

- AI 入門教學
- 學校課程
- 專題原型(PoC)
- 快速驗證想法

適合：
✅ 影像分類

不適合：
❌ 物件偵測：圖片裡有幾個人？
❌ 影像分割：裂縫面積多大？
❌ 物件追蹤：人從哪裡進來？

## Teachable Machine 三種專案

建立專案時會看到三種模式。

### Image Project(影像辨識)

```
輸入圖片、攝影機畫面
輸出這是什麼
```

例如：

- 貓狗辨識
- 戴口罩辨識
- 手勢辨識
- 剪刀石頭布

### Audio Project(聲音辨識)

```
輸入麥克風、音訊檔
輸出這是什麼聲音
```

例如：

- 鼓掌
- 打噴嚏
- 咳嗽
- 狗叫聲

### Pose Project(姿勢辨識)

```
輸入人體骨架
輸出目前動作
```

例如：

- 深蹲
- 舉手
- 開合跳
- 站立

## 實作：剪刀石頭布辨識

- 點擊：Get Started
- 選擇：Image Project
- 選擇模型：Standard Image Model即可。
- 建立類別：將預設類別改成：

```
剪刀
石頭
布
```

![alt text](./Teachable_Machine_assets/處裡類別.png)

- 開始訓練：點擊：Train Model
- 測試模型：訓練完成後。右側會出現：Preview攝影機畫面。
- 匯出模型：點擊：Export Model
  - TensorFlow.js：它可以直接在瀏覽器執行。因此最適合：HTML、JavaScript、網頁作品。
  - TensorFlow：
  - TensorFlow Lite：
- 結合 Gemini 生成網頁

```
請使用 HTML、CSS、JavaScript

幫我設計一個現代化 AI 辨識網站

需求：

1. 使用 Teachable Machine 模型
2. 顯示攝影機畫面
3. 顯示辨識結果
4. 顯示信心分數
5. 使用玻璃擬態風格
6. 支援手機版

以下是模型程式碼：

(貼上 Teachable Machine 程式碼)
```
