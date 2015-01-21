pres_ready = $(patsubst %_prezka.rst,%_prezka_ready,$(wildcard *_prezka.rst))

.SUFFIXES: _prezka_ready

all: $(pres_ready)

.PHONY: all clean

%_prezka_ready: %_prezka.rst
	@echo "Making $@ out of $<"
	@hovercraft --auto-console --skip-help ./$< $@

clean:
	@rm -rf $(pres_ready)
