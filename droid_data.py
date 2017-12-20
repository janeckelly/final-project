# I figured out how to work with .csv files by using a Python textbook I cataloged in my 507 class :)
# Irv Kalb, "Learn to Program with Python"

# import csv module
import csv

def droid_data_for_access_file(file_name):
    # open csv file with DROID data
    droid_csv_file = open(file_name, 'rU')

    # read csv file so that it's parsed into rows
    DROIDcsvParsed = csv.reader(droid_csv_file)

    # create empty list to store the header fields
    header = []

    # set readingHeaderLine to true (got this from Kalb textbook)
    readingHeaderLine = True

    # pull together all data in csv in a list of lists in which each list = one row of csv
    all_rows = []

    # iterate through all rows in parsed csv file
    for row in DROIDcsvParsed:
        # skip header line in csv file
        if readingHeaderLine:
            readingHeaderLine = True
            header.append(row)          # append header info to empty header list

        # if not reading header line, continue reading the file
        if readingHeaderLine:
            readingHeaderLine = False
            continue

        # append all individual rows from csv as a list to one big list
        all_rows.append(row)

        # create empty list to store metadata of interest in one place
        all_rows_metadata = []

    # iterate through every row in all_rows
    for row in all_rows:
        # identify and pull together the metadata of interest into one item, which is a tuple
        row_metadata_tuple = row[3], row[4], row[7], row[8], row[9], row[10], row[12], row[14], row[15], row[16], row[17]

        # convert tuple to a list to make it easier to work with
        row_metadata_list = list(row_metadata_tuple)

        # append list of metadata values to list
        all_rows_metadata.append(row_metadata_list)


    # clean up header info by turning into list
    header_clean = list(header[0])

    # create list of headers that we want; matches up with the metadata values identified above
    header_fields_for_access_file = header_clean[3], header_clean[4], header_clean[7], header_clean[8], header_clean[9], header_clean[10], header_clean[12], header_clean[14], header_clean[15], header_clean[16], header_clean[17]


    # iterate through each row from all rows of metadata
    for row in all_rows_metadata:
        for count, item in enumerate(row):           # enumerate adds counter to iterable variable so i can grab item from row and keep track of count in order to use that count to index into header fields
            header = header_fields_for_access_file[count]       # get header value based on the count we're at as we iterate through
            if item == '':                          # if item has no value, set item value equal to n/a
                item = 'n/a'
            else:
                item = item                        # if item has a value, keep value of item as is
            print(header + ': ' + item)             # join together the header and item to get header name: metadata value
        print('\n')                                 # print hard return between row's metadata values

    droid_csv_file.close()                          # close droid_csv_file


    # this section writes the metadata to a csv file so that it can be reused if needed in the future
    # got help for this section from Python docs: https://docs.python.org/3/library/csv.html
    # and some Google searching that took me here: https://www.blog.pythonlibrary.org/2014/02/26/python-101-reading-and-writing-csv-files/
    # and here: https://stackoverflow.com/questions/40170262/python-typeerror-argument-1-must-have-a-write-method

    # open new file to write data to
    with open('droid_metadata_for_access_files.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # write header row to the csv
        writer.writerow(header_fields_for_access_file)
        # for each line in the rows of metadata, write line to csv file
        for line in all_rows_metadata:
            writer.writerow(line)

# run this function using a specific csv file
droid_data_for_access_file('droid_profile_md5_included.csv')
