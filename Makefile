watch:
	python3 ./test/test_watcher.py --project channels --tests test --pattern Test*.py
test:
	python3 -m unittest discover -s ./test -p "Test_*.py"

.PHONY: test
