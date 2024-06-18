import zipfile
# 创建压缩包
# f = zipfile.ZipFile('dir_zip/zip.zip',mode="w")
# f.write("abc.txt")
# f.write("chucuo.txt")
# f.close()

# 如何解压缩
f = zipfile.ZipFile('dir_zip/zip.zip',mode="r")
# 直接全部解压说
# f.extractall('dir_zip/abc')
# 一个一个的解压说
# print(f.namelist())
for name in f.namelist():
    f.extract(name, 'dir_zip/abc')