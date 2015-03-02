pres_ready = $(patsubst %_prezka.rst,%_prezka_ready,$(wildcard *_prezka.rst))
static_dir = common_static

.SUFFIXES: _prezka_ready

all: $(pres_ready)

.PHONY: all clean

%_prezka_ready: %_prezka.rst
	@echo "Making $@ out of $<"
	@hovercraft --template hovercraft.cfg --auto-console --skip-help ./$< $@
	@./make_symlinks.sh $(static_dir) $@

clean:
	@rm -rf $(pres_ready)
