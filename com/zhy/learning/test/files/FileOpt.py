

class FileTest(object):


    def setFilePath(self,file_path):
        self.__file_path = file_path

    def read_file1(self):
        try:
            f = open(self.__file_path,'r')
            print(f.read())
        finally:
            if f:
                f.close()

    def read_file2(self):
        with open(self.__file_path,'r') as f:
            print(f.read())

#注意：read_file1和read_file2等效

    def read_file_lines(self):
        with open(self.__file_path,'r') as f:
              for line in f.readlines():
                 print(line.strip())

#注意：read_file_lines读取的数据没有格式


    def write_file_rewrite(self):
        with open(self.__file_path,'w') as wf:
            wf.write("Hello Write")

    def write_file_appendwrite(self):
        with open(self.__file_path,'a') as af:
            af.write("Hello Write")






f_test = FileTest()
f_test.setFilePath('D:\\temp\\dangbei.txt')


# Test Reading File
# print('read_file1 : ......\n')
# f_test.read_file1()
# print('\n')
#
# print('read_file2 : ......\n')
# f_test.read_file2()
# print('\n')
#
#
#
# print('read_file_lines : ......\n')
# f_test.read_file_lines()
# print('\n')


#Test Writing File
# f_test.write_file_appendwrite()
# f_test.read_file2()

# f_test.write_file_rewrite()
# f_test.read_file2()