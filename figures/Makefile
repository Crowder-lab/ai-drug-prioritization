PDF_FILE := Drug_Manuscript.pdf
PNG_FILE := figure.png

all: $(PNG_FILE)

$(PNG_FILE): $(PDF_FILE)
	magick -density 800 $(PDF_FILE) -crop 6800x6800+0+0 +repage $(PNG_FILE)
	touch $@

clean:
	rm -f $(PNG_FILE)

.PHONY: all clean
