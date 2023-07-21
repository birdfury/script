

import os
import shutil
def delet_comm_blankline(path):
    for root,dirs,files in os.walk(path):
        #print(files)
        for name in files:
            del_commline(os.path.join(root,name))
        for file in files:
            del_blankline(os.path.join(root,file))
    del_bakfile(path)
def del_commline(emfile) : 
    with open(emfile,'r',encoding='utf-8', errors='ignore') as oldfile:
        shutil.copyfile(emfile,emfile+'.bak')
        lines = oldfile.readlines()
        #print(lines)

    with open(emfile,'a+',encoding='utf-8', errors='ignore') as newfile:
        newfile.truncate(0)
        for line in lines:
            #print(line)
            #comstr = re.findall('#(.*?)',line)
            #comstr = re.match("#",line)
            #print(comstr)
            #if not line.strip().startswith('#') or line == "#!/bin/bash -p":
            if line == "#!/bin/bash -p\n" or line == "#!/bin/bash -p \n":
                newfile.write(line)
            elif not line.strip().startswith('#'):
                newfile.write(line) 
    oldfile.close()
    newfile.close()
    print("done")
def del_blankline(emfile2) : 
    with open(emfile2,'r',encoding='utf-8', errors='ignore') as f1:
        lines = f1.readlines()
    with open(emfile2,'w',encoding='utf-8', errors='ignore') as f2:
        for l in lines:
            if l == '\n' :
                l = l.strip("\n")
            f2.write(l)
    f1.close()
    f2.close()
    print("done")
def del_bakfile(filepath):
    for file_name in os.listdir(filepath):
        if file_name.endswith('.bak'):
            os.remove(filepath +'\\'+ file_name)


if __name__ == '__main__':
    print(os.getcwd())
    delet_comm_blankline("H:\\123\\321")