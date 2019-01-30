CC := g++
CFLAGS := -Wall -O2
DEBUGFLAGS := -Wall

ROOTSYS := $(HOME)/root
rootconfig := $(ROOTSYS)/bin/root-config
$(eval ROOTFLAGS := $(shell $(rootconfig) --cflags --libs --glibs --evelibs))

tminuit_sample : tminuit_sample.o
	$(CC) $< $(CFLAGS) $(ROOTFLAGS) -lMinuit -o $@

%.o : %.cpp
	$(CC) $< $(CFLAGS) $(ROOTFLAGS) -o $@ -c

clean:
	rm tminuit_sample *.o

.PHONY: clean
