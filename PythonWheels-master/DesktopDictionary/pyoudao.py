#-*- coding: utf-8 -*-

import os
import re
import time
import fcntl
import logging
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import webkit
import requests
import json

HOME = os.getenv("HOME") + '/.youdao-dict/'
LOG = HOME + '/pyoudao.log'
LOCK = HOME +  '/pyoudao.lock'

QUERY_URL = 'http://fanyi.youdao.com/openapi.do?keyfrom=tinxing&key=1312427901&type=data&doctype=json&version=1.1&q='

if not os.path.exists(HOME):
    os.mkdir(HOME)

logging.basicConfig(filename=LOG, level=logging.DEBUG)

class Dict:
    def __init__(self):
        self.mouse_in = False
        self.popuptime = 0
        self.last_selection = ''

        self.window = gtk.Window(gtk.WINDOW_POPUP)
        self.window.set_title("pyoudao")
        self.window.set_border_width(3)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.resize(360, 200)

        vbox = gtk.VBox(False, 0)
        vbox.show()

        eventbox = gtk.EventBox()
        eventbox.connect("selection_received", self._on_selection_received)
        eventbox.connect('enter-notify-event', self._on_mouse_enter)
        eventbox.connect('leave-notify-event', self._on_mouse_leave)

        gobject.timeout_add(500, self._on_timer, eventbox)
        eventbox.show()

        self.view = webkit.WebView()
        def title_changed(widget, frame, title):
            logging.debug('title_changed to %s, will open webbrowser ' % title)
            import webbrowser
            webbrowser.open('http://dict.youdao.com/search?le=eng&q=' + title )
        self.view.connect('title-changed', title_changed)
        self.view.show()

        self.window.add(vbox)
        vbox.pack_start(eventbox)
        eventbox.add(self.view)

    def _on_timer(self, widget):

        widget.selection_convert("PRIMARY", "STRING")

        if self.window.get_property('visible') and not self.mouse_in:
            x, y = self.window.get_position()
            px, py, mods = self.window.get_screen().get_root_window().get_pointer()
            if (px-x)*(px-x) + (py-y)*(py-y) > 400:
                logging.debug('distance big enough, hide window')
                self.window.hide()
            if(time.time() - self.popuptime > 3):
                logging.debug('time long enough, hide window')
                self.window.hide()

        return True

    def _on_selection_received(self, widget, selection_data, data):
        if str(selection_data.type) == "STRING":
            text = selection_data.get_text()
            if not text:
                return False
            text = text.decode('raw-unicode-escape')
            if(len(text) > 20):
                return False

            if (not text) or (text == self.last_selection):
                return False

            logging.info("======== Selected String : %s" % text)
            self.last_selection = text

            m = re.search(r'[a-zA-Z-]+', text.encode('utf8'))
            if not m:
                logging.info("Query nothing")
                return False

            word = m.group().lower()
            if self.ignore(word):
                logging.info('Ignore Word: ' + word)
                return False

            logging.info('QueryWord: ' + word)
            self.query_word(word)
            return True

        return False

    def query_word(self, word):
        cachewords = {}
        class Cache(object):
            def __init__(self, translation, phonetic, explains, web):
                self.translation = translation
                self.phonetic = phonetic
                self.explains = explains
                self.web = web

        if (word in cachewords.keys()):
            translation = cachewords[word].translation
            phonetic = cachewords[word].phonetic
            explains = cachewords[word].explains
            web = cachewords[word].web
        else:
            query_url = QUERY_URL + word
            js= json.loads(requests.get(query_url).text)
            if 'basic' not in js:
                logging.info('IgnoreWord: ' + word)
                return

            x, y, mods = self.window.get_screen().get_root_window().get_pointer()
            self.window.move(x+15, y+10)

            self.window.present()

            translation = '<br/>'.join(js['translation'])
            if 'phonetic' in js['basic']:
                phonetic = js['basic']['phonetic']
            else:
                phonetic = ''
            explains = '<br/>'.join(js['basic']['explains'])
            web = '<br/>'.join( ['<a href="javascript:void(0);">%s</a>: %s'%(i['key'], ' '.join(i['value'])) for i in js['web'][:3] ] )
            html = '''
    <style>
    .add_to_wordbook {
        background: url(https://dn-anything-about-doc.qbox.me/md0417215add.png) no-repeat;
        vertical-align: middle;
        overflow: hidden;
        display: inline-block;
        vertical-align: top;
        width: 24px;
        padding-top: 26px;
        height: 0;
        margin-left: .5em;
    }   
    </style>

            <h2>
            %(translation)s
            <span style="color: #0B6121; font-size: 12px">< %(phonetic)s > </span>
            <a href="javascript:void(0);" id="wordbook" class="add_to_wordbook" title="点击在浏览器中打开" onclick="document.title='%(word)s'"></a> <br/>
            </h2>
    
            <span style="color: #A0A0A0; font-size: 15px">[ %(word)s ] </span>
            <b>基本翻译:</b>
            <p> %(explains)s </p>
    
            <span style="color: #A0A0A0; font-size: 15px">[ %(word)s ] </span>
            <b>网络释意:</b>
            <p> %(web)s </p>

            ''' % locals()

            self.view.load_html_string(html, '')
            self.view.reload()
            self.popuptime = time.time()
            
            cachewords[word] = Cache(translation, phonetic, explains, web)

    def ignore(self, word):
        if len(word)<=3:
            return True
        return False

    def _on_mouse_enter(self, wid, event):
        logging.debug('_on_mouse_enter')
        self.mouse_in = True

    def _on_mouse_leave(self, *args):
        logging.debug('_on_mouse_leave')
        self.mouse_in = False
        self.window.hide()

def main():
    Dict()
    gtk.main()

if __name__ == "__main__":
    f=open(LOCK, 'w')
    try:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX|fcntl.LOCK_NB)
    except:
        print 'a process is already running!'
        exit(0)

    main()
