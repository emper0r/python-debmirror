#!/usr/bin/python
# Author: Tony Pe a <emperor.cu@gmail.com>
# License: GPLv3
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import os
import re

class MainWindow():
    def __init__(self):
        self.glade = gtk.glade.XML("./glades/UI.glade")
        self.window = self.glade.get_widget('MainWindow')
        self.window.connect('destroy', gtk.main_quit)

        self.exit_btn = self.glade.get_widget("btn_exit")
        self.exit_btn.connect("clicked", gtk.main_quit)

        self.btn_accept = self.glade.get_widget("btn_accept")
        self.btn_accept.connect("clicked", self.make_mirror)

        self.protocol = self.glade.get_widget("protocol")
        self.protocol.connect("changed", self.check_proto)

        self.distr = self.glade.get_widget("distr")
        self.distr.connect("changed", self.check_distr)

        self.branch = self.glade.get_widget("branch")
        self.branch.connect("changed", self.check_branch)

        self.prox_set = self.glade.get_widget("prox_set")
        self.prox_set.connect("changed", self.check_prox_set)

        self.check_main = self.glade.get_widget("check_main")
        self.check_contrib = self.glade.get_widget("check_contrib")
        self.check_nonfree = self.glade.get_widget("check_non-free")
 	
        self.host_entry = self.glade.get_widget("host_entry")
        self.port_entry = self.glade.get_widget("port_entry")
        self.user_entry = self.glade.get_widget("user_entry")
        self.pass_entry = self.glade.get_widget("pass_entry")

        self.origin = self.glade.get_widget("origin_entry")
        self.destiny = self.glade.get_widget("filechooser")

        self.window.show_all()

    def check_proto(self, widget):
        if self.protocol.get_active_text() == 'http' or 'ftp':
            self.origin.set_sensitive(True)

    def check_distr(self, widget):
        self.branch.set_sensitive(True)

    def check_branch(self, widget):
        self.check_main.set_sensitive(True)
        self.check_contrib.set_sensitive(True)
        self.check_nonfree.set_sensitive(True)

    def check_prox_set(self, widget):
        if self.prox_set.get_active_text() == "Yes":
            self.host_entry.set_sensitive(True)
            self.port_entry.set_sensitive(True)
            self.user_entry.set_sensitive(True)
            self.pass_entry.set_sensitive(True)
        else:
            self.host_entry.set_sensitive(False)
            self.port_entry.set_sensitive(False)
            self.user_entry.set_sensitive(False)
            self.pass_entry.set_sensitive(False)
 	
    def make_mirror(self, widget):
        origin = self.origin.get_text()
        branch = self.branch.get_active_text()
        protocol = self.protocol.get_active_text()
        distr = self.distr.get_active_text()

        if self.check_main.get_active() == True:
            main = "main,"
        else:
            main = ""

        if self.check_contrib.get_active() == True:
            contrib = "contrib,"
        else:
            contrib = ""

        if self.check_nonfree.get_active() == True:
            non_free = "non-free"
        else:
            non_free = ""

        destiny = self.destiny.get_current_folder()

        log = "> python-debmirror-gtk.log &"

        cmd = "debmirror --cleanup -v --allow-dist-rename --host=" + str(origin) + " --root=" + str(distr) + \
            " --arch=i386 --method=" + str(protocol) + " --dist=" + str(branch) + \
            " --section=" + main + contrib + non_free + " --nosource \
            --ignore-missing-release -ignore-release-gpg --diff=none " + str(destiny) + log

        self.progress_bar = self.glade.get_widget("progress_bar")
        self.progress_bar.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
        self.progress_bar.pulse()
        self.progress_bar.set_fraction(0.0)

        os.system(cmd)
        lines = []

        while 1:
            log = open("python-debmirror-gtk.log", 'r')
            log.xreadlines()
            #lines = log.strip('\r\n')

            if re.match('\[\d+\%\]+', lines):
                number = re.sub('\D?', "", lines)
                per = float(int(number)) / 100.0
                self.progress_bar.set_fraction(per)
            else:
                print lines
            log.close()

    def run(self):
        gtk.main()

def main():
    main_window = MainWindow()
    main_window.run()
if __name__ == "__main__":
    main()
