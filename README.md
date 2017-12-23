# PySoundGen

Python script to generate sounds and music from sound waves.

![plot](plot.png)


Waveform formula from http://code.activestate.com/recipes/578168-sound-generator-using-wav-file/

[Sample music produced by PySoundGen](#sample-music)

License: MIT


## Dependencies

  - Python 3
  - To use the `--play`  option, `aplay` is needed. This should be installed by default in most Linux distros.


## Usage

Latest iteration.

Allows you to specify a series of tones, each tone being an ordered triplet `(duration, frequency, amplitude%)`.

    $ python3 soundgen.py {duration},{freq},{amplitude%} [...] [--play]

For example,

    $ python3 soundgen.py 4,44,100 6,440,100 2,440,50 --play

generates a wav audio with 4 seconds of 44 Hz waves at 100% amplitude, then 6s of 440 Hz at 100%, then 2s of 440 Hz at 50%,
and plays the resulting wav (`--play`). Omit `--play` to only generate audio and not play it.

**NOTE:** The format of a tone must be *exactly* `{duration},{freq},{amplitude%}`. No extra spaces, no order changes, etc.


## Sample Music

The following generates the Sa-Re-Ga-Ma-Pa-Dha-Ni tone from Indian Classical Music:

    $ python3 soundgen.py 2,240,100 2,270,100 2,300,100 2,320,100 2,360,100 2,400,100 2,450,100

Wav file: [`Sound_369dfa0e70a58dc0c71433488de8270f.wav`](./Sound_369dfa0e70a58dc0c71433488de8270f.wav)


