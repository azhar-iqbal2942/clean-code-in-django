# with command `.SILENT` only echo commands will be printed everything else will be omitted
# .SILENT:
# .PHONY: migrate
clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	echo "Process Completed"

# TODO: Need to fix sometime it show weird behaviour
migrate:
	poetry shell && \
	cd src && \
	python manage.py migrate
	echo "Task Completed"

