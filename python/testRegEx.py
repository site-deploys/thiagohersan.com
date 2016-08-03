#! /usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub, search

def applyRegEx(line):
    if("img" in line):
        line = sub(r"< *img *?src *?= *?\"(([^ ]*?/)+(.+?))\".*?>", r"![](\3)", line)
        line = sub(r"-[0-9]+x[0-9]+\.(\w{3})", r".\1", line)
        line = sub(r"< *a *?href *?= *?\"(.*?)\" *?>(.*?)< *?/ *?a *?>", r"\2", line)
    else:
        line = sub(r"< *a *?href *?= *?\"(.*?)\" *?>(.*?)< *?/ *?a *?>", r"[\2](\1)", line)
    print line

lines = []
lines.append(' for <em><a href="http://en.wikipedia.org/wiki/E_pluribus_unum">e pluribus unum</a></em>, or, "from many, to one".  Through the use of <a href="http://code.google.com/p/andar/">augmented reality technology</a>, users can use their own phones to view these virtual works distributed throughout a physical environment.')

lines.append('<img src="http://www.thiagohersan.com/wp-content/uploads/2013/10/FaC00_idea-1024x548.jpg" alt="FaC00_idea" width="625" height="334" />')

lines.append('<a href="http://www.thiagohersan.com/wp-content/uploads/2013/05/iGotPoked.png"><img src="http://www.thiagohersan.com/wp-content/uploads/2013/05/iGotPoked.png" alt="iGotPoked" width="931" height="313"/></a>')

lines.append('<a href=""><img src="http://www.thiagohersan.com/wp-content/uploads/2013/12/like.png" alt="like" height="22" /> + <img src="http://www.thiagohersan.com/wp-content/uploads/2013/12/like.png" alt="like" height="22" /> + <img src="http://www.thiagohersan.com/wp-content/uploads/2013/12/like.png" alt="like" height="22" /> + <img src="http://www.thiagohersan.com/wp-content/uploads/2013/12/like.png" alt="like" height="22" /> + <img src="http://www.thiagohersan.com/wp-content/uploads/2013/12/like.png" alt="like" height="22" /> = <img src="http://www.thiagohersan.com/wp-content/uploads/2013/12/heart.png" alt="heart" height="22" /></a>')

for line in lines:
    applyRegEx(line)
    print ""
