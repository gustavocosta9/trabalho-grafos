# Gustavo Costa - Universidade Federal de Lavras, Minas Gerais
# -------------------TRABALHO DE GRAFOS-----------------------

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import sys

from topPlot import plotTop
from analysisDescriptive import infoBasicGraph
from topFunction import top10Function
from communities import graphCluster
from communities import plotCommunities
from bridges import findBridges

def cleanTerminal(): # Função estética.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# --------------- MENU -------------------
def main():
    while True:
        print("WELCOME TO THE FACEBOOK PAGES CONSULTATION.")
        print("(1) To plot the bar chart of the top 10 most influential Facebook pages.")
        print("(2) To plot the image of Facebook communities.")
        print("(3) To find out which bridges exist in the graph.")
        print("(4) To finish the program.")
        option = int(input("Enter the numerical value corresponding to the desired option:"))
        cleanTerminal()

        match option:
            
            case 1:
                xTop, yTop = top10Function(graph)
                plotTop(xTop, yTop)
            
            case 2:
                communities = graphCluster(graph)
                plotCommunities(graph, communities)
                if sys.platform.startswith('linux'):
                    os.system('xdg-open graph.png')
                elif sys.platform.startswith('win'):
                    os.system('start graph.png')
            case 3:
                findBridges(graph)
            
            case 4:
                print("Program Finished.")
                break
            
            case _:
                print("Invalid Option!")



# Primeiro passo: Criação do Grafo com todas suas características: Grau, Centralidade, NomePágina, id, idFacebook, arestas, tipoPágina.

graph = infoBasicGraph()

# Segundo passo: menu de operações.

main()


#attributeNames = list(graph.nodes[0].keys()) # Lista dos nomes dos atributos de um nó.
#print(attributeNames)

