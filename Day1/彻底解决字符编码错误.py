
# with open(file) as f:

# with open(file, ‘r’, encoding=‘utf-8’) as f:


# with open(file, ‘r’, encoding=‘utf-8’,errors='ignore') as f:


import chardet

# 修改单文件的编码
def file_format(file, target_bm):
    with open(file, 'rb+') as f:
        conent = f.read()  # 二进制的形式

        bm = chardet.detect(conent)['encoding']  # 获取编码
        if bm:
            conent = conent.decode(bm).encode(target_bm)

        f.seek(0)
        f.write(conent)


# https://www.cnblogs.com/zz22--/p/8799071.html