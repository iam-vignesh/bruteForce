from itertools import product
import zipfile
from tqdm import tqdm 

combo = (product([0,1,2,3,4,5,6,7,8,9],repeat = 6))

with open("passwordcombo.txt", "w") as f:
    for item in combo:
        combo_string = "".join(map(str,item))
        f.write(combo_string)
        f.write("\n")

print("\nAll password combinations generated! Write Complete. \n")
print("\n --------------------------------------------------------------- \n")

password_List = "passwordcombo.txt"
zip_File = zipfile.ZipFile("C:\\Users\\Vignesh\\Downloads\\secret.zip")
print("\n Matching passwords from the list now... \n")

with open(password_List, "rb") as passwordList:
    for password in tqdm (passwordList, unit = "password"):
        try:
            zip_File.extractall(pwd = password.strip())
        except:
            continue
        else:
            print(" [+] Password Found: ", password.decode().strip())
            break










