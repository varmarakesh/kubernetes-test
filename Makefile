# system python interpreter. used only to create virtual environment
PY = python3
VENV = venv
BIN=$(VENV)/bin

$(VENV): requirements.txt
	virtualenv $(VENV) --python $(PY)
	$(BIN)/pip install --upgrade -r requirements.txt
	$(BIN)/pip install -e .
	touch $(VENV)

install: $(VENV) ## Creates virtualenv and installs libs
	@echo "Installed project with requirements"

.PHONY: test
test: $(VENV) ## Runs unit tests
	@$(BIN)/pytest  tests/unit/*.py

clean:  ## Remove virtualenv, python cached files
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

.PHONY: help
help: ## Help Menu
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
