import os





# 判断文件是否存在
def check_file_exist(file_path):
    if not os.path.exists(file_path):
     print('file not exists :',file_path)
     return False
    else:
     print('file has exists :', file_path)
     return True

#覆盖的写文件
def write_file_over_write(file):
    with open(file,'wt') as f:   #注意：wt写操作的是文本，wb写操作的是二进制文件（音乐、视频等）
        f.write('line 1111111')  #写二进制文件：f.write(b'Hello')
        f.write('\n erqwerqwrewqe')

#读取文件：逐行读取
def read_file_by_line(file):
    with open(file,'rt') as f:     #注意：rt读取的是文本，rb读取的是二进制文件（音乐、视频等）
        for line in f:
          print("file line : ",line)

#直接读取文件全文
def read_file_by_content(file):
    """
    注意：With语句读写文件会自动有close行为，不用关心文件关闭。如要使用open等方法操作文件，记得关闭文件。
       本方法相当于以下代码：
      f = open(file,'rt')
      print('file content : ',f.read(),'\n')
      f.close()
    """
    with open(file,'rt') as f:
        print('file content : ',f.read(),'\n')

#读取文件的时候指定编码方式
def read_file_by_encode(file,encode):
    f = open(file , 'rt',encoding=encode)
   # f = open(file, 'rt', encoding=encode, errors='replace')  注意，不写errors时默认会使用UTF-8方式来读取文件，最好使用很明确的编码方式，尽量不要指定errors，否则会造成混乱和麻烦
    print('use encoding= ',encode,' to read file content : ', f.read(), '\n')
    f.close()

#打印输出到某个文件中
def print_out_to_file(file):
    with open(file,'wt') as f:   #注意，wt标识覆盖的写文件
        print('now begin to print to file ...')
        print('ewrqwerqwerqwer',file=f)



test_file = os.path.abspath('.')+'\\'+'tttt'+"\\"+'111.txt'
check_file_exist(test_file)

write_file_over_write(test_file)
read_file_by_line(test_file)
read_file_by_content(test_file)


read_file_by_encode(test_file,'ascii')



print_out_to_file(test_file)
read_file_by_content(test_file)

