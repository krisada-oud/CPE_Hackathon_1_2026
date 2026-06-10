# 🤖 AI Model Showcase with Gradio (Hackathon Starter Template)

ยินดีต้อนรับนักศึกษาทุกคนเข้าสู่โปรเจกต์ต้นแบบสำหรับแสดงผลงาน AI! 🚀 Repository นี้จัดทำขึ้นเพื่อให้ทุกทีมสามารถนำโมเดล AI ของตัวเอง มาสร้างเป็น Web Interface สวยๆ ได้อย่างรวดเร็วด้วย **Gradio** เพื่อใช้ในการ Demo ต่อหน้าคณะกรรมการ

---

## 🚀 ฟีเจอร์ของ Template นี้
* **Ready-to-Use:** โครงสร้างโค้ดเริ่มต้นที่เป็นระบบ พร้อมให้เชื่อมต่อโมเดล AI
* **Gradio UI:** หน้าเว็บอินเตอร์เฟซสำเร็จรูป รองรับการรับค่า (Input) และแสดงผล (Output)
* **Hackathon Friendly:** โค้ดไม่ซับซ้อน สามารถปรับแต่งและนำไปเปิดตัว (Deploy) บน Hugging Face Spaces ได้ง่าย

---

## 🛠️ ขั้นตอนการติดตั้งและเริ่มใช้งาน (Getting Started)

### 1. Clone โปรเจกต์
ให้นักศึกษาทำการ Fork หรือ Clone Repository นี้ไปยังเครื่องของตัวเอง
```bash
git clone https://github.com/krisada-oud/CPE_Hackathon_1_2026.git
```

### 2. การเตรียม Environment และติดตั้ง Library (เลือกวิธีที่สะดวก)
#### 2.1 ช่องทางที่ 1: ติดตั้งผ่าน Conda
```bash
# สร้าง environment ใหม่ชื่อ [YOUR_ENV_NAME] (แนะนำ Python 3.10)
conda create -n [YOUR_ENV_NAME] python=3.10 -y
  
# เปิดใช้งาน environment
conda activate [YOUR_ENV_NAME]
  
# ติดตั้ง library หลักที่ต้องใช้
conda install gradio numpy
```
#### 2.2 ติดตั้งผ่านไฟล์คอนฟิกสำเร็จรูป (requirements.yml / environment.yml)
```bash
# ในกรณีที่มีไฟล์ข้อกำหนดมาให้แล้ว ให้รันคำสั่งนี้เพื่อสร้าง env ทันที
conda env create -f requirements.yml
  
# เปิดใช้งาน environment
conda activate [YOUR_ENV_NAME]
```

## ขอให้ทุกท่านสนุกกับกิจกรรมในครั้งนี้ ขอบคุณครับ
