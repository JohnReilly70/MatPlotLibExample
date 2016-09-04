import numpy as np
import matplotlib.pyplot as plt

Freq1 = 4

#X?xFreq1 creates the number of sample points based off the Freq1 multipled by ?
X2xFreq1 = np.linspace(0, 1, 2*Freq1, endpoint=True)
X4xFreq1 = np.linspace(0, 1, 4*Freq1, endpoint=True)
X8xFreq1 = np.linspace(0, 1, 8*Freq1, endpoint=True)
X16xFreq1 = np.linspace(0, 1, 16*Freq1, endpoint=True)
X32xFreq1 = np.linspace(0, 1, 32*Freq1, endpoint=True)
X64xFreq1 = np.linspace(0, 1, 64*Freq1, endpoint=True)

YArray = []
w1 = 2 * np.pi * Freq1


YArray2xSamples = [np.cos(w1*SamplePoint) for SamplePoint in X2xFreq1]
YArray4xSamples = [np.cos(w1*SamplePoint) for SamplePoint in X4xFreq1]
YArray8xSamples = [np.cos(w1*SamplePoint) for SamplePoint in X8xFreq1]
YArray16xSamples = [np.cos(w1*SamplePoint) for SamplePoint in X16xFreq1]
YArray32xSamples = [np.cos(w1*SamplePoint) for SamplePoint in X32xFreq1]
YArray64xSamples = [np.cos(w1*SamplePoint) for SamplePoint in X64xFreq1]

title_string = ['Signal Frequency = ', str(Freq1), "Hz"]
s = "".join(title_string)
plt.suptitle(s)

# 2 * Frequency Samples
plt.subplot(231)
plt.plot(X2xFreq1,YArray2xSamples,'bo', X2xFreq1,YArray2xSamples, 'k')
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("2 Time Freqnecy Samples")

# 4 * Frequency Samples
plt.subplot(232)
plt.plot(X4xFreq1,YArray4xSamples, 'bo', X4xFreq1,YArray4xSamples, 'k')
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("4 Time Freqnecy Samples")

# 8 * Frequency Samples
plt.subplot(233)
plt.plot(X8xFreq1,YArray8xSamples, 'bo', X8xFreq1,YArray8xSamples, 'k')
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("8 Time Freqnecy Samples")

# 16 * Frequency Samples
plt.subplot(234)
plt.plot(X16xFreq1,YArray16xSamples, 'bo', X16xFreq1,YArray16xSamples, 'k')
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("16 Time Freqnecy Samples")

# 32 * Frequency Samples
plt.subplot(235)
plt.plot(X32xFreq1,YArray32xSamples, 'bo', X32xFreq1,YArray32xSamples, 'k')
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("32 Time Freqnecy Samples")

# 64 * Frequency Samples
plt.subplot(236)
plt.plot(X64xFreq1,YArray64xSamples, 'bo', X64xFreq1,YArray64xSamples, 'k')
plt.xlabel('Time, Seconds')
plt.ylabel('Magnitue')
plt.title("64 Time Freqnecy Samples")


plt.show()
