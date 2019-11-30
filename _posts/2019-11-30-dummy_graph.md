---
title: "Network Analysis and Pop Culture"
layout: post
date: 2019-11-30 12:16
tag:
- network_analysis
- coding
star: true
category: blog
author: utsav 
description: "Graph Theory and Movies"
---

## First Post
With the End Semester exams approaching I decided that this is the perfect time to start my blog. As I was studying Graphs for my exam preparation, I thought to implement something cool using them. After searching for some time I found [this](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/T4HBA3). This repository contains network graphs and network metadata from Moviegalaxies, a website providing network graph data from about 773 films. 

{% highlight html %}
This note **demonstrates** some of what [Markdown][some/link] is *capable of doing*.
{% endhighlight %}

---

## Data Processing 

The data above was processed to convert the raw data to a csv file containing co-appearance of two characters in a scene represented as edges of graph.

{% highlight raw %}
Source, Target, Weight
ANTHONY, MICHAEL, 2
{% endhighlight %}

The above format signifies that there are 2 scenes where Anthony and Michael have both appeared together in the movie Godfather (as annotated in the dataset we are using).

---

