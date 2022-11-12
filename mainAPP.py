import cmAPI
import time
import os 


global minecraftModsDir, modpacksArray
minecraftModsDir = ""
modpacksArray = ["defaultValue"]

class craftManager:
    def __init__(self):
        ...

    def mainGui(self):
        os.system("cls")
        print("""                 __ _  ___  ___                                  
                    / _| | |  \/  |                                  
    ___ _ __ __ _| |_| |_| .  . | __ _ _ __   __ _  __ _  ___ _ __ 
    / __| '__/ _` |  _| __| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
    | (__| | | (_| | | | |_| |  | | (_| | | | | (_| | (_| |  __/ |   
    \___|_|  \__,_|_|  \__\_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                                                    __/ |          
                                                    |___/           """)

        print("active modpack: ",cmAPI.verifyActiveModpack(minecraftModsDir))
        # Aqui é a interface inicial, o interessante aqui é que getlogin retorna o nome do usuario logado na maquina
        print(f"Welcome {os.getlogin()} to CraftManager \n1. Create Modpack\n2. Chose Modpack\n4. Modify Modpack")
        option = input("> ")
        match option:
            case "1":
                self.CreateModpack()
            case "2":
                self.chooseModpack()
                self.mainGui()
            case "3":
                self.iniConfig()
            
            case "break":
                exit()
            case _:
                print("Invalid Option")
                time.sleep(1.6) 
                self.mainGui()


    def CreateModpack(self):
        os.system("cls")
        print("CreateModpack:","-- MODPACK CREATION --")    
        modpackName = input("Name Your Modpack: ")    
        # Aqui o user tem que colocar o endereço da pasta onde os mods que ele quer fazer o modpack estão alocados
        actualModsDir = input(r"Where are the mods: ")
        # criar pasta com do modpack
        # mover todos os itens da pasta atual para a nova
        cmAPI.createDir(modpackName, os.path.join(ROOT_DIR, "modpacksFolder"))
        cmAPI.createFile("modpackInfo.txt", os.path.join(ROOT_DIR, "modpacksFolder", modpackName), modpackName)
        cmAPI.moveAllFiles(actualModsDir, os.path.join(ROOT_DIR, "modpacksFolder", modpackName))
        self.mainGui()



    def chooseModpack(self):
        print("--Choose your modpack--")
        count = 1
        for modpack in modpacksArray[1:]:
            print(f"{count}. {modpack}")
            count += 1
        choice = int(input("> "))
        modpackChosen = modpacksArray[choice]
        os.system("cls")
        print("chooseModpack DEBUG: ",modpackChosen)
        # identificar se lá dentro da pasta mods do mine tem um modpack ativo
        # se o resultado for none, significa que não achou modpackInfo, Ent vai pegar todos aqueles mods e jogar na pasta UnknowMods
        if cmAPI.verifyActiveModpack(minecraftModsDir) == "None or Unknown":
            cmAPI.moveAllFiles(minecraftModsDir, os.path.join(ROOT_DIR, "unknowData"))
        else:
            cmAPI.moveAllFiles(minecraftModsDir, os.path.join(ROOT_DIR, "modpacksFolder", cmAPI.verifyActiveModpack(minecraftModsDir)))
        # se retornar algo alem disso tem um modpack lá dentro, botar ele de volta na pasta
        
        # mover mods do modpack escolhido para a modsDir
        cmAPI.moveAllFiles(os.path.join(ROOT_DIR, "modpacksFolder", modpackChosen), minecraftModsDir)
        





if __name__ == "__main__":
    os.system("cls")
    # verifica se temos a localização de modsDir e load
    ROOT_DIR = os.path.abspath(os.curdir)
    if "modsDirLoc.txt" in os.listdir(ROOT_DIR):
        with open(os.path.join(ROOT_DIR, "modsDirLoc.txt"), 'r+') as file:
            if file.read() == "":
                modsDir = input(r"where is your .minecraft mods directory: ")
                file.write(modsDir)
            else:
                # vai pra linha 0 de novo
                file.seek(0)
                # Carrega o endereço da pasta pra minecraft variavel
                minecraftModsDir = file.read()
    else:
        ...
    
    # Carrega todos os modpacks pra memoria
    if "modpacksFolder" in os.listdir(ROOT_DIR):
        for modpack in os.listdir(os.path.join(ROOT_DIR, "modpacksFolder")):
            modpacksArray.append(modpack)
    else:
        print("LOADCONFIG ERROR: modpacksFolder not found")
    if "unknowData" in os.listdir(ROOT_DIR):
        ...
    else:
        os.makedirs(os.path.join(ROOT_DIR, "unknowData"))

    app = craftManager()
    app.mainGui()
                

                    
# SISTEMA DE CRIAR MODPACKS