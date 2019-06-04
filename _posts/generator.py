#!/bin/python

import datetime
x = datetime.date.today()
time = datetime.datetime.now()
time = str(time)
time = time[0:16]
file_title = input("file-title: ")
title = input("Input Title: ")
filename = str(x) + "-" + file_title + '.md'
description = input("Input Description: ")
text_to_write = '''---
title: "{0}"
layout: post
date: {1}
image: /assets/images/profile.png
headerImage: false
tag:
star: true
category: blog
author: awalvie 
description: "{2}"
---
'''.format(title, time, description) 

print(text_to_write)

with open(filename, 'w') as file:
    file.write(text_to_write)
