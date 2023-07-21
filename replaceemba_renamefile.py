
import os
def replace_emba(path):
    rename_file(path)
    for root,dirs,files in os.walk(path):
        print(files)
        for name in files:
            if name != 'docker-compose.yml':
                replace_string(os.path.join(root,name))

def rename_file(dirname):
    for root,dirs,files in os.walk(dirname):
        for name in files:
            name = os.path.join(root,name)
            newName = name.replace("emba","zyb")
            os.rename(name,newName)
            print(newName)
def replace_string(emfile) : 
    with open(emfile,'r',encoding='utf-8', errors='ignore') as oldfile:
        lines = oldfile.readlines()
    with open(emfile,'w',encoding='utf-8', errors='ignore') as newfile:
        for str in lines:
            restr = str.replace('emba','dc').replace('github','dc').replace('e-m-b-a','d-c').replace('EMBA','DC')
            newfile.write(restr)
    oldfile.close()
    newfile.close()
    print("done")


if __name__ == '__main__':
    print(os.getcwd())
    replace_emba("H:\\123\\321")