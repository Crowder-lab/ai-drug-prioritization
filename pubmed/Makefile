ABSTRACT_FINDER_SCRIPT := abstract_finder.R
DATA_FILE := data.xml
ABSTRACTS_FILE := abstracts.xml

all: $(ABSTRACTS_FILE)

$(ABSTRACTS_FILE): $(DATA_FILE)
	cat data.xml | hxselect -s '\n' "AbstractText" > $(ABSTRACTS_FILE)

$(DATA_FILE): $(ABSTRACT_FINDER_SCRIPT)
	Rscript $(ABSTRACT_FINDER_SCRIPT)

clean:
	rm -f $(DATA_FILE) $(ABSTRACTS_FILE)

.PHONY: all clean
