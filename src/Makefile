TARGETS = \
	kenya_matunda.pdf \

PYTHON = PYTHONPATH=../../svg-narrative/src/ $(shell which python3)
INKSCAPE = $(shell which inkscape)


all: ${TARGETS}

clean:
	touch  ${TARGETS}
	rm     ${TARGETS}

mrproper: clean
	touch d~
	rm    *~



kenya_matunda.svg: ../var/coffees/kenya_matunda.json produce_stickers.py
	${PYTHON} produce_stickers.py ../var/coffees/kenya_matunda.json ../var/templates/default.svg ../var/templates/World_map_blank_with_blue_sea.svg ../var/templates/roast.svg kenya_matunda.svg

kenya_matunda.pdf: kenya_matunda.svg
	${INKSCAPE} -z -D -A kenya_matunda.pdf kenya_matunda.svg

