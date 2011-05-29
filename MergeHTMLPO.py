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
# For xml2po code, 
#  Copyright (c) 2004, 2005, 2006 Danilo Šegan <danilo@gnome.org>.
#  Copyright (c) 2009 Claude Paroz <claude@2xlibre.net>.

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
    
      # Default parameters
      self.default_mode = 'docbook'
      self.operation = 'pot' # 'pot', 'merge', 'update'
      self.options = { 'mark_untranslated'   : False, 'expand_entities'     : True, 'expand_all_entities' : False }

    def convert(self):
      f = open(self.files)
      filelist = f.readlines()

      good = 0
      bad = 0

      for n in filelist:
        name = n.rstrip('\n')
        print "Working on file", name
        file1 = self.basename + 'en/' + name + '.html'
        file1out = self.basename + 'en/' + name + '.po'
        file2 = self.basename + 'el/' + name + '.html'
        file2out = self.basename + 'el/' + name + '.po'
        file3 = self.basename + 'output/' + name + '.po'
        #print "Files:", file1, file2

        try:
            #print 'default_mode:', self.default_mode, 'operation:', self.operation, 'options:', self.options
            xml2po_file1 = xml2po.Main(self.default_mode, self.operation, file1out, self.options)
            xml2po_file2 = xml2po.Main(self.default_mode, self.operation, file2out, self.options)
        except IOError:
            print >> sys.stderr, "Error: cannot open file %s for writing." % (output)
            sys.exit(1)

        # Standard POT producing
        #print 'About to produce PO files for', file1, file2
        xml2po_file1.to_pot([file1])
        xml2po_file2.to_pot([file2])

        if self.parse(file1out, file2out):
          good = good + 1
        else: 
          bad = bad + 1
          
      print good, "good files and", bad, "bad files."

    def parse(self, filepath1, filepath2):
      """
      Parses two HTML files and extracts the messages.
      """
      fileold = polib.pofile(filepath1)
      filenew = polib.pofile(filepath2)

      #print "  Number of messages: ", len(fileold), len(filenew)
      if len(fileold) == len(filenew) and len(fileold) != 0:
        print "    Matching: ", len(fileold), len(filenew)
        count = len(fileold)

        for i in range(0, count):
           pass
           #print 'msgid "' + fileold[i].msgid + '"'
           #print 'msgstr "' + filenew[i].msgid + '"'
           #print 
        return True
      else:
        print "    NOT matching:", len(fileold), len(filenew)
        return False


if __name__ == '__main__':
      a = MergeHTMLPO()
      #a.parse('file1.po', 'file2.po')
      #a.parse('/tmp/evolution.gnome-3-0.el.po', '/tmp/evolution-gnome-3-0-po-el-238573.po')
      #a.parse('/tmp/hamster-applet.master.el.po', '/tmp/hamster-applet-master-po-el-4852.po')
      #print a.parse('file1.po')
      a.convert()
#      a.parse('/tmp/english.po', '/tmp/greek.po')
