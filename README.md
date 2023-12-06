# Mini Trabalho da disciplina de Grafos ⚽

*Nome: Gustavo Costa*

*Turma: 10A*

*Curso: Ciências da Computação*

*Universidade Federal de Lavras*

O trabalho de Grafos consistiu em utilizar um dataset de um Grafo e realizar:
  - A própria criação do grafo nos códigos;
  - Realizar objetivos vistos dentro de sala de aula como: detecção de comunidades, pontes, centralidade, transitividade, densidade, etc.

<img src="https://i.ibb.co/wWxwJ9W/graph-13.png">

****

### Desafios enfrentados ⚠️
Como primeiro código envolvendo a manipulação de estruturas em grafos para a captura de insights valiosos, a própria *abstração* foi o maior empecilho do projeto porque demanda o conhecimento de alguns conceitos basilares da estrutura em grafos, saber oque a centralidade pode significar no contexto do problema, oque a densidade do grafo pode nos informar, etc.


### Perguntas a serem respondidas 📃
Como o tempo foi apertado pelo encurtamento do período letivo devido aos impactos do COVID-19, o trabalho teve como foco realizar operações no grafo e retirar alguns insights que possam nos trazer informações contextualizadas para a rede social Facebook. São eles:
  
  - Dado o dataset, quais são as 10 páginas do facebook mais influentes? Como é possível descobrir essa informação de um grafo?
  - Quantas comunidades existem no grafo do dataset? Ou seja, quantas comunidades existem no Facebook?
  - Quais são as pontes desse grafo? Oque essas pontes significam na contextualização do problema?

****

### Entendendo os arquivos 📑
O programa foi subdividido em diferentes arquivos .py para facilitar a manutenção e legibilidade do código.
  - *main.py* : arquivo responsável pela função menu que retorna os resultados condizentes com a escolha do usuário.

    <img src="https://i.ibb.co/q740Cyx/Captura-de-tela-2023-12-05-205219.png">
  
  - *analysisDescriptive.py* : arquivo responsável pela leitura dos datasets em formato .csv e pela criação do grafo e suas informações: grau de cada nó, densidade do grafo, transitividade do grafo, inserção das características de cada nó, etc.

    <img src="https://i.ibb.co/N9fJ6VY/Captura-de-tela-2023-12-05-205243.png">
  
  - *topFunction.py* : arquivo que consiste em achar as 10 páginas mais influentes pelos nós com as 10 maiores centralidades do grafo. xTop é o para ser o eixo X do gráfico e yTop para ser o eixo Y do gráfico.

    <img src="https://i.ibb.co/8XNkTyv/Captura-de-tela-2023-12-05-205318.png">
  
  - *topPlot.py* : arquivo que só tem como propósito receber os eixos do TopFunction.py (xTop e yTop) e plotar um gráfico das páginas mais influentes.

    <img src="https://i.ibb.co/S0gv7F2/Captura-de-tela-2023-12-05-205326.png">
  
  - *communities.py* : arquivo que recebe o grafo, detecta as comunidades utilizando o algoritmo de Louvain e também possui a função de plotagem das comunidades em um .png (Obs: quanto maior o grafo e sua densidade, mais demorado é).

    <img src="https://i.ibb.co/Yp7XxHV/Captura-de-tela-2023-12-05-205304.png">

    .png gerado das comunidades detectadas do grafo
    <img src="https://i.ibb.co/M532cnR/Captura-de-tela-2023-12-05-211920.png">
    
  - *bridges.py* : arquivo que detecta as pontes do grafo, arestas (u, v) que podem aumentar as comunidades do Facebook

    <img src="https://i.ibb.co/54CbFnb/Captura-de-tela-2023-12-05-205251.png">

    resultado gerado pela função de encontrar as pontes: escrita das pontes e o nome dos respectivos nós (páginas do facebook) que possuem essa aresta (u,v)
    <img src="https://i.ibb.co/5hRYsZp/Captura-de-tela-2023-12-05-211500.png">
    
  - *makefile* : utilização de um makefile com o propósito de criar um ambiente virtual e poder realizar a execução do programa sem grandes problemas, baixando as bibliotecas necessárias e realizando diferentes operações solicitadas pelo professor. Obs: fiz tanto para funcionamento em Linux e Mac quanto em Windows por isso a utilização de condicionais para detectar qual sistema operacional está sendo utilizado.

    <img src="https://i.ibb.co/CQcF89r/Captura-de-tela-2023-12-05-210816.png">
  
  - *dataset Stanford SNAP* : <a href="https://snap.stanford.edu/data/facebook-large-page-page-network.html" target=_blank>acesse aqui</a>

    .csv das arestas (musae-facebook-edges), só um pedaço, visto que há mais de 170 mil arestas no grafo.
    <img src="https://i.ibb.co/QY64S98/Captura-de-tela-2023-12-05-211004.png">

    .csv das caracteristicas de cada página (musae-facebook-target), só um pedaço, visto que há mais de 22 mil nós no grafo.
    <img src="https://i.ibb.co/6FN50PT/Captura-de-tela-2023-12-05-211140.png">

****
### Considerações Finais 💭
Apesar de ser um mini-trabalho pelo tempo, foi uma proposta interessante por ser uma oportunidade de aplicar alguns dos conhecimentos teóricos de grafos vistos ao longo de toda a disciplina em código. Além disso, é interessante dizer que em diversos momentos, pelo fato do grafo haver muitos nós e arestas, nem sempre determinados algoritmos tiveram uma boa eficiência, trazendo também as questões de pensar nas complexidades dos algoritmos que foram abordados durante o período inteiro pelo professor e como implementar soluções alternativas e eficientes que resultem em uma execução em tempo ótimo.

É extremamente importante saber oque um grafo pode representar e como sua utilização se dá em diversos segmentos atualmente: PageRank do Google, Estruturas de Dados, uso de grafos para mapeamento de melhores rotas e logística, o uso dos grafos para reconhecimentos faciais na produção de máscaras 3D a partir de imagens frontais 2D. Enfim, são tantas aplicações que é difícil expor em um simples texto.
****

### Autoria do dataset

B. Rozemberczki, C. Allen and R. Sarkar. Multi-scale Attributed Node Embedding. 2019.

    `@misc{rozemberczki2019multiscale,
            
            title={Multi-scale Attributed Node Embedding},
            
            author={Benedek Rozemberczki and Carl Allen and Rik Sarkar},
            
            year={2019},
            
            eprint={1909.13021},
            
            archivePrefix={arXiv},
            
            primaryClass={cs.LG}
        }`
