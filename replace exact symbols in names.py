import  os

DIR = 'D:/Python/Python_life_hacks/Rename_Files/PiC - Copy'

def rename_files(find_dir):
    for root, dirs, files in os.walk(find_dir):
        for name in files:
            rename_file(root, name)

def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)

def get_valid_name(name):
    """ replace ("replace what", "replace with")
    you can right here as many rules as you need """
    name = name.replace("00", "x")
    return name

rename_files(DIR)