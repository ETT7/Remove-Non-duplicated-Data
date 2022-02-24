import os
import shutil
import logging
path = os.path.join(os.getcwd(),'before')
path2 = os.path.join(os.getcwd(),'after')
fileList = []
folderList = []
fileList2 = []
folderList2 = []
justFile = []
justFolder = []
justFile2 = []
justFolder2 = []
logging.basicConfig(filename="deleted.log", 
					format='%(asctime)s %(message)s', 
					filemode='a+')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
def main():
    for root, dirs, files in os.walk(path):
        for folder in dirs:
            folderList.append(os.path.join(root,folder))
        for file in files:
            fileList.append(os.path.join(root,file))

    for root, dirs, files in os.walk(path2):
        for folder2 in dirs:
            folderList2.append(os.path.join(root,folder2))
        for file2 in files:
            fileList2.append(os.path.join(root,file2))

    for name in folderList:
        name.replace('//', '\\')
        justFolder.append(os.path.relpath(name, path))
    # print("justFolder",justFolder)
    for name in fileList:
        name.replace('//', '\\')
        justFile.append(os.path.relpath(name, path))
    # print("justFile",justFile)

    for name in fileList2:
        name.replace('//', '\\')
        justFile2.append(os.path.relpath(name, path2))
    # print("justFile2",justFile2)
    for name in folderList2:
        name.replace('//', '\\')
        justFolder2.append(os.path.relpath(name, path2))
    # print("justFolder2",justFolder2)

    difFile = list(set(justFile) - set(justFile2))
    # print("difFile",difFile)
    difFolder = list(set(justFolder) - set(justFolder2))
    delete(sorted(difFile, key=len), sorted(difFolder, key=len, reverse=True))
    # print("difFolder",difFolder)

def delete(difFile, difFolder):
    f= open("deleted.log","w+")
    f.write("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓*DELETED FILES↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n\n")
    f.close()
    if not difFile:
        print("0 File to Delete\n削除対象のファイルが存在しませんでした")
        logger.info("0\n削除対象のファイルが存在しませんでした")
    else:
        for name in difFile:
            try:
                print("Deleted Files :",os.path.join(path, name))
                logger.info(os.path.join(path, name))
                os.remove(os.path.join(path, name))
            except OSError as e:
                pass
                print("ファイル削除時のエラー: ", e)
    
    f= open("deleted.log","a")
    f.write("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓DELETED FOLDERS↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n\n")
    f.close()

    if not difFolder:
        print("0 Folder to Delete\n削除対象のフォルダが存在しませんでした")
        logger.info("0\n削除対象のフォルダが存在しませんでした")
    else:
        for name in difFolder:
            try:
                print("Deleted Folders :",os.path.join(path, name))
                logger.info(os.path.join(path, name))
                shutil.rmtree(os.path.join(path, name))
            except OSError as e:
                pass
                print("フォルダ削除時のエラー: ", e)

if __name__ == "__main__":
    main()




    

    



