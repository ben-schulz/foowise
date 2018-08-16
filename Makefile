watch:
	. env/bin/activate && python3 ./test/test_watcher.py --project ./foowise/channels ./foowise/math ./foowise/heuristic ./test --tests ./test --pattern Test*.py
test:
	. env/bin/activate && python3 -m unittest discover -s ./test -p "Test_*.py"

.PHONY: test
