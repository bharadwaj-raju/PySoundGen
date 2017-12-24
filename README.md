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

PySoundGen takes a file (`tones_file`) describing the sound wave, and a filename for the output audio file (`output_wav_file`).

    $ ./soundgen.py {tones_file} {output_wav_file} [--play]

`tones_file` is a newline-separated file of space-separated triplets of `(duration, frequency, amplitude%)`. This describes the sound wave.

For example, a file, say `tones.txt`, with:

    4 44 100
	6 440 100
	2 440 50

will produce audio with 4 seconds of 44 Hz waves at 100% amplitude, then 6s of 440 Hz at 100%, then 2s of 440 Hz at 50%.

**NOTE:** The maximum amplitude of a sound card is `32767`. The `amplitude%` value taken is a percentage of this.

**NOTE:** Values `duration` and `frequency` can be decimals.

**NOTE:** Comments can be used in `tones_file` with `#`.

For example,

    $ ./soundgen.py tones.txt output.wav --play

will generate a wav file `output.wav` with audio as described in the `tones.txt` file (see above), and will play the `output.wav`.

Omit `--play` to only generate audio and not play it.

## Sample Music

The following generates the Sa-Re-Ga-Ma-Pa-Dha-Ni-Sa2-Sa2-Ni-Dha-Pa-Ma-Ga-Re-Sa tone from Indian Classical Music:

    $ cat saregama.txt
	2 240 100  # Sa
	2 270 100  # Re
	2 300 100  # Ga
	2 320 100  # Ma
	2 360 100  # Pa
	2 400 100  # Dha
	2 450 100  # Ni
	2 480 100  # Sa2
	0.5 480 0  # Silence
	2 480 100  # Sa2
	2 450 100  # Ni
	2 400 100  # Dha
	2 360 100  # Pa
	2 320 100  # Ma
	2 300 100  # Ga
	2 270 100  # Re
	2 240 100  # Sa

    $ ./soundgen.py saregama.txt saregama.wav

Wav file: [`sample/saregama.wav`](./sample/saregama.wav?raw=true)

Tones file: [`sample/saregama.txt`](./sample/saregama.txt)


