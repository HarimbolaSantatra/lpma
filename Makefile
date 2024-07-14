BINDIR=~/.local/bin
FILES=lpma.py lpma
VENVDIR=~/.python-venv/
PYTHON=/usr/bin/python

all:
	cp $(FILES) $(BINDIR)/

install:
	mkdir -p $(VENVDIR)
	$(PYTHON) -m venv $(VENVDIR)/lpma
	$(VENVDIR)/lpma/bin/python -m pip install -r requirements.txt

clean:
	rm $(BINDIR)/lpma $(BINDIR)/lpma.py
