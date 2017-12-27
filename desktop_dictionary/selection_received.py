# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class GetSelectionExample(object):
    def __init__(self):
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.set_title("Get Selection")
	window.set_border_width(10)
	window.connect("destroy", gtk.main_quit)
	
	vbox = gtk.VBox(False, 0)
	window.add(vbox)
	vbox.show()

	button = gtk.Button(u"Output the chosen strings")
 	eventbox = gtk.EventBox()
	eventbox.add(button)
	button.connect_object("clicked", self.get_stringtarget, eventbox)
	eventbox.connect("selection_received", self.selection_received)
	vbox.pack_start(eventbox)
	eventbox.show()
	button.show()
	window.show()
    
    def get_stringtarget(self, widget):
	widget.selection_convert("PRIMARY", "STRING")
	return

    def selection_received(self, widget, selection_data, data):
	if str(selection_data.type) == "STRING":
	    print u"The chosen string:" + selection_data.get_text()
	elif str(selection_data.type) == "ATOM":
	    targets = selection_data.get_targets()
	    for target in targets:
         	name = str(target)
		if name is not None:
		    print "%s" % name
		else:
		    print "(bad target)"
	else:
	    print "Selection was not returned as \"STRING\" or \"ATOM\"!"

def main():
    gtk.main()
    return 0

if __name__ == '__main__':
    GetSelectionExample()
    main()
