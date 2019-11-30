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


---

## Data Processing 
The data above was processed to convert the raw data to a csv file containing co-appearance of two characters in a scene represented as edges of graph.
The format below shows that there are 2 scenes where Anthony and Michael have both appeared together in the movie Godfather (as annotated in the dataset we are using).

{% highlight raw %}
Source, Target, Weight
ANTHONY, MICHAEL, 2
{% endhighlight %}


---

## Plotting the graph
Now as we have our weighted edges in our CSV file we can plot them just like any other weighted graph. For visualisation, I have used [gephi](https://gephi.org/) previously, but I wanted to use only Python for this project so decided to use [networkx](https://networkx.github.io/), It's very well documented and so easy to use given your data is in correct format. You can find code for the project [here](https://github.com/us241098/Graphs-and-Pop-Culture) 
<br>
<br>
![Markdowm Image][https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Departed.png]
<figcaption class="caption">After plotting I got a visualisation like this for Godfather 2</figcaption>


---



