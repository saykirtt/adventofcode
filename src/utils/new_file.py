from os.path import exists

def new_file(year,day):

    path = f'src/{year}/day{day:02d}.py'

    if not exists(path):

        FILE_CONTENT = f"filename = 'inputs/{year}/day{day:02d}'\n\nwith open(filename,'r') as file:\n\tdata =file.read()"

        with open(path,"w") as f:
            f.write(FILE_CONTENT)