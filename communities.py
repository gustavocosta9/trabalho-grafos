# Clusterização das comunidades pertencentes ao Grafo pelo algoritmo de Louvain
import networkx as nx
import matplotlib.pyplot as plt
import community

def graphCluster (graph):

    partition = community.best_partition(graph) # Louvain é mais otimizado que Girvan-Newman.
    communities = {}
    for node, communityId in partition.items():
        if communityId not in communities:
            communities[communityId] = set()
        communities[communityId].add(node)
    return list(communities.values())

##########################################################################

def plotCommunities (graph, communities):
    
    rowsPlot = 10
    columnsPlot = (len(communities) + rowsPlot - 1) // rowsPlot

    plt.figure(figsize=(20, 10))  # Ajuste o tamanho da figura conforme necessário

    for i, community in enumerate(communities, start=1):
        
        plt.subplot(rowsPlot, columnsPlot, i)
        
        graphCommunity = graph.subgraph(community)
        position = nx.fruchterman_reingold_layout(graphCommunity)

        
        nx.draw(graphCommunity, position, with_labels=True, node_size=300, node_color='red')
        plt.title(f'Community {i}')

    plt.savefig('graph.png')

##########################################################################