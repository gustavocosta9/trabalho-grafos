import matplotlib.pyplot as plt


def plotTop(x, y):
    plt.bar(x, 
            y, 
            label='Page Name',
            color = 'green',
            width = 0.6
            )

    plt.title('The 10 most famous pages/peoples')
    plt.legend(['Popularity'], loc = 'upper right')
    plt.xlabel('Pages/Peoples')
    plt.ylabel('Degree of Centrality')

    plt.xticks(x,
            rotation = 7,
            fontname = 'Verdana',
            size=7
            )

    plt.show()