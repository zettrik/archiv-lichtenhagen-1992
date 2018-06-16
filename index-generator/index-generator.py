#!/usr/bin/env python3
import os
#import datetime
import logging
import helper.read_zotero_csv

class LH92:
    """ foo """
    def __init__(self):
        return

    def read_csv(self, csv_file):
        """ read csv file """
        foo = helper.read_zotero_csv.zotero_csv(csv_file)
        # fetch all csv data as they were exported from zotero
        #csv_data = foo.get_raw_csv_data()
        # fetch the data for all import sites, ready for the wiki
        csv_data = foo.get_prepared_csv_data()

        return csv_data

    def create_markdown_page(self, csv_data):
        """ create one single page in markdown syntax for mkdocs
        """
        pagetext = ""
        pagetext += "#Ereignisgeschichte\n"
        # begin range with 1 to skip csv head and end with +1
        for row in range(1, len(csv_data[1:])+1):
            #print(csv_data[row])
            # skip empty rows
            if csv_data[row]:
                """
                title = "%s" % self.get_title(csv_data, row)
                #TODO skip row if pagename is empty
                print("\n%s -- %s -- %s --" % \
                    (str(datetime.datetime.now()), \
                    row, str(title)))
                """
                titletext = self.convert_csv2pagetext(csv_data, row)
                #print(titeltext)
                pagetext += titletext
        print(pagetext)
        return

    def get_title(self, csv_data, row):
        """ return the title of an entry in the given row
            todo: return some value if empty
        """
        signature = ""
        for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                #print("Feld: %s" % field)
                #print("%s: %s" % (csv_data[0][field], csv_data[row][field]))

                if csv_data[0][field] == "Signatur":
                    logging.info("Signatur: %s" % csv_data[row][field])
                    #print("Signatur: %s" % csv_data[row][field])
                    signature = csv_data[row][field]
        return signature


    def convert_csv2pagetext(self, csv_data, row):
        """
        change some csv fields before putting them in markdown
        """
        text = ""

        for field in range(len(csv_data[0])):
                # print title
                if csv_data[0][field] == "Titel":
                    #print("Titel: %s" % csv_data[row][field])
                    text += "### **%s**\n" % csv_data[row][field]

        for field in range(len(csv_data[0])):
                # separate authors
                if csv_data[0][field] == "Autor_in":
                    #print(csv_data[row][field])
                    for tag in csv_data[row][field][:]:
                        #print(tag)
                        text += "* Autor_in: %s\n" % tag

        for field in range(len(csv_data[0])):
                # separate authors
                if csv_data[0][field] == "Date":
                    #print(csv_data[row][field])
                    text += "* Datum: %s\n" % csv_data[row][field]

        for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                # separate tags
                if csv_data[0][field] == "Tag":
                    text += "* Tags: "
                    #print(csv_data[row][field])
                    for tag in csv_data[row][field][:]:
                        #print(tag)
                        text += "%s, " % tag
                    text += "\n"

        for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                #print("Feld: %s" % field)
                #print("%s: %s" % (csv_data[0][field], csv_data[row][field]))
                # check if there is more than one file attachment
                if csv_data[0][field] == "Dateianhang":
                    # separate multiple files in several attributes
                    text += "* Dateien:\n"

                    for filepath in csv_data[row][field][:]:
                        filename = ("%s" % os.path.basename(filepath))
                        text += "\t* %s\n" % (filename)
                        """ for now skip file handling 
                        # upload and link into page, if image exists
                        if os.path.isfile(filepath):
                            #text += "\t* %s %s\n" % (csv_data[0][field], filename)
                            #self.upload_file(filename, filepath)
                            # upload ocr from jpg, if ocr exists
                            if os.path.splitext(filename)[1] == ".jpg":
                                filename_ocr = os.path.splitext(filename)[0] + ".txt"
                                #print("ocr filename %s": % filename_ocr)
                                filepath_ocr = os.path.splitext(filepath)[0] + ".txt"
                                #print("ocr filepath %s": % filepath_ocr)
                                if os.path.isfile(filepath_ocr):
                                    text += "\t* %s\n" % (filename_ocr)
                                    #self.upload_file(filename_ocr, filepath_ocr)
                        """


        # handle all other fields
        text += "* Details:\n"
        for field in range(1, len(csv_data[1:])):
        #for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                if not csv_data[0][field] == "Tag" \
                and not csv_data[0][field] == "Dateianhang" \
                and not csv_data[0][field] == "Autor_in" \
                and not csv_data[0][field] == "Titel" \
                and not csv_data[0][field] == "Date" \
                and not csv_data[0][field] == "Signatur" \
                and csv_data[0][field]:
                    newrow = "\t* %s: %s\n" % (csv_data[0][field], csv_data[row][field])
                    #print(newrow)
                    text += newrow

        # finally put signature at the end of this title 
        for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                # use signature attribute as category for wikipage
                if csv_data[0][field] == "Signatur":
                    logging.info("* Signatur: %s" % csv_data[row][field])
                    #print("Signatur: %s" % csv_data[row][field])
                    text += ("* Signatur: *%s*" % csv_data[row][field])
                    #signature =  csv_data[row][field]
                    #category = signature.split("-")
                    #text += "* Kategorie: %s-%s\n" % (category[0], category[1])

        text += "\n\n"
        return text


if __name__ == "__main__":
    """ foo """
    doit = LH92()
    csv = doit.read_csv("little.csv")
    #print(csv)
    doit.create_markdown_page(csv)

