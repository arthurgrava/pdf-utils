PYTHON := .env/bin/python
PIP := .env/bin/pip
JUPYTER := .env/bin/jupyter

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "dist" -type d | xargs rm -rf
	@find . -name "htmlcov" | xargs rm -rf
	@find . -name ".coverage" | xargs rm -rf
	@find . -name ".pytest_cache" | xargs rm -rf
	@find . -name ".cache" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "*.egg-info" | xargs rm -rf
	@find . -name "build" | xargs rm -rf

install: clean
	virtualenv .env -p python3
	${PIP} install -r requirements.txt

merge: clean
	${PYTHON} scripts/merger.py --output-name ${OUTPUT} --merge-these ${INFILES}

select: clean
	${PYTHON} scripts/selector.py \
		--output-name ${OUTPUT} \
		--infile ${INFILE} \
		--pages ${PAGES}
