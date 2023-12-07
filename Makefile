install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# cd server && python -m pytest -vv --cov=server test_*.py
	python -m pytest -vv --cov=server test_*.py
	# python -m pytest -vv --cov=main --cov=mylib test_*.py
	

format:	
	black *.py 

lint:
	ruff check server/*.py server/mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint
		
all: install lint test format deploy
