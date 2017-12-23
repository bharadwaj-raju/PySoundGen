import math
import sys
import wave
import array
import subprocess as sp
from collections import namedtuple
import base64
import hashlib

# Usage: soundgen.py seconds,freq,amplitude [...] [--play]

Tone = namedtuple('Tone', 'duration freq amplitude')

tones_raw = [x for x in sys.argv[1:] if x != '--play']
tones = []

for tone_raw in tones_raw:
	tones.append(Tone(*[int(x) for x in tone_raw.split(',')]))

data = array.array('h') # signed short integer (-32768 to 32767) data
						# -32768 to 32767 is the max amplitude of a sound card

sample_rate = 44100  # samples/second, 44100 = CD Quality Audio
n_channels = 1  # of channels (1 = mono, 2 = stereo)
data_size = 2  # 2 bytes because of using signed short integers => bit depth = 16

for tone in tones:
	n_samples_per_cycle = int(sample_rate / tone.freq)
	n_samples = sample_rate * tone.duration
	for i in range(n_samples):
		sample = 32767 * float(tone.amplitude) / 100
		sample *= math.sin(math.pi * 2 * (i % n_samples_per_cycle) / n_samples_per_cycle)
		data.append(int(sample))

uid = hashlib.md5(base64.b64encode(data.tostring())).hexdigest()

with wave.open('Sound_%s.wav' % uid, 'w') as f:
	f.setparams((n_channels, data_size, sample_rate, n_samples, "NONE", "Uncompressed"))
	f.writeframes(data.tostring())

print('Sound_%s.wav' % uid)

if '--play' in sys.argv:
	sp.Popen(['aplay', 'Sound_%s.wav' % uid]).wait()

