+++
title = 'GREENER'
date = 2024-09-05T03:38:32+05:30
draft = false
+++

# greener: graph neural networks for news media profiling

in the summer of 2020 i got an opportunity to work on GREENER with dr. preslav nakov and tanbih team. this project aimed at detecting bias and factuality of news media but beyond mere textual signals. in this blog post, we'll dive into the technical details behind greener, including its methods and concepts.

## problem definition

greener's goal is to profile news media outlets based on two characteristics:
- **factuality**: this can be low, mixed, or high, depending on how truthful a media outlet's reporting is.
- **bias**: this can be categorized as left, center, or right, indicating the political leaning of a media outlet.

rather than relying only on the content of articles, greener also uses audience overlap data. this is based on **homophily**, a principle that suggests similar entities (in this case, media outlets) are often connected. if two outlets share a similar audience, they are likely to share attributes like factuality or bias.

---

## graph construction: audience overlap graph

the first step in greener is to create an **audience overlap graph**. think of this graph as a network where each point (node) represents a news outlet, and the connections (edges) between them represent their audience overlap. the strength of these connections is determined by how much their audiences overlap.

### audience overlap score

the **audience overlap score** measures how similar the audiences of two outlets are. it is calculated as follows:

- the overlap score between two outlets (let's call them a and b) is calculated by dividing the number of shared audience members by the total audience size of both outlets combined, minus the shared audience. 
- this score ranges from 0 to 1, where 1 means that the audiences of both outlets are identical, and 0 means there is no overlap.

the formula is:

```
overlap_score(a, b) = shared_audience(a, b) / (total_audience(a) + total_audience(b) - shared_audience(a, b))
```

---

## graph neural networks (gnns) for representation learning

after building the graph, greener uses **graph neural networks (gnns)** to create representations (embeddings) for each media outlet. these embeddings capture the structure of the audience overlap graph and the characteristics of each media outlet.

### node2vec

one of the methods greener uses to create these representations is **node2vec**. imagine taking a random walk around the graph—much like moving from one point to another in a network based on how they are connected. node2vec uses these walks to understand which nodes are similar based on their neighborhoods. it then creates numerical representations for each node that best describe these similarities.

the goal of node2vec is to increase the likelihood that similar nodes will have similar representations. it focuses mainly on the structure of the graph, capturing audience similarities between media outlets.


### graph convolutional networks (gcn)

another method used in greener is **graph convolutional networks (gcn)**. gcns are specifically designed to learn from both the graph's structure and the characteristics of individual nodes.

- gcns update each node's representation by combining information from its neighbors. imagine a news outlet learning about its characteristics by "listening" to the outlets it is connected to.
- this process is repeated in layers, with each layer refining the representation based on the latest information from neighboring nodes.
- the final result is a set of numerical representations that take into account both the audience overlap and other available characteristics.

the propagation rule for gcn is:
```
h_next = activation((d^-0.5 * (a + i) * d^-0.5) * h_current * w)
```

```
where:
- `h_next` is the representation of nodes at the next layer.
- `h_current` is the representation of nodes at the current layer.
- `a` is the adjacency matrix (connections between nodes).
- `i` is the identity matrix (self-connections).
- `d` is the degree matrix, which indicates the number of connections each node has.
- `w` is the weight matrix that the model learns.
- `activation` is a non-linear function like relu.
```

### graphsage

**graphsage** (graph sample and aggregate) is another method that greener uses. it works similarly to gcn but is more efficient for large graphs.

- instead of using all neighbors, graphsage selects a fixed number of neighbors for each node to learn from. this makes it scalable to very large datasets.
- it then combines the information from these sampled neighbors using simple functions like averaging or finding the maximum value.

the aggregation rule is:
```
h_next = activation(weight * aggregate({h_current_of_neighbors}))
```

```
where:
- `h_next` is the updated representation of a node.
- `weight` is the weight matrix that the model learns.
- `aggregate` is a function (like averaging) that combines the information from neighbors.
- `h_current_of_neighbors` represents the features of the current node's neighbors.
```
---

## fusion with textual representations

while the audience overlap graph gives valuable insights, greener also uses traditional **textual features** from sources like news articles and social media. these features are extracted using advanced language models like **bert**.

the final prediction combines insights from both the graph and the textual features. greener trains separate models for each set of features and then averages the predictions to make a final decision. this ensures that the strengths of both types of data are fully utilized.

---

## experimental results

in tests using standard datasets, greener showed significant improvements in predicting both factuality and bias compared to earlier methods. here are some highlights:

- **factuality prediction**: greener improved by up to 27 percentage points in accuracy when combining audience overlap and textual data.
- **bias prediction**: using both types of data together led to an increase of up to 9 percentage points, showing that audience data and textual features complement each other well.

---
