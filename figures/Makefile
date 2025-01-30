PDF_FILE := Drug_Manuscript.pdf
PNG_FILE := figure.png

all: $(PNG_FILE)

$(PNG_FILE): $(PDF_FILE)
	magick -density 800 $(PDF_FILE) -crop 5100x5100+850+0 +repage $(PNG_FILE)

clean:
	rm -f $(PNG_FILE)

.PHONY: all clean
