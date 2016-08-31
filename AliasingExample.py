import numpy as np
import matplotlib.pyplot as plt

Freq1 = 4


X2xFreq1 = np.linspace(0, 1, 2*Freq1, endpoint=True)
X4xFreq1 = np.linspace(0, 1, 4*Freq1, endpoint=True)
X8xFreq1 = np.linspace(0, 1, 8*Freq1, endpoint=True)
X16xFreq1 = np.linspace(0, 1, 16*Freq1, endpoint=True)

YArray = []
w1 = 2 * np.pi * Freq1


YArray2xSampling = [np.cos(w1*SamplePoint) for SamplePoint in X2xFreq1]
YArray4xSampling = [np.cos(w1*SamplePoint) for SamplePoint in X4xFreq1]
YArray8xSampling = [np.cos(w1*SamplePoint) for SamplePoint in X8xFreq1]
YArray16xSampling = [np.cos(w1*SamplePoint) for SamplePoint in X16xFreq1]

# 2 * Frequency Sampling
plt.subplot(221)
plt.plot(X2xFreq1,YArray2xSampling)
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("2 Time Freqnecy Sampling")

# 4 * Frequency Sampling
plt.subplot(222)
plt.plot(X4xFreq1,YArray4xSampling)
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("4 Time Freqnecy Sampling")

# 8 * Frequency Sampling
plt.subplot(223)
plt.plot(X8xFreq1,YArray8xSampling)
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("8 Time Freqnecy Sampling")

# 8 * Frequency Sampling
plt.subplot(224)
plt.plot(X16xFreq1,YArray16xSampling)
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("16 Time Freqnecy Sampling")


plt.show()
