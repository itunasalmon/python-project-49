install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --break-system-packages dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall --break-system-packages dist/*.whl

lint:
	poetry run flake8 brain_games