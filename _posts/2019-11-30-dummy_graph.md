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
With the End Semester exams approaching I decided that this is the perfect time to start my blog. As I was studying Graphs for my exam preparation, I thought to implement something cool using them. After searching for a while I found [this](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/T4HBA3). This repository contains network graphs and network metadata from Moviegalaxies, a website providing network graph data from about 773 films. 


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
Now as we have our weighted edges in our CSV file we can plot them just like any other weighted graph. For visualisation, I have used [gephi](https://gephi.org/) previously, but I wanted to use only Python for this project so decided to use [networkx](https://networkx.github.io/), It's very well documented and so easy to use given your data is in correct format. You can find code for the project [here](https://github.com/us241098/Graphs-and-Pop-Culture) .
<br>
<div style="text-align:center"><img src="https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Departed.png" /></div>
<figcaption class="caption">After plotting I got a visualisation like this for Godfather 2</figcaption>


---

## Community Detection
Community detection aims to identify highly connected groups of individuals or objects inside these networks, these groups are called communities. The motives behind community detection are diverse: it can help a brand understand the different groups of opinion toward its products, target certain groups of people or identify influencers. In our graphs communities depict the group of people that have interacted the most on screen.
<br>
`community` module uses Louvain method for community detection.
<div style="text-align:center;height:600px;width:1000px;"><img src="https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Departed_communities.png" /></div>
<figcaption class="caption">Communities plotted. Observe how well it has separated the two different timelines in the movie. </figcaption>

---

## Pulp fiction
<div style="text-align:center"><img src="https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Pulp_Fiction.png" /></div>
<figcaption class="caption">Pulp fiction charcaters co-appearance</figcaption>
<br>
<br>
<div style="text-align:center"><img src="https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Pulp_Fi_communities.png" /></div>
<figcaption class="caption">Communities in Pulp Fiction</figcaption>

---

## The Departed
<div style="text-align:center"><img src="https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Departed_2.png" /></div>
<figcaption class="caption">The Departed charcaters co-appearance</figcaption>
<br>
<br>
<div style="text-align:center"><img src="https://raw.githubusercontent.com/us241098/Graphs-and-Pop-Culture/master/img/Departed_communities_2.png" /></div>
<figcaption class="caption">Communities in The Departed</figcaption>

---


