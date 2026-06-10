import gradio as gr
import numpy as np

# ==========================================
# 1. ส่วนของฟังก์ชัน Back-end (AI Inference Simulation)
# ==========================================

# ฟังก์ชันจำลองการทำงานของ NLP / Text Processing
def text_analysis_func(text, confidence_threshold, task_type):
    if not text.strip():
        return "กรุณากรอกข้อความก่อนครับ", {}, "Invalid Input"
    
    # จำลองผลลัพธ์จากโมเดล
    result_str = f"ข้อความที่ส่งมา: '{text}'ถูกประมวลผลด้วยงานประเภท [{task_type}]"
    mock_predictions = {
        "Positive (เชิงบวก)": 0.85 if confidence_threshold < 85 else 0.40,
        "Negative (เชิงลบ)": 0.10,
        "Neutral (ทั่วไป)": 0.05
    }
    status = "Success (ประมวลผลสำเร็จ)"
    return result_str, mock_predictions, status


# ฟังก์ชันจำลองการทำงานของ Computer Vision (Image Processing)
def image_processing_func(input_image, brightness_factor):
    if input_image is None:
        return None, "กรุณาอัปโหลดรูปภาพ"
    
    # จำลองการประมวลผลภาพ (เช่น การปรับความสว่างโดยใช้ numpy)
    # ภาพใน Gradio จะถูกแปลงเป็น numpy array (RGB) โดยอัตโนมัติ
    processed_img = np.clip(input_image.astype(int) + brightness_factor, 0, 255).astype(np.uint8)
    
    return processed_img, "ประมวลผลรูปภาพเสร็จสิ้น!"


# ==========================================
# 2. ส่วนของ Front-end (Gradio UI Layout)
# ==========================================

# ใช้ gr.Blocks เพื่อจัดการหน้าจอแบบอิสระ
with gr.Blocks(title="AI Project Template") as demo:
    
    # gr.Markdown: สำหรับเขียนคำอธิบายหน้าเว็บ รองรับ HTML และ Markdown
    gr.Markdown("""
    # 🚀 ระบบสาธิตการใช้งาน Gradio สำหรับโครงงาน AI
    ยินดีต้อนรับนักศึกษาทุกคน! เว็บไซต์นี้เป็นตัวอย่างรวม Component ยอดฮิตของ Gradio เพื่อให้นำไปประยุกต์ใช้กับโครงงานของตัวเอง
    """)
    
    # ------------------------------------------
    # TAB 1: ประมวลผลข้อความ (Text & NLP)
    # ------------------------------------------
    with gr.Tab("📝 Text & NLP Task"):
        gr.Markdown("### ส่วนที่ 1: ระบบวิเคราะห์ข้อความ (จำลอง)")
        
        with gr.Row():  # จัดกลุ่มให้อยู่ในแถวเดียวกัน (แบ่งซ้าย-ขวา)
            
            # --- ฝั่งซ้าย: Inputs ---
            with gr.Column():
                # gr.Textbox: กล่องรับข้อความ
                text_input = gr.Textbox(
                    label="กรอกข้อความที่ต้องการวิเคราะห์", 
                    placeholder="พิมพ์ข้อความที่นี่ เช่น 'วันนี้อากาศดีมาก'...",
                    lines=3
                )
                # gr.Slider: แถบเลื่อนปรับค่าตัวเลข (เหมาะกับค่า Threshold, Hyperparameter)
                slider_input = gr.Slider(
                    minimum=0, maximum=100, value=50, step=5,
                    label="Confidence Threshold (%)"
                )
                # gr.Dropdown: เมนูตัวเลือกแบบ Dropdown
                dropdown_input = gr.Dropdown(
                    choices=["Sentiment Analysis", "Named Entity Recognition (NER)", "Summarization"],
                    value="Sentiment Analysis",
                    label="เลือกงานของ AI (Task)"
                )
                # gr.Button: ปุ่มกดเพื่อสั่งรันฟังก์ชัน
                submit_text_btn = gr.Button("🔮 เริ่มวิเคราะห์ข้อความ", variant="primary")
            
            # --- ฝั่งขวา: Outputs ---
            with gr.Column():
                # gr.Textbox: กล่องแสดงข้อความผลลัพธ์ (ตั้ง interactive=False เพื่อไม่ให้ผู้ใช้แก้ไข)
                text_output = gr.Textbox(label="ผลลัพธ์สรุปจาก AI", interactive=False)
                # gr.Label: เหมาะสำหรับการแสดงผลลัพธ์แบบ Classification (แสดงเปอร์เซ็นต์/ความมั่นใจ)
                label_output = gr.Label(label="ระดับความเชื่อมั่น (Classification)")
                # gr.Text: กล่องสถานะสั้นๆ
                status_output = gr.Text(label="สถานะระบบ")

        # ผูกฟังก์ชันเข้ากับปุ่ม (กำหนด Inputs และ Outputs ให้ตรงกับฟังก์ชัน)
        submit_text_btn.click(
            fn=text_analysis_func,
            inputs=[text_input, slider_input, dropdown_input],
            outputs=[text_output, label_output, status_output]
        )

    # ------------------------------------------
    # TAB 2: ประมวลผลรูปภาพ (Computer Vision)
    # ------------------------------------------
    with gr.Tab("🖼️ Computer Vision Task"):
        gr.Markdown("### ส่วนที่ 2: ระบบประมวลผลรูปภาพ (จำลอง)")
        
        with gr.Row():
            # --- ฝั่งซ้าย: Inputs ---
            with gr.Column():
                # gr.Image: กล่องรับรูปภาพ (รองรับการลากวาง, อัปโหลด, หรือเปิดกล้อง)
                image_input = gr.Image(label="อัปโหลดรูปภาพที่นี่ (รองรับ .jpg, .png)", type="numpy")
                # gr.Radio: ปุ่มเลือกตัวเลือกแบบ Radio button
                radio_input = gr.Radio(
                    choices=[0, 30, 60, -50], 
                    value=30, 
                    label="ปรับระดับความสว่าง (Brightness Offset)"
                )
                submit_img_btn = gr.Button("⚡ ประมวลผลภาพ", variant="secondary")
                
            # --- ฝั่งขวา: Outputs ---
            with gr.Column():
                # gr.Image: กล่องแสดงรูปภาพผลลัพธ์
                image_output = gr.Image(label="รูปภาพผลลัพธ์จาก AI")
                img_status = gr.Textbox(label="ข้อความจากระบบ", interactive=False)
                
        # ผูกฟังก์ชันประมวลผลภาพเข้ากับปุ่ม
        submit_img_btn.click(
            fn=image_processing_func,
            inputs=[image_input, radio_input],
            outputs=[image_output, img_status]
        )

    # ------------------------------------------
    # ส่วนท้ายของเว็บ (Footer)
    # ------------------------------------------
    gr.Markdown("""
    ---
    💡 **คำแนะนำสำหรับนักศึกษา:** ลองเปลี่ยนฟังก์ชัน 'text_analysis_func' หรือ 'image_processing_func' 
    ให้เป็นฟังก์ชันที่ไปโหลดโมเดลจริงของนักศึกษามาใช้ (เช่น PyTorch, TensorFlow, HuggingFace Transformers หรือ Ultralytics YOLO)
    """)

# ==========================================
# 3. คำสั่งเปิดระบบใช้งาน (Launch)
# ==========================================
if __name__ == "__main__":
    # share=True จะสร้างลิงก์สาธารณะ (gradio.live) ให้นักศึกษาส่งงานหรือเปิดให้เพื่อนเล่นได้ชั่วคราว 72 ชม.
    demo.launch(share=False)