import networkx as nx
import os

def findBridges(graph):
    
    bridgesTxt = 'bridges.txt'

    bridges = list(nx.bridges(graph))
    
    with open(bridgesTxt, "w", encoding="utf-8") as file:
        for u, v in bridges:
            # Nome de cada nó integrante da ponte (u,v)
            pageU = graph.nodes[u]['page_name']
            pageV = graph.nodes[v]['page_name']
                
            file.write(f"Bridge: (ID_SOURCE: {u} NAME_SOURCE: {pageU}) - (ID_TARGET: {v} NAME_TARGET: {pageV})\n")
    
    if os.name == "nt": #Windows
        os.system("start notepad " + bridgesTxt)
    elif os.name == "posix": #Linux/Mac
        os.system("open -t " + bridgesTxt)
    else:
        print("Unsupported operating system.")
