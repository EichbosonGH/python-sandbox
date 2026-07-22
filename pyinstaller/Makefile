
# bundlen mit temporärem pyinstaller
make-zufallszahl-onetime:
	uvx --with numpy pyinstaller --onefile zufallszahl.py

# pyinstaller installieren und numpy bereitstellen
install-pyinstaller:
	uv tool install pyinstaller --with numpy

# bundlen der Python-Daten
make-zufallszahl:
	pyinstaller --onefile zufallszahl.py

# pyinstaller alle paketen aus der aktuellen .venv mitgeben (nicht getestet)
install-pyinstaller-all:
	uv sync
	uv pip freeze > requirements.txt
	uv tool install pyinstaller --with-requirements requirements.txt
	rm requirements.txt