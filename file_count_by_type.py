# identify files and folders
# count the number of word processing documents in the directory: .txt, .doc/.docx, .pdf

# import OS module so that we can access files on the underlying operating system
import os

# Get file directory path from user
path = input('Please enter the full file path, including the first / of the path, here: ')

# Or, use the file path that I used to test this script.
# path = "/Users/Jane/Documents/UIUC/452/final-project/marijuanachallenge"

# os.listdir will get us all of the stuff at path
dirs = os.listdir(path)

# create empty lists where we'll pull together the files and folders
file_list = []
folder_list = []

file_paths_output = open('file_paths_output.txt', 'w')

# iterate through everything in the top level folder to see what's a file and what's a folder
for item in dirs:
    file_name = item
    file_path = path + '/' + file_name

    # if the thing is a file, append it to the file list; this only gets us the files in the top level folder
    if os.path.isfile(file_path) == True:
        # append each file to the list of files
        file_list.append(file_name)

        #file_path = folder_path + '/' + file_name
        print(file_name + ': ' + file_path, file=file_paths_output)

    #if the thing is a folder, append it to the folder list
    else:
        folder_list.append(file_name)

# iterate through every folder in the list of folders
for folder in folder_list:
    # create the full folder path for each folder
    folder_path = path + '/' + folder
    # get all the things at each of the folder paths
    folder_dirs = os.listdir(folder_path)

    # iterate through every item in every folder; this will get us to the files in subfolders
    for item in folder_dirs:
        # append each file to the list of files
        file_list.append(item)
        file_path = folder_path + '/' + file_name
        print(item + ': ' + file_path, file=file_paths_output)

# create empty lists to store files of each document type
txt_files = []
doc_docx_files = []
pdf_files = []
other_file_types = []

# iterate through all the files in the file list
for file in file_list:
    if file.endswith('.txt'):
        txt_files.append(file)
    elif file.endswith('.doc' or '.docx'):
        doc_docx_files.append(file)
    elif file.endswith('.pdf'):
        pdf_files.append(file)
    else:
        other_file_types.append(file)

# open a new output file
file_type_output = open('file_type_output.txt', 'w')

# print to output file
print('Number of files of each file type:\n.txt files:', len(txt_files), '\n.doc and .docx files:', len(doc_docx_files), '\n.pdf files:', len(pdf_files), '\nall other file types:', len(other_file_types), file=file_type_output)

