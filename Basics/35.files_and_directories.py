from pathlib import Path


# Absolute path
# c:\Program Files\Microsoft
# Relative path
# /usr/local/bin

path_ecom = Path("ecommerce")

# check path
print(path_ecom.exists())

# create a dir
path_new_dir = Path("new_dir")
print(path_new_dir.mkdir())

# remove a dir
path_del_dir = Path("new_dir")
print(path_del_dir.rmdir())

# display all files in a dir
path_list_of_files = Path()
for file in path_list_of_files.glob("*.py"):
    print(file)
