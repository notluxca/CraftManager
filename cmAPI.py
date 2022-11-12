from genericpath import isdir
import shutil
import os


# Criar pasta com um nome numa localização especifica
def createDir(name, location):
    if isdir(fr"{location}"):
        try:
            path = os.path.join(fr"{location}", name)
            os.makedirs(path)
        except OSError as error:
            print("createDir: ERROR, ",error)
        


# Criar arquivo com nome localização e data(coisas dentro do arquivo)
def createFile(name, location, data):
    if os.path.exists(location):
        try:
            with open(os.path.join(location, name), 'w') as f:
                f.write(data)
        except Exception as error:
            print(error)
    else:
        print("createFile: ERROR, Localização não existe")



def moveAllFiles(source, dest):
    mods = os.listdir(source)
    for file in mods:
        shutil.move(os.path.join(source, file), dest)



# def verifyActiveModpack(folder):
#     try:
#         for file in os.listdir(folder):
#             if file == "modpackInfo.txt":
                
#                 with open(os.path.join(folder, "modpackinfo.txt"), "r", encoding='UTF-8') as file:
#                         return file.read()
#             else:
#                 return "Unknow or none"
#     except Exception as error:
#         print("ERROR: verifyActivemodpack, ", error)
            
            
def verifyActiveModpack(folder):
    files = os.listdir(folder)
    if "modpackInfo.txt" in files:
        with open(os.path.join(folder, "modpackinfo.txt"), "r", encoding='UTF-8') as file:
            return file.read()
    else:
        return "None or Unknown"






#fazendo o sistema de mover todos os arquivos de uma pasta para uma determinada localização

