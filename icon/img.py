import os
from PIL import Image

def convert_bmp_to_png(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".bmp"):
            bmp_path = os.path.join(directory, filename)
            png_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.png")

            # 打开 BMP 图片
            bmp_image = Image.open(bmp_path)

            # 创建一个带透明背景的 RGBA 图像
            rgba_image = bmp_image.convert("RGBA")

            # 获取图像数据
            data = rgba_image.getdata()

            # 替换白色背景为透明背景
            new_data = []
            for item in data:
                # 假设白色背景的 RGB 值为 (255, 255, 255)
                if item[:3] == (255, 255, 255):
                    new_data.append((255, 255, 255, 0))  # 将白色背景转换为透明
                else:
                    new_data.append(item)

            # 更新图像数据
            rgba_image.putdata(new_data)

            # 保存为 PNG 图片
            rgba_image.save(png_path)

            print(f"Converted {filename} to {os.path.basename(png_path)}")

# 指定 BMP 文件所在目录
directory = "./"
convert_bmp_to_png(directory)
