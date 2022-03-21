import os

DIR = 'D:/Python/Python_life_hacks/Rename_Files/PiC - Copy'

def rename_files(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            count += 1
            exceptions(count, root, name)

def exceptions(count, root, name):
    """Rules for different file types"""
    if 'jpg' or '.jpeg' in name:
        valid_name = name.replace(str(name), f'00{count}.jpg')
        rename(root, name, valid_name)
    elif 'png' in name:
        valid_name = name.replace(str(name), f'00{count}.png')
        rename(root, name, valid_name)

def rename(root, name, valid_name):
    """ Use os.rename    - to physically change names
            os.path.join -  to create paths to the files  """
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


if __name__ == '__main__':
    rename_files(DIR)
