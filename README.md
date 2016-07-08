This package is used by EOS to package ka-lite as a flatpak, to do so it
contains 2 small scripts:
 + src/wrapper.py will trigger socket activation of the ka-lite server
 + src/kalite-start.sh overcomes a flatpak limitation that it can't call
   commands with arguments
