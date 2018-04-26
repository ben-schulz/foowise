watch:
	python3 ./test_watcher.py --project . --tests test --pattern Test*.py
test:
	python3 -m unittest discover -s ./test -p "Test_*.py"

.PHONY: test
