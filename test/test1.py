from io import BytesIO
from captcha.image import ImageCaptcha
import os

# 创建ImageCaptcha实例
captcha = ImageCaptcha()

data: BytesIO = captcha.generate('ABCD')

output_dir = './resource/image'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file_path = os.path.join(output_dir, 'captcha.png')

with open(output_file_path, 'wb') as f:
    f.write(data.getvalue())

print(f"Captcha saved to {output_file_path}")
