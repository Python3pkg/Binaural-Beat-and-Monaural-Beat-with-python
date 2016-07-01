# Binaural-Beat-and-Monaural-Beat-with-python
This python script enables you to handle your mind state by a kind of "Brain-Wave Controller" which is generally known as Biaural beat or Monoaural beat in a simplified method.

## Use-case: Create and play "Binaural Beat"

For example, if `400` Hz was played in left ear and `430` Hz in the right, then the binaural beat would have a frequency of 30 Hz.

```python
from PyBrainWave.brainbeat.binaural_beat import BinauralBeat
from PyBrainWave.waveform.sine_wave import SineWave

 brain_beat = BinauralBeat()
 brain_beat.wave_form = SineWave()
 brain_beat.play_beat(
    frequencys=(400, 430),
    play_time=10,
    volume=0.5
)
```

### Main-settings

- The wave form of binaural beat is the `SineWave`.
- The parameter of `play_time` is per seconds.


## Installation

Install using pip:

```sh
pip install PyBrainWave
```
or
```sh
pip3 install PyBrainWave
```

### Source code

The source code is currently hosted on GitHub.

- [Binaural-Beat-and-Monaural-Beat-with-python](https://github.com/chimera0/Binaural-Beat-and-Monaural-Beat-with-python)

### Python package index(PyPI)

Binary installers for the latest released version are available at the Python package index.

- [PyBrainWave: Python Package Index](https://pypi.python.org/pypi/PyBrainWave/)

## Dependencies

- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/): v0.2.9 or higher
- [NumPy](http://www.numpy.org/): v1.7.0 or higher

## Licence

- [GPL2](https://github.com/chimera0/Binaural-Beat-and-Monaural-Beat-with-python/blob/master/LICENSE)

## Description

 The function of this library is inducing you to be extreme immersive mind state on the path to peak performance. You can handle your mind state by using this library which is able to control your brain waves by the binaural beat and the monaural beat.


### Concept of Binaural beat and Monaural beat

 According to a popular theory, brain waves such as Delta, Theta, Alpha, Beta, and Gamma rhythms tend to be correlated with mind states. The delta waves(1-3 Hz) are regarded as the slowest brain waves that are typically produced during the deep stages of sleep. The theta waves(4-7 Hz) are offen induced by the meditative state or focusing the mind. The alpha waves(8-12 Hz) are associate with relaxed state. The beta waves(13-29 Hz) normal waking consciousness. The Gamma waves(30-100 Hz) are the fastest of the brain waves and associated with peak concentration and the brain's optimal frequency for cognitive functioning.

 By a theory of the binaural beat, signals of two different frequencies from headphone or earphone are presented separately, one to each ear, your brain detects the phase variation between the frequencies and tries to reconcile that difference. The effect on the brain waves depends on the difference in frequencies of each tone. For example, if 400 Hz was played in one ear and 430 in the other, then the binaural beat would have a frequency of 30 Hz.

 The monaural beats are similar to the binaural beats. But they vary in distinct ways. The binaural beats seem to be "created" or perceived by cortical areas combining the two different frequencies. On the other hand, the monaural beats are due to direct stimulation of the basilar membrane. This makes it possible to hear the beats.

 Please choose either binaural beets or monaural beats. If you set up 5 Hz, your brain waves and the frequency can be tuned and then you are able to be the meditative state or focusing the mind. Or what you choose to be relaxed state is the alpha waves(8-12 Hz).


### References

- Brandy, Queen., et al., (2003) “Binaural Beat Induced Theta EEG Activity and Hypnotic Susceptibility : Contradictory Results and Technical Considerations,” American Journal of Clinical Hypnosis, pp295-309.
- Green, Barry., Gallwey, W. Timothy., (1986) The Inner Game of Music, Doubleday.
- Kennerly, Richard Cauley., (1994) An empirical investigation into the effect of beta frequency binaural beat audio signals on four measures of human memory, Department of Psychology, West Georgia College, Carrolton, Georgia.
- Kim, Jeansok J., Lee, Hongjoo J., Han, Jung-Soo., Packard, Mark G. (2001) “Amygdala Is Critical for Stress-Induced Modulation of Hippocampal Long-Term Potentiation and Learning,” The Journal of Neuroscience, Vol. 21, pp5222-5228.
- LeDoux, Joseph. (1998) The emotional brain : the mysterious underpinnings of emotional life, London : Weidenfeld & Nicolson.
- McEwen, Bruce S., Sapolsky, Robert M. (1995) “Stress and cognitive function,” Current Opinion in Neurobiology, Vol. 5, pp205-216.
- Oster, Gerald., (1973) “Auditory Beats in the Brain,” Scientific American, pp94-102.
- Radford, Benjamin., (2001) “Pokemon Contagion: Photosensitive Epilepsy or Mass Psychogenic Illness?,” Southern Medical Journal, Vol. 94, No. 2, pp197-204.
- Steward, Oswald., (2000) Functional neuroscience, Springer.
- Swann, R., et al. (1982) The Brain ? A User’s Manual, New York: G. P. Putnam’s Sons.
- Takeo, Takahashi., et al., (1999) “Pokemon seizures,” Neurol J Southeast Asia, Vol. 4, pp1-11.
- Vollenweider., Franz X., Geyer., Mark A. (2001) “A systems model of altered consciousness: Integrating natural and drug-induced psychoses,” Brain Research Bulletin, Vol. 56, No. 5, pp495-507.
- Wahbeh, Helane., Calabrese, Carlo., Zwickey, Heather., (2007) “Binaural Beat Technology in Humans : A Pilot Study to Assess Psychologic and Physiologic Effects,” The Journal of Alternative and Complementary Medicine, Vol. 13, No. 1, pp25-32.
- Westman, Jack C., Walters, James R. (1981) “Noise and Stress : A Comprehensive Approach,” Environmental Health Perspectives, Vol. 41, pp291-309.

## Author

- [chimera0](https://github.com/chimera0)

