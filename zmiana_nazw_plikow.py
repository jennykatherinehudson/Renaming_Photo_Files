import os

def change_files_names(dir, main_name):
    list_of_elements = os.listdir(dir)
    new_file_names = []
    new_file_numbers = [ i for i in range(1, len(list_of_elements)+1)]

    for number in new_file_numbers:
        if len(str(number)) == 1:
            new_number = main_name + '00' + str(number) + '.jpg'
            new_file_names.append(new_number)
        elif len(str(number)) == 2:
            new_number = main_name +'0' + str(number) + '.jpg'
            new_file_names.append(new_number)
        else:
            new_number = main_name + str(number) + '.jpg'
            new_file_names.append(new_number)

    for i, j in zip(list_of_elements,new_file_names):
        old_name = os.path.join(dir, i)
        new_name = os.path.join(dir, j)
        os.rename(old_name, new_name)
    return print('The renaming files has been processed successfully!')

dir = r'E:\Python\zmiana_nazw_for_Iwona'
main_name = '2017_dress_'

change_files_names(dir, main_name)


