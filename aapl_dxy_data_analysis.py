import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#Verileri çekme (Yahoo Finance üzerinden)
aapl_data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')  # Apple hisse senedi verileri
dxy_data = yf.download('DX-Y.NYB', start='2020-01-01', end='2024-01-01')  # DXY (USD Endeksi) verileri

#Min-Max Normalizasyonu
# Verileri 0 ile 1 arasında normalize etme
aapl_data['Normalized'] = (aapl_data['Close'] - aapl_data['Close'].min()) / (aapl_data['Close'].max() - aapl_data['Close'].min())
dxy_data['Normalized'] = (dxy_data['Close'] - dxy_data['Close'].min()) / (dxy_data['Close'].max() - dxy_data['Close'].min())

#Z-Skoru Normalizasyonu
# Verileri, ortalama ve standart sapmaya göre normalize etme
aapl_data['Z-Score'] = (aapl_data['Close'] - aapl_data['Close'].mean()) / aapl_data['Close'].std()
dxy_data['Z-Score'] = (dxy_data['Close'] - dxy_data['Close'].mean()) / dxy_data['Close'].std()

#Zaman Serisi Grafikleri 
#matplotlib.pyplot
# Apple ve DXY'nin zaman serisi kapanış fiyatlarını çiziyoruz
plt.figure(figsize=(14, 6))
plt.plot(aapl_data['Close'], label='Apple (AAPL)', color='blue')  # matplotlib.pyplot Apple hisse senedi fiyatı grafiği çizmek
plt.plot(dxy_data['Close'], label='DXY (USD Index)', color='green')  # DXY endeksi fiyatı
plt.title('Kapanış Fiyatları (2020-2024)')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend() #çizilen her bir veri serisinin neyi temsil ettiğini gösterir.
plt.grid(True) #ızgara aktif
plt.show()

# Min-Max Normalizasyon Grafiği
plt.figure(figsize=(14, 6))
plt.plot(aapl_data['Normalized'], label='Apple (Min-Max)', color='blue', alpha=0.8)
plt.plot(dxy_data['Normalized'], label='DXY (Min-Max)', color='green', alpha=0.8)
plt.title('Min-Max Normalizasyon (2020-2024)')
plt.xlabel('Tarih')
plt.ylabel('Normalleştirilmiş Değer')
plt.legend()
plt.grid(True)
plt.show()

# Z-Skoru Normalizasyon Grafiği
plt.figure(figsize=(14, 6))
plt.plot(aapl_data['Z-Score'], label='Apple (Z-Skoru)', color='blue', alpha=0.8)
plt.plot(dxy_data['Z-Score'], label='DXY (Z-Skoru)', color='green', alpha=0.8)
plt.title('Z-Skoru Normalizasyon (2020-2024)')
plt.xlabel('Tarih')
plt.ylabel('Z-Skoru Değerleri')
plt.legend()
plt.grid(True)
plt.show()


#Aşırı Değer (Outlier) Analizi
# Apple için aşırı değerleri belirleme
aapl_q1, aapl_q3 = aapl_data['Close'].quantile(0.25), aapl_data['Close'].quantile(0.75) #veri setindeki kapanış fiyatlarının %25’lik dilimindeki değeri verir.
aapl_iqr = aapl_q3 - aapl_q1
aapl_lower_bound = aapl_q1 - 1.5 * aapl_iqr
aapl_upper_bound = aapl_q3 + 1.5 * aapl_iqr
aapl_outliers = aapl_data[(aapl_data['Close'] < aapl_lower_bound) | (aapl_data['Close'] > aapl_upper_bound)]

# DXY için aşırı değerleri belirleme
dxy_q1, dxy_q3 = dxy_data['Close'].quantile(0.25), dxy_data['Close'].quantile(0.75)
dxy_iqr = dxy_q3 - dxy_q1
dxy_lower_bound = dxy_q1 - 1.5 * dxy_iqr
dxy_upper_bound = dxy_q3 + 1.5 * dxy_iqr
dxy_outliers = dxy_data[(dxy_data['Close'] < dxy_lower_bound) | (dxy_data['Close'] > dxy_upper_bound)]

# Aşırı değerlerin yazdırılması
print("Apple Aşırı Değerler:")
print(aapl_outliers[['Close']])
print("\nDXY Aşırı Değerler:")
print(dxy_outliers[['Close']])

#Aşırı Değer Grafiklerini Çizme
plt.figure(figsize=(14, 6))

# Apple için scatter plot
plt.subplot(1, 2, 1) #Birden fazla grafik. 1 satır ve 2 sütunlu bir figürün ilk (sol) alt grafik alanını aktif hale getirir.
plt.plot(aapl_data.index, aapl_data['Close'], label='Apple (AAPL)', color='blue')  # Apple kapanış fiyatı
plt.scatter(aapl_outliers.index, aapl_outliers['Close'], color='red', label='Aşırı Değerler', zorder=5)  # aşırı değerleri belirtilen koordinatlarda noktalar halinde gösterir.
plt.title('Apple Aşırı Değerler')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.grid(True)

# DXY için scatter plot
plt.subplot(1, 2, 2)
plt.plot(dxy_data.index, dxy_data['Close'], label='DXY (USD Index)', color='green')  # DXY kapanış fiyatı
plt.scatter(dxy_outliers.index, dxy_outliers['Close'], color='red', label='Aşırı Değerler', zorder=5)  # Aşırı değerler
plt.title('DXY Aşırı Değerler')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.grid(True)

plt.tight_layout() #grafik penceresindeki tüm alt grafiklerin düzgün bir şekilde yerleşmesini sağlar.
plt.show()


#Histogram
# Her iki veri setinin histogramlarını ve KDE (Kernel Density Estimation) grafiğini çiziyoruz
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.histplot(aapl_data['Close'], bins=50, kde=True, color='blue')  # seaborn kütp. Apple histogramı çizimi
plt.title('Apple Kapanış Fiyatı Dağılım Histogramı')
plt.xlabel('Fiyat (USD)')

plt.subplot(1, 2, 2)
sns.histplot(dxy_data['Close'], bins=50, kde=True, color='green')  # DXY histogramı
plt.title('DXY Kapanış Fiyatı Dağılım Histogramı')
plt.xlabel('Fiyat (Endeks)')

plt.show()

#İstatistiksel Momentler
# Apple ve DXY için ortalama, standart sapma, çarpıklık (skewness) ve basıklık (kurtosis) hesaplamaları
try:
    aapl_mean = aapl_data['Close'].mean().item()  # Ortalama
    aapl_std_dev = aapl_data['Close'].std().item()  # Standart sapma
    aapl_skewness = aapl_data['Close'].skew().item()  # Çarpıklık (skewness)
    aapl_kurtosis = aapl_data['Close'].kurt().item()  # Basıklık (kurtosis)

    print("Apple İstatistiksel Momentler:")
    print(f"Ortalama: {aapl_mean:.2f}")
    print(f"Standart Sapma: {aapl_std_dev:.2f}")
    print(f"Çarpıklık (Skewness): {aapl_skewness:.2f}")
    print(f"Basıklık (Kurtosis): {aapl_kurtosis:.2f}")
except Exception as e:
    print("Apple verileri için istatistiksel momentler hesaplanırken bir hata oluştu:", str(e))

try:
    dxy_mean = dxy_data['Close'].mean().item()  # Ortalamayı tek değeri döndürürme
    dxy_std_dev = dxy_data['Close'].std().item()  # Standart sapma
    dxy_skewness = dxy_data['Close'].skew().item()  # Çarpıklık (skewness)
    dxy_kurtosis = dxy_data['Close'].kurt().item()  # Basıklık (kurtosis)

    print("\nDXY İstatistiksel Momentler:")
    print(f"Ortalama: {dxy_mean:.2f}")
    print(f"Standart Sapma: {dxy_std_dev:.2f}")
    print(f"Çarpıklık (Skewness): {dxy_skewness:.2f}")
    print(f"Basıklık (Kurtosis): {dxy_kurtosis:.2f}")
except Exception as e:
    print("DXY verileri için istatistiksel momentler hesaplanırken bir hata oluştu:", str(e))

#Volatilite Grafikleri
# Apple ve DXY'nin günlük getiri volatilitesini hesaplayıp grafikle gösteriyoruz
aapl_data['Daily_Return'] = aapl_data['Close'].pct_change()  # Apple hisse senedinin kapanış fiyatlarındaki yüzdesel değişimi hesap.
dxy_data['Daily_Return'] = dxy_data['Close'].pct_change()  # DXY için de aynı işlemi yap

aapl_volatility = aapl_data['Daily_Return'].std() * np.sqrt(252)  # Yıllık volatiliteyi hesapla
dxy_volatility = dxy_data['Daily_Return'].std() * np.sqrt(252)  # Yıllık volatiliteyi hesapla

# Günlük getiri ve volatilite grafiğini çizme
plt.figure(figsize=(14, 6))
plt.plot(aapl_data['Daily_Return'], label=f'Apple Günlük Getiri (Volatilite: {aapl_volatility:.2f})', color='blue')
plt.plot(dxy_data['Daily_Return'], label=f'DXY Günlük Getiri (Volatilite: {dxy_volatility:.2f})', color='green')
plt.title('Günlük Getiri ve Volatilite')
plt.xlabel('Tarih')
plt.ylabel('Günlük Getiri')
plt.legend()
plt.grid(True)
plt.show()

#Boxplot seaborn kütp.
# Apple ve DXY kapanış fiyatları için boxplot grafikleri çiziyoruz
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.boxplot(aapl_data['Close'], color='blue')  # Apple boxplot
plt.title('Apple Kapanış Fiyatı Boxplot')

plt.subplot(1, 2, 2)
sns.boxplot(dxy_data['Close'], color='green')  # DXY boxplot
plt.title('DXY Kapanış Fiyatı Boxplot')
plt.show()

# Hipotez Testi: Apple ve DXY Arasındaki Korelasyon
try:
    # dropna() Verilerin Temizlenmesi: NaN değerlerini çıkartmak 
    aapl_data_clean = aapl_data['Close'].dropna()
    dxy_data_clean = dxy_data['Close'].dropna()

    # Korelasyon ve p-değerini doğru şekilde çıkar
    corr, p_value = stats.pearsonr(aapl_data_clean, dxy_data_clean) #scipy.stats kütüph. ile İki veri seti arasındaki Pearson korelasyon katsayısını ve ilgili p-değerini hesaplar

    # DeprecationWarning hatasını engellemek için
    print(f"\nApple ve DXY Arasındaki Korelasyon: r = {corr[0]:.4f}")
    print(f"p-değeri: {p_value[0]:.4f}")


    # Sonuçların Yorumlanması
    if p_value < 0.05: #Alfa Değeri %5lik hata payı
        print("Apple ve DXY arasında anlamlı bir ilişki vardır.")
    else:
        print("Apple ve DXY arasında anlamlı bir ilişki yoktur.")
except Exception as e:
    print("Apple ve DXY arasındaki korelasyon test edilirken bir hata oluştu:", str(e))
