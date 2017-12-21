# final-project

<b>IS452
Final Project README


Introduction</b>

My final project ended up taking the form of a few files—several scripts, two spreadsheets, and a new access file. I have included more files in GitHub than are actually part of the completed project. Several extra scripts are included to show some of the additional work that went into the final submission. 

The original goal of the project was to append metadata to access files for researchers using born-digital material in an archive and to do some simple redaction. Redaction ended up being a bit overly ambitious, so I scrapped that component fairly early in the project.

<b>Run the code!</b>

file_count_by_type.py

Option 1: file path provided by user; .py must also be found at that file path

Option 2: use the file path commented out in script (line 11)

create_access_file.py

No input is required from user, but you must have droid_profile_md5_included.csv file to run script and you must have already created “access files” in the current directory that contains create_access_files.py and droid_profile_md5_included.csv.

<b>More information about the scripts:</b>

file_count_by_type.py

- input: file path provided by user, or file path commented out in script (line 11)
- output: two .txt files – file_type_output.txt & file_paths_output.txt

This script returns a list of files and file paths in a directory as well as a count of how many files of a certain number of file types are present in that directory. 

create_access_file.py
- input: no input required from user, but must have droid_profile_md5_included.csv file to run script and must have already created “access files” in current directory
- output: droid_metadata_for_access_files.csv & access file, The Bill of Rights as a Constitution_access-file.txt

In order to run this program, two things already have to be in place: the droid_profile_md5_included.csv and an empty folder called “access files” in the current directory. This program creates a subset of the metadata in the DROID profile .csv and appends it to a .txt file, which is a copy of a born-digital item in a theoretical manuscript collection, and then creates an access file for users.

<b>Calling the two functions!</b>

After defining these two fairly long functions, I was able to call the functions. I provided the two arguments in the script, rather than asking for user input since there are a lot of moving pieces in this program. I would expect/hope that someone who was using this program would be familiar enough with what’s going on here to provide the two arguments as input if that turns out to be more efficient than editing the script itself.
