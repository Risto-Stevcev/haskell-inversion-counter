GHC = ghc

.PHONY:
default: Main
	
.PHONY:
test: TestInversionCounter

Main:
	$(GHC) Main.hs -o Main

TestInversionCounter:
	$(GHC) TestInversionCounter.hs -o TestInversionCounter

.PHONY:
all: clean default test

.PHONY:
clean:
	rm -f *.o *.hi *.*~ TestInversionCounter Main
