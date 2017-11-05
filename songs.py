import os


def list_dir(path="./songs"):

    file_list = []
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            if os.path.splitext(file)[1] == '.mp3':
                file_name = os.path.splitext(file)[0]  # filenames
                # file_name = os.path.join(path, file) #filepaths&filenames
                file_list.append(file_name)
        else:
            pass
    print(len(file_list), 'songs founded, they are: ', file_list, '\n')
    return(file_list)

if __name__ == '__main__':
    list_dir()

    # TESTING!!!!!!!!!!!!111
    print('TESTING!!!!!!!!!!!!!!!!!!!!!!')
