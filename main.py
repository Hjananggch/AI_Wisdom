import time
import cv2

IMAGE_PATHS = [
    r"C:\Users\H2250\Desktop\AI&Wisdom\QAZ\C.JPG",
    r"C:\Users\H2250\Desktop\AI&Wisdom\QAZ\B.JPG",
    r"C:\Users\H2250\Desktop\AI&Wisdom\QAZ\A.JPG",
]

IMAGE_DISPLAY_TIME = 5

def display_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (600, 800))
    cv2.imshow("AI", img)
    cv2.waitKey(IMAGE_DISPLAY_TIME * 1000)

def ai_wisdom(password):
    """
    AI智慧函数

    参数:
    password (str): 密码

    返回:
    str: 返回结果
    """
    if password == "210426":
        print("Hello World!\nHello, AI&Wisdom!")

        for path in IMAGE_PATHS:
            display_image(path)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~请等待~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print("元宝：希望大家都发卷，人更卷！！！")
        print("金安：今天很开心和大家一起来到玉龙雪山的脚下写下了这一段不是很优雅的代码。希望大家天天开心~")
        return "ok"
    else:
        print("打开世界的大门错误！")

if __name__ == "__main__":
    while True:
        password = input("请输入AI&WisDom的密码：")
        output = ai_wisdom(password)
        if output == "ok":
            break
