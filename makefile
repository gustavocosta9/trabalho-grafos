.PHONY: all install run runmanual runwithinterface

install: 
	python -m venv GustavoCostaGrafos
	GustavoCostaGrafos/Scripts/pip install --upgrade -r libraries.txt

run: GustavoCostaGrafos
	echo "musae_facebook_edges.csv\musae_facebook_target.csv"
ifeq ($(OS),Windows_NT)
	if exist graph.png start "" graph.png
	if exist bridges.txt start "" bridges.txt
else
	xdg-open graph.png
	xdg-open bridges.txt
endif
	@echo "Execucao do alvo run concluida"

plot_communities: GustavoCostaGrafos
		GustavoCostaGrafos/Scripts/python communities.py
ifeq ($(OS),Windows_NT)
	if exist graph.png start "" graph.png
else
	xdg-open graph.png
endif

show_bridges: GustavoCostaGrafos
	GustavoCostaGrafos/Scripts/python bridges.py
ifeq ($(OS),Windows_NT)
	if exist bridges.txt start "" bridges.txt
else
	xdg-open bridges.txt
endif

main: GustavoCostaGrafos
	GustavoCostaGrafos/Scripts/python main.py

all: run plot_communities show_bridges main

GustavoCostaGrafos:
	python -m venv GustavoCostaGrafos

clean:
	rm -rf GustavoCostaGrafos/
	rm -f graph.png
	rm -f bridges.txt
