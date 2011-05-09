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

# Author  : Simos Xenitellis <simos@gnome.org>, 2010

PROGNAME='gnome-l10n-merge-html'

PACKAGE_NAME    = 'GNOME L10n Translator Stats'
PACKAGE_VERSION = '0.1'
PACKAGE_AUTHORS = ['Simos Xenitellis <simos@gnome.org>']
PACKAGE_COPYRIGHT = 'Copyright 2010 Simos Xenitellis'

import re
import polib

class MergeHTMLPO:
    def __init__(self):
      self.files = '/home/user/Dropbox/el/FILES'
      self.basename = '/home/user/Dropbox'
      pass

    def convert(self):
      f = open(self.files)
      filelist = f.readlines()

      for n in filelist:
        name = n.rstrip('\n')
        print "Working on", name
        self.parse(self.basename + '/en/' + name, self.basename + '/el/' + name)

    def parse(self, filepath1, filepath2):
      """
      Parses two HTML files and extracts the messages.
      """
      fileold = polib.pofile(filepath1)
      filenew = polib.pofile(filepath2)

      if len(fileold) == len(filenew) and len(fileold) != 0:
        count = len(fileold)

        for i in range(0, count):
           print 'msgid "' + fileold[i].msgid + '"'
           print 'msgstr "' + filenew[i].msgid + '"'
           print 
      else:
        print "Unequal", len(fileold), len(filenew)

if __name__ == '__main__':
      a = MergeHTMLPO()
      #a.parse('file1.po', 'file2.po')
      #a.parse('/tmp/evolution.gnome-3-0.el.po', '/tmp/evolution-gnome-3-0-po-el-238573.po')
      #a.parse('/tmp/hamster-applet.master.el.po', '/tmp/hamster-applet-master-po-el-4852.po')
      #print a.parse('file1.po')
      a.convert()
#      a.parse('/tmp/english.po', '/tmp/greek.po')

