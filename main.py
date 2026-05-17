import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# Klasör Oluşturma ve Tema Ayarları
# -----------------------------------
os.makedirs("graphs", exist_ok=True)

# Grafiklerin profesyonel görünmesi için Seaborn teması
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 11, 'axes.labelsize': 12, 'axes.titlesize': 14})

# -----------------------------------
# Dataset Yükleme ve Ön İşleme
# -----------------------------------
# Dosya yolunu kendi proje klasör yapınıza göre ("data/ev_battery_degradation_v1.csv") ayarlayabilirsiniz
df = pd.read_csv("data/ev_battery_degradation_v1.csv")
df.columns = df.columns.str.strip()

print("Veri Seti Başarıyla Yüklendi. Satır Sayısı:", len(df))

# -----------------------------------
# 1. Batarya Sağlığı vs Şarj Döngüsü (Kimya Ayrımı ile)
# -----------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

sns.scatterplot(
    x='Total_Charging_Cycles',
    y='SoH_Percent',
    hue='Battery_Type',  # LFP ve NMC farkını net bir şekilde ortaya koyar
    alpha=0.5,           # Yoğunluk bölgelerini görebilmek için saydamlık
    palette='Set1',
    data=df,
    ax=ax
)

ax.set_title("Battery Health (SoH) Decay over Charging Cycles")
ax.set_xlabel("Total Charging Cycles")
ax.set_ylabel("State of Health (%)")
ax.legend(title="Battery Chemistry")

plt.savefig("graphs/1_charging_cycles_vs_soh_advanced.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------
# 2. Fiziksel Aşınma: İç Direnç vs Batarya Sağlığı (Yeni İçgörü Grafiği)
# -----------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

sns.scatterplot(
    x='Internal_Resistance_Ohm',
    y='SoH_Percent',
    hue='Battery_Type',
    alpha=0.5,
    palette='Set1',
    data=df,
    ax=ax
)

ax.set_title("The Physical Indicator of Degradation: Internal Resistance vs SoH")
ax.set_xlabel("Internal Resistance ($\Omega$)")
ax.set_ylabel("State of Health (%)")
ax.legend(title="Battery Chemistry")

plt.savefig("graphs/2_internal_resistance_vs_soh.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------
# 3. Batarya Kimyalarına Göre Sağlık Dağılımı (KDE Plot)
# -----------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

sns.kdeplot(
    data=df,
    x='SoH_Percent',
    hue='Battery_Type',
    fill=True,
    common_norm=False,
    alpha=0.4,
    palette='Set1',
    ax=ax
)

ax.set_title("Density Distribution of State of Health (SoH) by Battery Type")
ax.set_xlabel("State of Health (%)")
ax.set_ylabel("Density")

plt.savefig("graphs/3_soh_density_by_battery_type.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------
# 4. Sürüş Tarzının Batarya Sağlığına Etkisi (İşlevsiz Countplot Yerine)
# -----------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

# Sürüş tarzlarını medyan değerlerine göre en sağlıkludan en düşüğe sıralıyoruz
driving_order = df.groupby('Driving_Style')['SoH_Percent'].median().sort_values(ascending=False).index

sns.boxplot(
    x='Driving_Style',
    y='SoH_Percent',
    order=driving_order,
    palette='Pastel1',
    data=df,
    ax=ax
)

ax.set_title("Impact of Driving Style on Battery State of Health")
ax.set_xlabel("Driving Style")
ax.set_ylabel("State of Health (%)")

plt.savefig("graphs/4_driving_style_vs_soh.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------
# 5. Araç Modellerine Göre Sıralı Batarya Sağlığı
# -----------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Modelleri medyan SoH değerine göre yüksekten düşüğe sıralıyoruz (Görsel okumayı kolaylaştırır)
model_order = df.groupby('Car_Model')['SoH_Percent'].median().sort_values(ascending=False).index

sns.boxplot(
    x='Car_Model',
    y='SoH_Percent',
    order=model_order,
    palette='Set3',
    data=df,
    ax=ax
)

ax.set_title("Battery Health Distribution Across Different Car Models")
ax.set_xlabel("Car Model")
ax.set_ylabel("State of Health (%)")
plt.xticks(rotation=15)

plt.savefig("graphs/5_car_model_vs_soh_sorted.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------
# 6. Çevresel ve Operasyonel Faktörlerin Kombine Analizi (Subplots Grid)
# -----------------------------------
# Sayfayı kalabalıklaştırmamak için 3 zayıf korelasyonlu etkeni tek bir satırda topluyoruz
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Sıcaklık Etkisi
sns.scatterplot(data=df, x='Avg_Temperature_C', y='SoH_Percent', alpha=0.3, color='crimson', ax=axes[0])
axes[0].set_title("Average Temperature vs SoH")
axes[0].set_xlabel("Average Temperature (°C)")
axes[0].set_ylabel("State of Health (%)")

# Hızlı Şarj Oranı Etkisi
sns.scatterplot(data=df, x='Fast_Charge_Ratio', y='SoH_Percent', alpha=0.3, color='darkorange', ax=axes[1])
axes[1].set_title("Fast Charge Ratio vs SoH")
axes[1].set_xlabel("Fast Charge Ratio")
axes[1].set_ylabel("")  # Y ekseni etiketini gizle (ortak kullanım)

# Deşarj Akım Oranı Etkisi
sns.scatterplot(data=df, x='Avg_Discharge_Rate_C', y='SoH_Percent', alpha=0.3, color='teal', ax=axes[2])
axes[2].set_title("Avg Discharge Rate vs SoH")
axes[2].set_xlabel("Average Discharge Rate (C-rate)")
axes[2].set_ylabel("")

plt.suptitle("Impact of Environmental & Operational Factors on Battery Health", fontsize=16, fontweight='bold', y=1.02)
plt.savefig("graphs/6_operational_factors_grid.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------
# 7. Geliştirilmiş Korelasyon Isı Haritası (Korelasyon Matrisi)
# -----------------------------------
fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    fmt=".2f",          # Virgülden sonra iki basamak netlik sağlar
    cmap='coolwarm',
    linewidths=0.5,     # Hücreler arası ince çizgi estetik katar
    ax=ax
)

ax.set_title("Correlation Heatmap of EV Battery Features", pad=20)

plt.savefig("graphs/7_correlation_heatmap_polished.png", dpi=300, bbox_inches='tight')
plt.close()

print("Tüm modern ve içgörü odaklı grafikler 'graphs/' klasörüne başarıyla kaydedildi!")