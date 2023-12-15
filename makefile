VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

inputgraph = "dataset/musae_facebook_edges.csv"
anotherarg = "dataset/musae_facebook_target.csv"


$(VENV)/bin/activate: libraries.txt
	python3 -m venv $(VENV)
	$(PIP) install -r libraries.txt


run: $(VENV)/bin/activate
	$(PYTHON) src/main.py $(inputgraph) $(anotherarg)

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	
