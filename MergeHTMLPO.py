#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Copyright (c) 2011, Simos Xenitellis <simos@gnome.org>.

PROGNAME='gnome-l10n-merge-html'

PACKAGE_NAME    = 'GNOME L10n Translator HTML Merge tool'
PACKAGE_VERSION = '0.1'
PACKAGE_AUTHORS = ['Simos Xenitellis <simos@gnome.org>']
PACKAGE_COPYRIGHT = 'Copyright 2011 Simos Xenitellis'

import re
import polib
import xml2po

class MergeHTMLPO:
    def __init__(self):
      self.files = 'FILES'
      self.basename = ''
    
    def convert(self):
      f = open(self.files)
      filelist = f.readlines()

      good = 0
      bad = 0

      for n in filelist:
        name = n.rstrip('\n')
        print "Working on file", name
        file1out = self.basename + 'en/' + name + '.po'
        file2out = self.basename + 'el/' + name + '.po'
        file3out = self.basename + 'output/' + name + '.po'

        print 'Files:', file1out, file2out
        if self.parse(file1out, file2out, file3out):
          good = good + 1
        else: 
          bad = bad + 1

      print good, "good files and", bad, "bad files."

    def parse(self, filepath1, filepath2, filepath3):
      """
      Parses two HTML files and extracts the messages.
      """
      fileold = polib.pofile(filepath1)
      filenew = polib.pofile(filepath2)

      #print "  Number of messages: ", len(fileold), len(filenew)
      if len(fileold) == len(filenew) and len(fileold) != 0:
        print "    Matching: ", len(fileold), len(filenew)
        count = len(fileold)

        outputfile = open(filepath3, 'w')

        outputfile.write("""
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"POT-Creation-Date: 2011-05-29 13:05+0300\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n" """)

        outputfile.write('\n\n')

        for i in range(0, count):
           print >> outputfile, 'msgid "' + self.removenums(fileold[i].msgid) + '"'
           print >> outputfile, 'msgstr "' + self.removenums(filenew[i].msgid) + '"'
           print >> outputfile

        outputfile.close()
        return True
      else:
        print "    NOT matching:", len(fileold), len(filenew)
        return False

    def removenums(self, message):
      if re.match('\d+\.', message):
        return message[message.find(' ')+1:]
      else:
        return message

if __name__ == '__main__':
      a = MergeHTMLPO()
      #a.parse('file1.po', 'file2.po')
      #a.parse('/tmp/evolution.gnome-3-0.el.po', '/tmp/evolution-gnome-3-0-po-el-238573.po')
      #a.parse('/tmp/hamster-applet.master.el.po', '/tmp/hamster-applet-master-po-el-4852.po')
      #print a.parse('file1.po')
      a.convert()
#      a.parse('/tmp/english.po', '/tmp/greek.po')
