import os

class DirTest(object):

    def printOsParams(self):
        print('---> os.name ; ', os.name)
        print('---> os.altsep ; ', os.altsep)
        print('---> os.extsep ; ', os.extsep)
        print('---> os.st ; ', os.st)
        print('---> os.os.environ.values() ; ', os.environ.values())
        print('---> os.environ.get(\'PATH\') ; ', os.environ.get('PATH'))
        print('---> os.path.abspath(\'.\') ; ', os.path.abspath('.'))

    def create_dir(self,path_name):
        if os.path.exists(path_name):
            print('path has exists ')
        else:
            os.mkdir(path_name)

    def delete_dir(self,path_name):
        if os.path.exists(path_name):
            os.rmdir(path_name)

    def get_last_ext_name(self,file_name):
        if os.path.isfile(file_name):
            return os.path.splitext(file_name)

    def create_file(self,file_name):
        if os.path.isfile(file_name):
            print('file has exists!')
        else:
            with open(file_name,'w') as wf:
              print('file has been created ')

    def rename_file(self,file_name_orginal,file_name_new):
        if file_name_orginal==file_name_new:
            print('the name you want to change is the same as original file')
        elif os.path.isfile(file_name_new):
            print('file has exists!')
        else:
            os.rename(file_name_orginal,file_name_new)

    def delete_file(self,file_name):
        if os.path.isfile(file_name) | os.path.exists(file_name):
            os.remove(file_name)



dt = DirTest()

# print os's parameters
# dt.printOsParams()

test_dir = os.path.abspath('.')+'\\'+'tttt'
dt.create_dir(test_dir)
# dt.delete_dir(test_dir)


new_file = test_dir+"\\"+'test.txt'
dt.create_file(new_file)
print('the file : '+new_file+' \'s last ext name = ',dt.get_last_ext_name(new_file)[1])
change_name_file = test_dir+"\\"+'111.txt'
dt.rename_file(new_file,change_name_file)
dt.delete_file(change_name_file)
