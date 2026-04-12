.PHONY: install test lint secure clean update

# Target commands for DevOps lifecycle

install:
	python3 -m pip install --upgrade pip setuptools wheel
	pip install -r requirements.txt
	pre-commit install || echo "Pre-commit cannot be installed, ignoring..."

lint:
	flake8 src/
	shellcheck scripts/setup.sh || echo "Shellcheck not found. Ignored."

test:
	pytest tests/ -v

secure:
	bandit -r src/
	pip-audit

clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf results/*.txt results/PDF/*.pdf

update:
	python3 -m pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	pip-audit --fix
