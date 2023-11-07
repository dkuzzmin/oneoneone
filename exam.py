from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

print("Lets hack")

flag = False
for i in range (97,123):
    if flag:
        break
    for n in range (97,123):
        find_me = chr(i)+chr(n)
        secret_password = find_me + 'bcmpda' 
        print(secret_password)
        flag = unzip_with_7z(zip_file_path,dest_path,secret_password)
        if flag:
            print("Password is: ", secret_password)
            break



