from os.path import exists
from os import makedirs

def new_file(year,day):
    path = f'src/{year}'
    file = path+f'/day{day:02d}.py'
    #print(path)
    if not exists(path):
        makedirs(path)

    if not exists(file):

        FILE_CONTENT = f"filename = 'inputs/{year}/day{day:02d}'\n\nwith open(filename,'r') as file:\n\tdata =file.read()"

        with open(file,"w") as f:
            f.write(FILE_CONTENT)