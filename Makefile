.PHONY: init 
init:
	uv sync
	uvx nbstripout --install

.PHONY: info
info:
	uv version