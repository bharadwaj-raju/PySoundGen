#!/usr/bin/env python3

import math
import sys
import wave
import array
import subprocess as sp
from collections import namedtuple

# Usage: soundgen.py tones_file wav_output_file [--play]

Tone = namedtuple('Tone', 'duration freq amplitude')

tones_file = sys.argv[1]
wav_output_file = sys.argv[2]

tones = []

with open(tones_file) as f:
	for line in f:
		if not line.startswith('#') and line:
			line = line.strip()
			line = line.split()[:3]
			#duration =
			tones.append(Tone(*[float(x) for x in line]))

data = array.array('h') # signed short integer (-32768 to 32767) data
						# -32768 to 32767 is the max amplitude of a sound card

sample_rate = 44100  # samples/second, 44100 = CD Quality Audio
n_channels = 1  # of channels (1 = mono, 2 = stereo)
data_size = 2  # 2 bytes because of using signed short integers => bit depth = 16

for tone in tones:
	n_samples_per_cycle = int(sample_rate / tone.freq)
	n_samples = int(sample_rate * tone.duration)
	for i in range(n_samples):
		sample = 32767 * float(tone.amplitude) / 100
		sample *= math.sin(math.pi * 2 * (i % n_samples_per_cycle) / n_samples_per_cycle)
		data.append(int(sample))

with wave.open(wav_output_file, 'w') as f:
	f.setparams((n_channels, data_size, sample_rate, n_samples, "NONE", "Uncompressed"))
	f.writeframes(data.tostring())

if '--play' in sys.argv:
	sp.Popen(['aplay', wav_output_file]).wait()

