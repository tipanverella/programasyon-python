file_path = input(": ")
directories = 

        files = glob.iglob("/c/Users/dedea/git/programasyon-python/*.csv", recursive = True)
        if file_path not in files:
            print("Dokuman ou a pa la, map jete m!")
            sys.exit()
        else:


files = glob.iglob("/c/Users/dedea/git/programasyon-python/*.csv", recursive = True)




def find(path, name):
    for root, dirs,  files in os.walk(path):
        if name in files:
            result = os.path.join(root, name)
        return result



name = input("Ki non document ou a? ")
        file = str(find(file_path, name) )



            if name in file: