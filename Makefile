.PHONY: test

test:
	PYTHONPATH=. pytest -s

test_ci:
	PYTHONPATH=. pytest -vv

test_update_snapshots:
	PYTHONPATH=. pytest --snapshot-update --allow-snapshot-deletion
