
from paddleocr import PaddleOCR

# 初始化 OCR 模型
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# 图像路径
img_path = "./processed1.jpg"

# OCR 推理
results = ocr.ocr(img_path)
text = results[0]["rec_texts"]
print(results[0]["rec_texts"])  # 输出第一个识别结果的文本
# 输出识别结果