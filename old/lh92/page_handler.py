# -*- coding: utf-8  -*-
"""
This is the bot for Lichtenhagen 1992 archive.

The following parameters are supported:

&params;

-dry              If given, doesn't do any real changes, but only shows
                  what would have been changed.

"""

from __future__ import unicode_literals

__version__ = '$Id: 23dac2badba93914592c50e95d72c53d7d2d7ea7 $'
#

import pywikibot
from pywikibot import pagegenerators
from pywikibot import i18n

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class BasicBot:
    # Edit summary message that should be used is placed on /i18n subdirectory.
    # The file containing these messages should have the same name as the caller
    # script (i.e. basic.py in this case)

    #def __init__(self, generator, dry):
    def __init__(self):
        """
        Constructor.

        Parameters:
            @param generator: The page generator that determines on which pages
                              to work.
            @type generator: generator.
            @param dry: If True, doesn't do any real changes, but only shows
                        what would have been changed.
            @type dry: boolean.
        """
        #self.generator = generator
        self.dry = False

        # Set the edit summary message
        #site = pywikibot.Site()
        #self.summary = i18n.twtranslate(site, 'basic-changing')

    def run(self):
        """Process each page from the generator."""
        for page in self.generator:
            self.insert_text(page)

    def insert_text(self, csv_data, row):
        """insert given csv values"""

        if csv_data[row][0] == '"Key"':
            return

        newsite = pywikibot.Site()
        pagename = "SandKasten-%s" % (csv_data[row][0])
        print("Creating new page: %s" % pagename)
        newpage = pywikibot.Page(newsite, pagename)
        text = ""
        newrow = ""

        for field in range(len(csv_data[0])):
            if csv_data[row][field]:
                print(field)
                print("%s: %s" % (csv_data[0][field], csv_data[row][field]))
                newrow = "[[%s::%s]]" % (csv_data[0][field], csv_data[row][field])
                text += newrow
                text += "\n\n"

        text += "\n\n[[Kategorie:II-B-2]]\n\n"

        #newpage.put(text)
        #newpage.save
        try:
            newpage.text = text
            # Save the page
            newpage.save(summary="foo", botflag=True)
        except pywikibot.LockedPage:
            pywikibot.output(u"Page %s is locked; skipping." % page.title(asLink=True))
        except pywikibot.EditConflict:
            pywikibot.output( u'Skipping %s because of edit conflict' % (page.title()))
        except pywikibot.SpamfilterError as error:
            pywikibot.output( u'Cannot change %s because of spam blacklist entry %s' % (page.title(), error.url))

        #pywikibot.output(u"Page %s created." % pagename)

        print("\n")

        return 


    def load(self, page):
        """Load the text of the given page."""
        try:
            # Load the page
            text = page.get()
        except pywikibot.NoPage:
            text = "<<placeholder-new-page>>"
            newsite = pywikibot.Site()
            newpage = pywikibot.Page(newsite, page.title())
            newpage.put(text)
            pywikibot.output(u"Page %s does not exist; creating."
                             % page.title(asLink=True))
            return text
        except pywikibot.IsRedirectPage:
            pywikibot.output(u"Page %s is a redirect; skipping."
                             % page.title(asLink=True))
        else:
            return text
        return None

    def save(self, text, page, comment=None, minorEdit=True,
             botflag=True):
        """Update the given page with new text."""
        # only save if something was changed
        if text != page.get():
            # Show the title of the page we're working on.
            # Highlight the title in purple.
            pywikibot.output(u"\n\n>>> \03{lightpurple}%s\03{default} <<<"
                             % page.title())
            # show what was changed
            pywikibot.showDiff(page.get(), text)
            pywikibot.output(u'Comment: %s' % comment)
            if not self.dry:
                if pywikibot.input_yn(
                        u'Do you want to accept these changes?',
                        default=False, automatic_quit=False):
                    try:
                        page.text = text
                        # Save the page
                        page.save(summary=comment or self.comment,
                                  minor=minorEdit, botflag=botflag)
                    except pywikibot.LockedPage:
                        pywikibot.output(u"Page %s is locked; skipping."
                                         % page.title(asLink=True))
                    except pywikibot.EditConflict:
                        pywikibot.output(
                            u'Skipping %s because of edit conflict'
                            % (page.title()))
                    except pywikibot.SpamfilterError as error:
                        pywikibot.output(
                            u'Cannot change %s because of spam blacklist entry %s'
                            % (page.title(), error.url))
                    else:
                        return True
        return False


def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: list of unicode
    """
    # Process global arguments to determine desired site
    local_args = pywikibot.handle_args(args)

    # This factory is responsible for processing command line arguments
    # that are also used by other scripts and that determine on which pages
    # to work on.
    genFactory = pagegenerators.GeneratorFactory()
    # The generator gives the pages that should be worked upon.
    gen = None
    # If dry is True, doesn't do any real changes, but only show
    # what would have been changed.
    dry = False

    # Parse command line arguments
    for arg in local_args:
        if arg.startswith("-dry"):
            dry = True
        else:
            genFactory.handleArg(arg)

    if not gen:
        gen = genFactory.getCombinedGenerator()
    if gen:
        # The preloading generator is responsible for downloading multiple
        # pages from the wiki simultaneously.
        gen = pagegenerators.PreloadingGenerator(gen)
        bot = BasicBot(gen, dry)
        bot.run()
    else:
        pywikibot.showHelp()

if __name__ == "__main__":
    main()
