#!/usr/bin/env python3
import pywikibot
import os.path

class create_filepage:
    def __init__(self):
        return

    def upload_file(self,filepage, filepath, comment):
        print("filepage: %s" % filepage)
        print("filepath: %s" % filepath)
        print("comment: %s" % comment)
        if not os.path.isfile(filepath):
            print("File does not exist or is unreadable: %s" % filepath)
            exit(1)

        ## The site we want to run our bot on. Define the name in user-config.py
        site = pywikibot.Site()
        page = pywikibot.FilePage(site, filepage)
        page.text = comment
        page.save('')

        ## upload local file
        try:
            site.upload(page, source_filename=filepath, ignore_warnings=True) 
            print("upload successful: %s" % filepath)
        except pywikibot.data.api.UploadWarning as upload_warning:
            print(page.fileUrl()) 
            print(page.usingPages()) 
            print(page.get_file_history()) 
            print("error: %s" % upload_warning)
            print("!File has not been saved!")
        except:
            print("some error occurde while uploading a file")


## for debug tests...
if __name__ == "__main__":
    filepage = "SandKasten-testupload.txt"
    filepath = "/data/zotero-export/zote.txt" 
    comment = "test"

    foo = create_filepage()
    foo.upload_file(filepage, filepath, comment)
