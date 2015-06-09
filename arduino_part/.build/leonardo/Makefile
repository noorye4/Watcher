


















.build/leonardo/Wire/utility/twi.o : lib/Wire/utility/twi.c
	@echo [93mWire/utility/twi.c[0m
	@mkdir -p .build/leonardo/Wire/utility
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c lib/Wire/utility/twi.c
include .build/leonardo/Wire/utility/twi.d






.build/leonardo/Wire/Wire.o : lib/Wire/Wire.cpp
	@echo [93mWire/Wire.cpp[0m
	@mkdir -p .build/leonardo/Wire
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c lib/Wire/Wire.cpp
include .build/leonardo/Wire/Wire.d



.build/leonardo/Wire/libWire.a : .build/leonardo/Wire/utility/twi.o .build/leonardo/Wire/Wire.o
	@echo [92mLinking libWire.a[0m
	@/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs $@ $^







.build/leonardo/arduino/wiring_pulse.o : /usr/share/arduino/hardware/arduino/cores/arduino/wiring_pulse.c
	@echo [93marduino/wiring_pulse.c[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/wiring_pulse.c
include .build/leonardo/arduino/wiring_pulse.d

.build/leonardo/arduino/wiring_analog.o : /usr/share/arduino/hardware/arduino/cores/arduino/wiring_analog.c
	@echo [93marduino/wiring_analog.c[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/wiring_analog.c
include .build/leonardo/arduino/wiring_analog.d

.build/leonardo/arduino/wiring_digital.o : /usr/share/arduino/hardware/arduino/cores/arduino/wiring_digital.c
	@echo [93marduino/wiring_digital.c[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/wiring_digital.c
include .build/leonardo/arduino/wiring_digital.d

.build/leonardo/arduino/wiring_shift.o : /usr/share/arduino/hardware/arduino/cores/arduino/wiring_shift.c
	@echo [93marduino/wiring_shift.c[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/wiring_shift.c
include .build/leonardo/arduino/wiring_shift.d

.build/leonardo/arduino/WInterrupts.o : /usr/share/arduino/hardware/arduino/cores/arduino/WInterrupts.c
	@echo [93marduino/WInterrupts.c[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/WInterrupts.c
include .build/leonardo/arduino/WInterrupts.d

.build/leonardo/arduino/wiring.o : /usr/share/arduino/hardware/arduino/cores/arduino/wiring.c
	@echo [93marduino/wiring.c[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/wiring.c
include .build/leonardo/arduino/wiring.d

.build/leonardo/arduino/avr-libc/malloc.o : /usr/share/arduino/hardware/arduino/cores/arduino/avr-libc/malloc.c
	@echo [93marduino/avr-libc/malloc.c[0m
	@mkdir -p .build/leonardo/arduino/avr-libc
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/avr-libc/malloc.c
include .build/leonardo/arduino/avr-libc/malloc.d

.build/leonardo/arduino/avr-libc/realloc.o : /usr/share/arduino/hardware/arduino/cores/arduino/avr-libc/realloc.c
	@echo [93marduino/avr-libc/realloc.c[0m
	@mkdir -p .build/leonardo/arduino/avr-libc
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc   -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/avr-libc/realloc.c
include .build/leonardo/arduino/avr-libc/realloc.d






.build/leonardo/arduino/Tone.o : /usr/share/arduino/hardware/arduino/cores/arduino/Tone.cpp
	@echo [93marduino/Tone.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/Tone.cpp
include .build/leonardo/arduino/Tone.d

.build/leonardo/arduino/IPAddress.o : /usr/share/arduino/hardware/arduino/cores/arduino/IPAddress.cpp
	@echo [93marduino/IPAddress.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/IPAddress.cpp
include .build/leonardo/arduino/IPAddress.d

.build/leonardo/arduino/WString.o : /usr/share/arduino/hardware/arduino/cores/arduino/WString.cpp
	@echo [93marduino/WString.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/WString.cpp
include .build/leonardo/arduino/WString.d

.build/leonardo/arduino/WMath.o : /usr/share/arduino/hardware/arduino/cores/arduino/WMath.cpp
	@echo [93marduino/WMath.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/WMath.cpp
include .build/leonardo/arduino/WMath.d

.build/leonardo/arduino/HID.o : /usr/share/arduino/hardware/arduino/cores/arduino/HID.cpp
	@echo [93marduino/HID.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/HID.cpp
include .build/leonardo/arduino/HID.d

.build/leonardo/arduino/Stream.o : /usr/share/arduino/hardware/arduino/cores/arduino/Stream.cpp
	@echo [93marduino/Stream.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/Stream.cpp
include .build/leonardo/arduino/Stream.d

.build/leonardo/arduino/new.o : /usr/share/arduino/hardware/arduino/cores/arduino/new.cpp
	@echo [93marduino/new.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/new.cpp
include .build/leonardo/arduino/new.d

.build/leonardo/arduino/HardwareSerial.o : /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp
	@echo [93marduino/HardwareSerial.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp
include .build/leonardo/arduino/HardwareSerial.d

.build/leonardo/arduino/main.o : /usr/share/arduino/hardware/arduino/cores/arduino/main.cpp
	@echo [93marduino/main.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/main.cpp
include .build/leonardo/arduino/main.d

.build/leonardo/arduino/Print.o : /usr/share/arduino/hardware/arduino/cores/arduino/Print.cpp
	@echo [93marduino/Print.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/Print.cpp
include .build/leonardo/arduino/Print.d

.build/leonardo/arduino/USBCore.o : /usr/share/arduino/hardware/arduino/cores/arduino/USBCore.cpp
	@echo [93marduino/USBCore.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/USBCore.cpp
include .build/leonardo/arduino/USBCore.d

.build/leonardo/arduino/CDC.o : /usr/share/arduino/hardware/arduino/cores/arduino/CDC.cpp
	@echo [93marduino/CDC.cpp[0m
	@mkdir -p .build/leonardo/arduino
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c /usr/share/arduino/hardware/arduino/cores/arduino/CDC.cpp
include .build/leonardo/arduino/CDC.d



.build/leonardo/arduino/libarduino.a : .build/leonardo/arduino/wiring_pulse.o .build/leonardo/arduino/wiring_analog.o .build/leonardo/arduino/wiring_digital.o .build/leonardo/arduino/wiring_shift.o .build/leonardo/arduino/WInterrupts.o .build/leonardo/arduino/wiring.o .build/leonardo/arduino/avr-libc/malloc.o .build/leonardo/arduino/avr-libc/realloc.o .build/leonardo/arduino/Tone.o .build/leonardo/arduino/IPAddress.o .build/leonardo/arduino/WString.o .build/leonardo/arduino/WMath.o .build/leonardo/arduino/HID.o .build/leonardo/arduino/Stream.o .build/leonardo/arduino/new.o .build/leonardo/arduino/HardwareSerial.o .build/leonardo/arduino/main.o .build/leonardo/arduino/Print.o .build/leonardo/arduino/USBCore.o .build/leonardo/arduino/CDC.o
	@echo [92mLinking libarduino.a[0m
	@/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs $@ $^















.build/leonardo/src/compass.o : src/compass.cpp
	@echo [93msrc/compass.cpp[0m
	@mkdir -p .build/leonardo/src
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions  -o $@ -c src/compass.cpp
include .build/leonardo/src/compass.d

.build/leonardo/src/sketch.o : .build/leonardo/src/sketch.cpp
	@echo [93msrc/sketch.cpp[0m
	@mkdir -p .build/leonardo/src
	@/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=105 -I/usr/share/arduino/hardware/arduino/cores/arduino -ffunction-sections -fdata-sections -g -Os -w -DUSB_VID=0x2341 -DUSB_PID=0x8036 -I/usr/share/arduino/hardware/arduino/variants/leonardo -Ilib/Wire -Ilib/Wire/utility -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/cores/arduino/avr-libc -fno-exceptions -iquote src  -o $@ -c .build/leonardo/src/sketch.cpp
include .build/leonardo/src/sketch.d







.build/leonardo/firmware.elf : .build/leonardo/src/compass.o .build/leonardo/src/sketch.o .build/leonardo/Wire/libWire.a .build/leonardo/arduino/libarduino.a
	@echo [92mLinking firmware.elf[0m
	@/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -mmcu=atmega32u4 -Wl,-Os -Wl,--gc-sections -o $@ $^ -lm


.build/leonardo/firmware.hex : .build/leonardo/firmware.elf
	@echo [92mConverting to firmware.hex[0m
	@/usr/share/arduino/hardware/tools/avr/bin/avr-objcopy -O ihex -R .eeprom $^ $@

include .build/leonardo/src/dependencies.d .build/leonardo/arduino/dependencies.d .build/leonardo/Wire/dependencies.d

all : .build/leonardo/firmware.hex
	@true

