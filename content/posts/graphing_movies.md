+++
title = "Graphing the Movies"
date = 2019-11-22T08:43:29+05:30
draft = false
+++
## First Post
With the end semester exams coming up, I figured it’s the perfect time to start my blog (yeah, great timing, right?). As I was studying Graphs for exam prep, I wanted to implement something cool using them. After searching for a while, I stumbled upon [this dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/T4HBA3). It’s from Moviegalaxies, a site that provides network graph data from around 773 films. Pretty neat, huh?

---

## Data Processing 
So, I took the raw data and processed it into a CSV file, showing how two characters appear together in a scene, which is represented as edges of a graph. For example, if you look at the Godfather, there are two scenes where Anthony and Michael both appear together. Here's how it looks in the CSV format:

{{< highlight csv >}}
Source, Target, Weight
ANTHONY, MICHAEL, 2
{{< /highlight >}}

---

## Plotting the graph
Now that we have the weighted edges in our CSV file, we can plot them like any other weighted graph. I’ve used [gephi](https://gephi.org/) for visualizing graphs before, but this time I wanted to stick with Python, so I went with [networkx](https://networkx.github.io/). It’s super well-documented and easy to use, as long as your data is in the right format. If you want the code I wrote, you can check it out [here](https://github.com/us241098/Graphs-and-Pop-Culture).

<br>
{{< figure src="/Departed.png" caption="Graph for Godfather 2" alt="Graph for Godfather 2" >}}

---

## Community Detection
Community detection is basically about finding groups of nodes that are closely connected in the graph. These groups are called communities. In real life, brands can use this to understand different opinions about their products, or to find influencers. For our graphs, communities show groups of characters who appear together the most on screen.

I used the `community` module, which applies the Louvain method for community detection.

<br>
{{< figure src="/Departed_communities.png" caption="Communities plotted for Godfather 2" alt="Communities plotted for Godfather 2" >}}

---

## Pulp Fiction
Here's how the graph looks for *Pulp Fiction*:

{{< figure src="/Pulp_Fiction.png" caption="Pulp Fiction characters co-appearance" alt="Pulp Fiction characters co-appearance" >}}

<br><br>

And here are the communities for *Pulp Fiction*:

{{< figure src="/Pulp_Fi_communities.png" caption="Communities in Pulp Fiction" alt="Communities in Pulp Fiction" >}}

---

## The Departed
Now onto *The Departed*. Here’s the graph showing the characters who appear together:

{{< figure src="/Departed_2.png" caption="The Departed characters co-appearance" alt="The Departed characters co-appearance" >}}

<br><br>

And finally, the communities in *The Departed*:

{{< figure src="/Departed_communities_2.png" caption="Communities in The Departed" alt="Communities in The Departed" >}}

---
