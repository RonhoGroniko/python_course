import librosa
import librosa.display
import librosa.feature
import IPython
import IPython.display as ipd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.fft import fft
import sklearn


audio_data = '10-second-count-down.mp3'
y, sr = librosa.load(audio_data)


plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr)
plt.show()

spectrum = fft(y)

frequencies = np.fft.fftfreq(len(spectrum), 1 / sr)

plt.figure(figsize=(8, 4))
plt.plot(frequencies[:len(frequencies) // 2], np.abs(spectrum[:len(spectrum) // 2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()

y_harmonic, y_percussive = librosa.effects.hpss(y)
plt.figure(figsize=(15, 5))
librosa.display.waveshow(y_harmonic, sr=sr, alpha=0.25)
librosa.display.waveshow(y_percussive, sr=sr, color='r', alpha=0.5)
plt.title('Harmonic + Percussive')

# Beat Extraction
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
print('Detected Tempo: '+str(tempo)+ ' beats/min')
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
beat_time_diff=np.ediff1d(beat_times)
beat_nums = np.arange(1, np.size(beat_times))

print(beat_nums)

fig, ax = plt.subplots()
fig.set_size_inches(15, 5)
ax.set_ylabel("Time difference (s)")
ax.set_xlabel("Beats")
# Ошибка произошла, потому что sns.barplot ожидала,
# что значения для осей x и y будут указаны как именованные аргументы,
# а не просто переданы по порядку.
g = sns.barplot(x=beat_nums, y=beat_time_diff, palette="BuGn_d", hue=beat_nums, ax=ax, legend=False)
g.set(xticklabels=[])
plt.show()

# Calculate MFCCs
mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=20)
plt.figure(figsize=(15, 5))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.show()
print(mfccs)

# Spectral Centroid
cent = librosa.feature.spectral_centroid(y=y, sr=sr)
plt.figure(figsize=(15,5))
plt.subplot(1, 1, 1)
plt.semilogy(cent.T, label='Spectral centroid')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, cent.shape[-1]])
plt.legend()
plt.show()


spectral_centroids = cent[0]
spectral_centroids.shape

# Вычисление временной переменной для визуализации
plt.figure(figsize=(12, 4))
frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)

# Нормализация спектрального центроида для визуализации
def normalize(y, axis=0):
    return sklearn.preprocessing.minmax_scale(y, axis=axis)

# Построение спектрального центроида вместе с формой волны
librosa.display.waveshow(y, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_centroids), color='b')
plt.show()
