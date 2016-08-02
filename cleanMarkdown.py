#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, makedirs
from os.path import join, exists
from time import sleep
from re import sub, search
from slugify import slugify

posts = []

if __name__ == "__main__":
    SOURCE_DIR = "source"
    PROJ_DIR = join(SOURCE_DIR, "_projects")
    OUT_DIR = join(SOURCE_DIR, "_posts")

    for filename in [f for f in listdir(PROJ_DIR) if f.endswith(".md")]:
        fullPath = join(PROJ_DIR, filename)
        chikChikCount = 0
        thisPost = {}
        with open(fullPath) as txt:
            content = ""
            for line in txt.read().splitlines():
                if(line == '---'):
                    chikChikCount += 1
                elif(':' in line and chikChikCount < 2):
                    (key, val) = line.split(':', 1)
                    thisPost[key.strip()] = val.strip()
                elif chikChikCount >= 2:
                    line = sub(r"</?em>", "*", line)
                    line = sub(r"</?strong>", "**", line)
                    line = sub(r"</?strong>", "**", line)
                    line = sub(r"</?p>", "", line)
                    if("img" in line and "href" in line):
                        imgFile = search(r".*/([\S]+.(jpg|png|jpeg|bmp|gif)).*",line).group(1)
                        line = "![](%s)"%imgFile
                    line = sub(r"<a *?href *?= *?\"(.*?)\" *?>(.*?)< *?/ *?a *?>", r"[\2](\1)", line)
                    content += "%s\n"%line
            thisPost['content'] = content
            posts.append(thisPost)
            txt.close()

    # write out
    for p in posts:
        cleanTitle = sub(r" *\([0-9 \-]+\)","",p['title']).strip()
        outputFileName = slugify(cleanTitle)
        coverFileName = slugify(cleanTitle, max_length=16, word_boundary=True)
        category = p['category'] if 'category' in p else p['layout']
        description = p['description'] if 'description'in p else ''
        with open(join(OUT_DIR,outputFileName+".md"), 'w') as out:
            out.write("---\n")
            out.write("layout: %s\n"%p['layout'])
            out.write("category: %s\n"%category)
            out.write("title: %s\n"%cleanTitle)
            out.write("description: %s\n"%description)
            out.write("url: %s/\n"%outputFileName)
            out.write("date: %s\n"%sub(r"\+[0-9:]+","",p['date']))
            out.write("cover: /images/covers/%s-300x90.jpg\n"%coverFileName)
            out.write("---\n")
            out.write(p['content'])
            out.close()
        if not exists(join(OUT_DIR, outputFileName)):
            makedirs(join(OUT_DIR, outputFileName))
