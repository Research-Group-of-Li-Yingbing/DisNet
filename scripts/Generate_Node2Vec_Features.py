# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:00:46 2020

@author: Jinhang Jiang
"""

## Loard packages
import networkx as nx
from node2vec import Node2Vec
import pandas as pd
import numpy as np

## Read the file and trasform it to a networkx matrix
df= pd.read_csv('Data/network_table.csv', index_col=0)
graph=nx.from_numpy_matrix(df)


node2vec = Node2Vec(graph, dimensions=20, walk_length=5, num_walks=200, workers=4)
model = node2vec.fit(window=10, min_count=1)

embedding_matrix = node2vec.wv.vectors
#print(embedding_matrix.shape)
#print(embedding_matrix[0:10,0:10])
embedding_matrix = pd.DataFrame(embedding_matrix)
print(embedding_matrix.head())
embedding_matrix.to_csv('Undirected_network_embeddings.csv', index=False)
