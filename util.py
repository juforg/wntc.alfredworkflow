# -*- coding: utf-8
import os


def notice(msg, title="notice"): 
    ''' notoce message in notification center'''
    os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))

