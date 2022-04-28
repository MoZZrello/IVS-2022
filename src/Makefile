## @file Makefile
# @brief makefile Ke spuštení programu, zabalení, vyčištění, testovaní, ..
# @author Andrea Michlíková
# @date 27.4.2022
# Spouští se přes příkazový řádek příkazem make [argument]

PACK_NAME=xharma05_xlojdo00_xmichl11_xspirk01
PACK_DIR=..\..\$(PACK_NAME)

all: 

pack: clean doc
	mkdir $(PACK_DIR)
	cd $(PACK_DIR) && mkdir doc && mkdir install && mkdir repo 
	Copy-Item -Path ..\documentation\html\* ..\..\xharma05_xlojdo00_xmichl11_xspirk01\doc -PassThru
	Copy-Item -Path .\XOinstaller.exe ..\..\xharma05_xlojdo00_xmichl11_xspirk01\install -PassThru
	Copy-Item -Path ..\* -Destination ..\..\xharma05_xlojdo00_xmichl11_xspirk01\repo -Recurse
	cd ..\..\ && zip -r $(PACK_NAME).zip $(PACK_NAME)
	rm -r -fo $(PACK_DIR)

clean: 
	rm -r -fo .\__pycache__

test: test_mathlib.py
	pip install numpy
	python test_mathlib.py

doc: 
	doxygen Doxyfile

run: 
	start XOcalc.exe

profile: profiling.py
	python profiling.py <data.txt