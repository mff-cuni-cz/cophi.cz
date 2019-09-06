.PHONY: clean

pdfs: instruct/instruct.pdf

%.pdf: %.tex
	pdfcsplain $<

clean:
	rm -f -- *.pdf *.log *.ref
