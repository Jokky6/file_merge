import os

file_dir = os.getcwd()+'/markdown'
#获取当前文件夹中的文件名称列表
file_names=os.listdir(file_dir)
#打开当前目录下的result.md文件，如果没有则创建
file=open('result.md','w')
#先遍历文件名
for file_name in file_names:
    file_path = file_dir+'/'+file_name
    for line in open(file_path):
        print(line)
        file.writelines(line)
    file.writelines('\n')
    # print(file)
    #遍历单个文件，读取行数
#关闭文件
file.close()