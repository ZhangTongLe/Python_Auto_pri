import requests
from PIL import Image


api_key = 'fJ1yWWbXRpEFyCJU8gekp96W'
img_path = 'F:\Python自动化办公训练营\Day3\制作证件照\white_person.jpg'

id_card ='F:\Python自动化办公训练营\Day3\制作证件照\id_card.png'



# 在线更换背景，支持人像、汽车、猫狗，
# 调接口，预览模式每个月50次
def remove_online():
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img_path, 'rb')},
        data={'size': 'preview', 'bg_color': '#438EDB'},  # preview、full、auto、medium、
        headers={'X-Api-Key': api_key},
    )
    if response.status_code == requests.codes.ok:
        with open(id_card, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage():
    img = Image.open(id_card)

    # width:400 height:576
    out = img.resize((400, 576), Image.ANTIALIAS)
    # resize image with high-quality
    out.save('id_card.png')





if __name__ == '__main__':
    remove_online()
    ResizeImage()













