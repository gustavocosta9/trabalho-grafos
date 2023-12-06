import pandas as pd
import networkx as nx

def infoBasicGraph():
    
    pathFile = 'C:\\Users\\Pichau\\Desktop\\UFLA\\3° Período\\Grafos\\Trabalho-Grafos\\dataset\\musae_facebook_edges.csv'
    pathFile2 = 'C:\\Users\\Pichau\\Desktop\\UFLA\\3° Período\Grafos\\Trabalho-Grafos\dataset\\musae_facebook_target.csv'

    # 1 - Leitura das arestas do Grafo.
    
    edgesDf = pd.read_csv(pathFile)
    totalEdges = len(edgesDf.id_1)

    # 2 - Leitura das características de cada nó do Grafo.
    
    featuresDf = pd.read_csv(pathFile2)

    # 3 - Criação do grafo utilizando a biblioteca networkx.

    graph = nx.from_pandas_edgelist(edgesDf, 'id_1', 'id_2', create_using=nx.Graph())

    # 4 - Análise Descritiva do grafo: Grau, Centralidade e Transitividade.

    degreeDict = dict(graph.degree(graph.nodes())) #Lista de nós do grafo passada para a função que calcula o grau de cada nó, após isso cria-se dict
    nx.set_node_attributes(graph, degreeDict, 'degree') #cria novo atributo pra cada nó que é o Grau.


    featuresDict = featuresDf.set_index('id').to_dict(orient='index') #Setando um novo dicionario tendo o 'id' como index para as info. de cada nó
    nx.set_node_attributes(graph, featuresDict) #Adicionando esse dicionário como características de cada nó no grafo.


    density = nx.density(graph)           # Densidade do grafo
    transitivity = nx.transitivity(graph) # Transitividade do grafo


    centralityDegree = nx.degree_centrality(graph)        # dicionário de centralidade de cada nó.
    centralityDegreeList = list(centralityDegree.items()) # conversão pra lista de tuplas (idNó, centralidadeNó)
    for nodeId, centrality in centralityDegreeList:
        graph.nodes[nodeId]['centrality'] = centrality

    return graph
