#!/usr/bin/env python3
import csv
import sys
import os.path

class create_markdown:
    def __init__(self, csv_file):
        if os.path.isfile(csv_file):
                self.file = csv_file
        else:
            self.file = ""
            print("File '%s' does not exist or is unreadable." % csv_file)
            sys.exit(1)


    def get_raw_csv_data(self):
        """ return a dictionary with content of the csv file
        """
        csv_content = open(self.file,'r')
        try:
            csv_raw_data = list(csv.reader(csv_content))

        finally:
            csv_content.close()

        return(csv_raw_data)


    def get_prepared_csv_data(self):
        """ do some nasty conversations from zotero relicts
            and prepare for wikipagetext
        """
        csv_data = self.get_raw_csv_data()
        #print("Head of csv file: ")
        #print(csv_data[0][0:])

        """
        translate zotero keys to the mediawiki attributes we want
        you can put more in here...
        """
        transtable = [["Title", "Titel"],  \
                        ["Author", "Autor_in"]]
        # just change the keys in the first row (0=csv head)
        for key in range(len(csv_data[0][0:])):
            for transkey in range(len(transtable[0:])):
                if csv_data[0][key] == transtable[transkey][0]:
                    csv_data[0][key] = transtable[transkey][1]
        #print("New head of csv file: ")
        #print(csv_data[0][0:])

        """
        change the path(s) of the file attachments
        and split them if multiple fields were given
        """
        oldpath = "/media/age/fubus/age.extern/zotero"
        newpath = "/data/zotero-export"
        # skip the first row (0=csv head) and start with first real entry
        for row in range(1, len(csv_data[0:])):
            for i in range(len(csv_data[row][0:])):
                if csv_data[row][i]:
                    #print(row)
                    #print("%s: %s" % (csv_data[0][i], csv_data[row][i]))
                    if csv_data[0][i] == "Dateianhang":
                        files = csv_data[row][i].replace(oldpath, newpath)
                        # if there is more than one file than make a list out of it
                        #todo: make sure that no empty entries get in here and test if file exists before adding to csv_data
                        filelist = files.split("; ")
                        files = list(filter(None, filelist))
                        csv_data[row][i] = files
                        #print("filelist: " + str(filelist))
                        #print("files: " + str(files))
                        #for i in range(len(files)):
                            #print("--" + files[i] + "---\n")
                        #print("replaced filepath: ")
                        #print("%s: %s" % (csv_data[0][i], csv_data[row][i][0:]))

        """
        split up zoteros "manual tags" field
        """
        for row in range(1, len(csv_data[0:])):
            for i in range(len(csv_data[row][0:])):
                if csv_data[row][i]:
                    #print(row)
                    #print("%s: %s" % (csv_data[0][i], csv_data[row][i]))
                    if csv_data[0][i] == "Tag":
                        tags = csv_data[row][i].split("; ")
                        csv_data[row][i] = tags
                        #print("%s: %s" % (csv_data[0][i], csv_data[row][i][0:]))
        """
        split up zoteros "authors" field
        """
        for row in range(1, len(csv_data[0:])):
            for i in range(len(csv_data[row][0:])):
                if csv_data[row][i]:
                    #print(row)
                    #print("%s: %s" % (csv_data[0][i], csv_data[row][i]))
                    if csv_data[0][i] == "Autor_in":
                        tags = csv_data[row][i].split("; ")
                        csv_data[row][i] = tags
                        #print("%s: %s" % (csv_data[0][i], csv_data[row][i][0:]))
 
        #print(csv_data[0][0:])
        #print(csv_data[1][0])
        return(csv_data)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        print("usage: %s archivbereiche.csv" % sys.argv[0])
        sys.exit(1)

    foo = create_markdown(filename)
    csv_raw_data = foo.get_raw_csv_data()
    csv_data = foo.get_prepared_csv_data()
