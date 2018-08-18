watch:
	. env/bin/activate && python3 foowise/test/test_watcher.py --project foowise/channels foowise/math foowise/heuristic foowise/test --tests foowise/test --pattern Test*.py

test:
	. env/bin/activate && python3 -m unittest discover -s foowise/test -p "Test_*.py"

.PHONY: test watch
