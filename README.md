# RemoteCarController
Simple python program that creates pulse signals on an arbitrary waveform generator to simulate signal from a remote car controller.

## Project Description
The idea is to teach the children a little something about radio waves and how they are used in the real world, like driving a remote control car. The way the car works is that the controller sends a series of pulses at 49.9 MHz, and the number of pulses tells the car which way to go. The code for “forward” is 4 long pulses of 49.9 MHz followed by 10 short pulses; “backward” is 4 long pulses followed by 40 short pulses; etc. (A long pulse is 2.1 ms ON followed by 0.7 ms OFF. The short pulse is 0.7 ms ON followed by 0.7 ms OFF.) The pulse series repeats for however many seconds the user holds down the forward/reverse/etc levers.

## Required equipment
*  Agilent 33220A Arbitrary Waveform Generator (GPIB Address: 8)
*  Signal Source or waveform generator to generate a constant 49.9 MHz signal.

## Tools
*  Python 3.6
*  PyCharm: python IDE
*  Qt Designer: to create UI form
   - Default location: C:\Program Files (x86)\Python36-32\Lib\site-packages\pyqt5-tools\
   - To convert ui form to python file: pyuic5 -x Main.ui -o Main.py
*  pyinstaller: to build exe from python
   - Default location: C:\Program Files (x86)\Python36-32\Scripts\
   - To create executable: pyinstaller.exe --onefile --windowed Main.py

## Project dependencies
*  PyQt5
*  PyVISA (requires NI-VISA library)

## Class Diagram
[ClassDiagram.docx](/uploads/ffaa473af7e96d087d3d329b8890331a/ClassDiagram.docx)
