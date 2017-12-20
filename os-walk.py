import os
import collections

# function that prints all file names in path that is passed to function
# from https://www.blog.pythonlibrary.org/2016/01/26/python-101-how-to-traverse-a-directory/

file_names = []
for root, dirs, files in os.walk('/Users/Jane/Documents/UIUC/452/final-project/marijuanachallenge'):
    for file in files:
        if file.endswith('.txt') or file.endswith('.doc') or file.endswith('.docx') or file.endswith('.pdf') == -1:           # ignore .tmp files: not going to be made accessible to researchers
            pass
        else:
            file_names.append(os.path.join(root, file))


# figure out if there are duplicate file names in different folders within directory
# file_names_counts = collections.Counter(file_names)
# file_names_dict = dict(file_names_counts)

print(file_names)
