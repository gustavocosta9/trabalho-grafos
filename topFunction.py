import networkx as nx

def top10Function (graph):

    centralityDegree = nx.degree_centrality(graph)
    top10 = sorted(centralityDegree, key=centralityDegree.get, reverse=True)[:10]

    xTop = []
    yTop = []
    for top in top10:
        xTop.append(graph.nodes[top]['page_name'])
        yTop.append(graph.nodes[top]['centrality'])
    
    return xTop, yTop