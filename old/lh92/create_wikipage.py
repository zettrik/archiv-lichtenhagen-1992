#!/usr/bin/env python3
import pywikibot

class create_wikipage:
    def __init__(self):
        self.site = pywikibot.Site()
        return


    def insert_text(self, pagename, pagetext, comment):
        page = pywikibot.Page(self.site, pagename)
        if page.exists():
            print("Overwriting existing page: '%s'" % pagename)
            print(" last edit by %s at %s " % (page.userName(), page.editTime()))
        else:
            print("Creating new page: '%s'" % pagename)
        '''
        if page.exists():
            print("The page '%s' already exists." % pagename)
            print("Last edit by %s at %s " % (page.userName(), page.editTime()))
            answer = input("May I overwrite it (y/n)? ")
            if answer != "y":
                print("cancelling...")
                exit(1)
        '''

        page.text = pagetext # insert text in page
        page.save(comment)  # save the page
        ''' writing in async mode is faster but harder to debug '''
        #page.save(comment, async = True)  # save the page in background

    def replace_text(self, pagename, oldtext, newtext, comment):
        page = pywikibot.Page(self.site, pagename)
        page.text = page.text.replace(oldtext, newtext)
        page.save(comment)  # save the page

    def show_text(self, pagename):
        page = pywikibot.Page(self.site, pagename)
        print(page.text) # show page content


    def delete_page(self, pagename):
        page = pywikibot.Page(self.site, pagename)
        page.delete(reason='delete test', mark = True) # delete page


## for debugging, tests...
if __name__ == "__main__":
        pagename = "SandKasten2"
        testtext = "foomakilla"
        newtext = "faamokillo"
        comment = "test"

        foo = create_wikipage()
        foo.insert_text(pagename, testtext, comment)
        foo.show_text(pagename)
        foo.replace_text(pagename, testtext, newtext, comment)
        foo.show_text(pagename)
        foo.delete_page(pagename)
        foo.show_text(pagename)
