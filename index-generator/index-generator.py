#!/usr/bin/env python3
#import os
#import datetime
import logging
import helper.read_zotero_csv
import helper.read_archivescopes_csv

class LH92:
    """ foo """
    def __init__(self):
        return

    def read_zotero_csv(self, csv_file):
        """ read zotero csv export
        """
        rawdata = helper.read_zotero_csv.zotero_csv(csv_file)
        archivdata = rawdata.get_prepared_csv_data()

        return archivdata

    def read_archivescopes_csv(self, csv_file):
        """ read csv file with archivescopes and descriptions
        """
        rawdata = helper.read_archivescopes_csv.create_markdown(csv_file)
        archivescopes = rawdata.get_prepared_csv_data()

        return archivescopes

    def create_markdown_pages(self, md_filepath, scopes, data):
        """ create single pages in markdown syntax for all scopes
        """
        allentries = 0
        print("Gesamtanzahl an Archivbereichen: " + str(len(scopes[1:])))
        for i in range(1,len(scopes[1:])):
            print(scopes[i][0:2])
            part = scopes[i][0:]
            scope = str(scopes[i][0])
            filename = str(md_filepath) + scope + ".md"
            print("writing markdown file: " + str(filename))

            with open(filename, mode='w', encoding='utf-8') as md_file:
                string = "#" + str(part[0]) + " " + str(part[1]) + "\n"
                string += str(part[2]) + "\n"
                if part[3]:
                    string += "\n* Zeitraum: " + str(part[3]) + "\n\n"
                else:
                    string += "\n"
                # write markdown head for this page
                md_file.write(string)
                # write all entries of this scope
                pagetext, entries = self.get_pagetext(scope, data)
                #print(pagetext)
                md_file.write(str(pagetext))
                allentries += entries
            print("Einträge in der Datei: %s" % entries)
        print("Gesamteinträge in der Datei: %s" % allentries)

    def create_markdown_bibo(self, md_filepath, data):
        """ create biblio page in markdown syntax
        """
        filename = str(md_filepath) + "bibliothek.md"
        print("writing markdown file: " + str(filename))
        with open(filename, mode='w', encoding='utf-8') as md_file:
            #string = "# Bibliothek\n"
            string = ""
            # write markdown head for this page
            md_file.write(string)
            # write all entries of this scope
            pagetext, entries = self.get_pagetext("Bibliothek", data)
            #print(pagetext)
            md_file.write(str(pagetext))
        print("Einträge in der Bibliothek: %s" % entries)

    def get_pagetext(self, scope, data):
        pagetext = ""
        entries = 0
        for row in range(1, len(data[1:])+1):
            #print(data[row])
            # skip empty rows
            if data[row]:
                for field in range(len(data[0])):
                    if data[row][field]:
                        #print("Feld: %s" % field)
                        #print("%s: %s" % (data[0][field], data[row][field]))
                        if data[0][field] == "Archive Location":
                            #print("Archive Location: %s" % data[row][field])
                            if data[row][field] == scope:
                                pagetext += "\n"
                                #print("Archive Location: %s" % data[row][0])
                                entries += 1
                                #pagetext += str(data[row])
                                pagetext += self.convert_csv2pagetext(data, row)
                                #print(titletext)
                if scope == "Bibliothek":
                    print("%s: %s" % (data[0][field], data[row][field]))
                    pagetext += "\n"
                    entries += 1
                    pagetext += self.convert_csv2pagetext(data, row)

                """
                title = "%s" % self.get_title(csv_data, row)
                #TODO skip row if pagename is empty
                print("\n%s -- %s -- %s --" % \
                    (str(datetime.datetime.now()), \
                    row, str(title)))
                """
        return (pagetext, entries)


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
        """ change some csv fields before putting them in markdown
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
                # separate authors
                if csv_data[0][field] == "Place":
                    #print(csv_data[row][field])
                    if csv_data[row][field]:
                        text += "* Ort: %s\n" % csv_data[row][field]

        for field in range(len(csv_data[0])):
                # separate authors
                if csv_data[0][field] == "Publication Title":
                    #print(csv_data[row][field])
                    if csv_data[row][field]:
                        text += "* Publikation: %s\n" % csv_data[row][field]

        for field in range(len(csv_data[0])):
                # separate authors
                if csv_data[0][field] == "Pages":
                    #print(csv_data[row][field])
                    if csv_data[row][field]:
                        text += "* Seiten: %s\n" % csv_data[row][field]

        for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                # separate tags
                if csv_data[0][field] == "Tag":
                    text += "* Tags: "
                    #print(csv_data[row][field])
                    for tag in csv_data[row][field][:]:
                        #print(tag)
                        text += "%s; " % tag
                    text += "\n"

        for field in range(len(csv_data[0])):
                # separate authors
                if csv_data[0][field] == "Rights":
                    if csv_data[row][field]:
                        #text += "* Nutzungsrechte: %s\n" % csv_data[row][field]
                        rights = csv_data[row][field].split(";")
                        text += "* Nutzungsrechte: " 
                        for right in rights:
                            if right == "0":
                                # unknown rights, skip whole entry
                                #print("Status unklar")
                                text += "Die Nutzungsrechte sind ungeklärt. " 
                                return "\n\n"
                            if right == "1":
                                text += "Die Nutzung bedarf einer Zustimmung durch die Geber*innen. " 
                            if right == "2":
                                text += "Die Nutzung insbesondere Reproduktion tangiert gegebenenfalls das Urheberrecht Dritter. "
                            if right == "3":
                                text += "Die Nutzung insbesondere Reproduktion tangiert gegebenfalls Persönlichkeitsrechte Dritter. Es wird entsprechend eine geschwärzte Kopie vorgelegt. "
                            #if right == "4":
                            if right == "5":
                                text += "Die Nutzung des Digitalisates insbesondere die Reproduktion bedarf des Verweises auf die Quelle. "
                        text += "\n"

        """ for now completely skip file handling 
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

        """ for now don't print any further details
        # handle all other fields
        text += "* Details:\n"
        #for field in range(2, len(csv_data[1:])):
        for field in range(len(csv_data[0])):
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
        """

        for field in range(len(csv_data[0])):
                # separate authors
                if csv_data[0][field] == "Archive Location":
                    #print(csv_data[row][field])
                    if csv_data[row][field]:
                        text += "* Fundstelle: %s\n" % csv_data[row][field]


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
    #archivedata = doit.read_zotero_csv("lichtenhagen.csv")
    #print(archivedata)
    #archivescopes = doit.read_archivescopes_csv("archivbereiche.csv")
    #print(archivescopes)

    #doit.create_markdown_pages("../lh92-index/docs/", archivescopes, archivedata)

    bibliodata = doit.read_zotero_csv("lichtenhagen_bibliothek.csv")
    #print(bibliodata)
    doit.create_markdown_bibo("../lh92-index/docs/", bibliodata)

