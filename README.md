Finansal Veri Analizi Projesi

Bu proje, Apple (AAPL) ve DXY (USD Endeksi) gibi finansal varlıkların fiyat davranışlarını analiz etmek üzerine odaklanmaktadır. Yahoo Finance'ten veriler çekilerek bu varlıklar üzerinde çeşitli normalizasyon işlemleri, grafiksel görselleştirme ve istatistiksel analizler gerçekleştirilmiştir.

Kullanılan Kütüphaneler

yfinance: Yahoo Finance'ın hisse senedi verilerini çekmek için kullanıldı.

pandas: Veri manipülasyonu ve analizi için kullanıldı.

numpy: Matematiksel hesaplamalar için kullanıldı.

matplotlib ve seaborn: Verilerin görselleştirilmesi için kullanıldı.

scipy.stats: İstatistiksel analizler ve hipotez testleri için kullanıldı.

Proje Özellikleri



Veri Çekme

Apple (AAPL) ve DXY (USD Endeksi) için 2020-2024 yılları arasındaki fiyat verileri Yahoo Finance üzerinden çekildi.



Normalizasyon

Min-Max Normalizasyonu: Veriler, 0 ile 1 arasında ölçeklendirilerek normalize edildi.

Z-Skoru Normalizasyonu: Veriler, ortalama ve standart sapmaya dayalı olarak normalize edildi.



Grafiksel Görselleştirme

Zaman Serisi Grafikleri: Apple ve DXY'nin kapanış fiyatları zaman serisi grafiği olarak gösterildi.

Normalizasyon Grafikleri: Min-Max ve Z-Skoru normalizasyonları sonrası verilerin zaman serisi grafikleri çizildi.



Aşırı Değer (Outlier) Analizi

Interquartile Range (IQR) yöntemi kullanılarak Apple ve DXY kapanış fiyatları için aşırı değerler belirlendi ve görselleştirildi.



Histogram ve KDE Grafikleri

Her iki veri seti için histogram ve Kernel Density Estimation (KDE) grafikleri çizilerek verilerin dağılımı analiz edildi.



İstatistiksel Momentler

Ortalama, standart sapma, çarpıklık (skewness) ve basıklık (kurtosis) hesaplanarak verilerin istatistiksel özellikleri belirlendi.



Volatilite Analizi

Apple ve DXY'nin günlük getirileri hesaplandı ve bu getirilerden yıllık volatilite hesaplanarak görselleştirildi.



Boxplot Grafikleri

Apple ve DXY'nin kapanış fiyatları üzerine boxplot grafikleri çizilerek veri dağılımının özellikleri görsel olarak sunuldu.



Hipotez Testi: Korelasyon Analizi

Pearson Korelasyon Testi kullanılarak Apple ve DXY arasındaki korelasyon hesaplandı. p-değeri kullanılarak bu iki finansal varlık arasında anlamlı bir ilişki olup olmadığı belirlendi.

Sonuçlar

Bu analiz, Apple ve DXY arasındaki potansiyel ilişkiyi ve bu varlıkların fiyat hareketlerini anlamamıza yardımcı oldu.

p-değeri < 0.05 olduğu durumlarda, iki veri seti arasında istatistiksel olarak anlamlı bir ilişki olduğu sonucuna varıldı. Bu da Apple ve DXY fiyatlarının birlikte hareket edebileceğini gösterir.
