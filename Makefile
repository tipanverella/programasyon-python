CC=poetry
PYTHONFILES=energie_mecanique

lint: $(PYTHONFILES)
	$(CC) run black .
	$(CC) run pylint $(PYTHONFILES)

test: lint
	$(CC) run pytest -vv
