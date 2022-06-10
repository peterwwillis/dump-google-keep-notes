
dump-keep-notes: venv
	./venv/bin/python dump-keep-notes.py
	./venv/bin/python dump-state-2-markdown.py

venv:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

