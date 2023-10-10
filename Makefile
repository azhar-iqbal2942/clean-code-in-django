# with command `.SILENT` only echo commands will be printed everything else will be omitted
.SILENT:

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	echo "Process Completed"

