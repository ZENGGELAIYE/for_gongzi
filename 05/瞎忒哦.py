import shutil
# 可以移动文件
# 把文件夹dir1中的文件移动到dir2中
# shutil.move("dir1/123.txt",'dir2') # 相对于想在的路劲，想转移的位置

# 复制文件
# f1 = open("dir2/123.txt",mode="rb")
# f2 = open("dir1/1234.txt",mode='wb') # 文件1中没有文件先得创建一个
# shutil.copyfileobj(f1,f2) # 把文件f1复制到文件f2

# 执行两个文件路径，进行文件复制
# 只是复制文件的内容并没有复制文件的权限
# shutil.copyfile("dir1/1234.txt","dir1/a.txt")

# 复制文件内容+权限一起复制
# shutil.copy("dir1/a.txt","dir1/1.txt")

# 复制文件内容 + 权限 + 修改权限
# shutil.copy2("批扣.py","dir1/a.py")

# 修改时间，权限的复制，不复制内容
# shutil.copystat('批扣.py','dir1/1.txt')
#
# # 只拷贝权限
# shutil.copymode('.','dir1/1.txt')

# # 复制文件夹
# # shutil.copytree('dir1','dir3')
# # 删除文件夹
# shutil.rmtree("dir3")