PY_FILE := circle_locations.py
TEX_FILE := figure.tex
PDF_FILE := figure.pdf
PNG_FILE := figure.png

all: $(PNG_FILE)

$(PNG_FILE): $(PDF_FILE)
	magick -density 800 $(PDF_FILE) -crop 5100x5100+850+0 +repage $(PNG_FILE)

$(PDF_FILE): $(TEX_FILE)
	xelatex $(TEX_FILE)

$(TEX_FILE): $(PY_FILE)
	uv run $(PY_FILE) > $(TEX_FILE)

clean:
	rm -f $(PNG_FILE)

.PHONY: all clean
