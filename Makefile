watch:
	. env/bin/activate && python3 ./test/test_watcher.py --project channels matrices math test --tests test --pattern Test*.py
test:
	. env/bin/activate && python3 -m unittest discover -s ./test -p "Test_*.py"

.PHONY: test
