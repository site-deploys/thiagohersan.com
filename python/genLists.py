#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, system
from os.path import join, isdir
from time import sleep
from re import sub

posts = {}
def getDate(i):
    return i['date']

if __name__ == "__main__":
    SOURCE_DIR = "source"
    POST_DIR = join(SOURCE_DIR, "_posts")
    POST_PERMALINK_DIR = "project"
    PAGE_TITLE = "Thiago Hersan"

    for filename in [f for f in listdir(POST_DIR) if f.endswith(".md")]:
        fullPath = join(POST_DIR, filename)
        chikChikCount = 0
        thisPost = {}
        with open(fullPath) as txt:
            for line in txt.read().splitlines():
                if(line == '---'):
                    chikChikCount += 1
                if(':' in line and chikChikCount < 2):
                    (key, val) = line.split(':', 1)
                    thisPost[key.strip()] = val.strip()
            if(not thisPost['category'] in posts):
                posts[thisPost['category']] = []
            posts[thisPost['category']].append(thisPost)
            txt.close()

    # order each category by descending date (most recent first)
    for (key, val) in posts.iteritems():
        val.sort(key=getDate, reverse=True)
        outDirName = key+'s'
        with open(join(SOURCE_DIR, join(outDirName,"index.md")), 'w') as out:
            out.write("---\n")
            out.write("layout: list\n")
            out.write("title: '"+PAGE_TITLE+"'\n")
            out.write("description: '"+outDirName.title()+"'\n")
            out.write("url: /"+POST_PERMALINK_DIR+"/\n")
            out.write("posts: \n")
            for post in val:
                tabString = "  - "
                for (pKey, pVal) in post.iteritems():
                    out.write(tabString+pKey+": "+pVal+"\n")
                    tabString = "    "
            out.write("---\n")
            out.close()
