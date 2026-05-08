# GÜNER TÜRKYILMAZ PRO | Manken1453
# Güneş Patlaması ve GPS Senkronizasyon Analiz Aracı

def gunes_firtinasi_kontrol(kp_endeksi):
    print(f"--- Mevcut KP Endeksi: {kp_endeksi} ---")
    if kp_endeksi >= 7:
        return "⚠️ KRİTİK: Şiddetli güneş fırtınası! GPS ve uydu sinyallerinde kesinti riski yüksek."
    elif kp_endeksi >= 5:
        return "🟡 UYARI: Orta şiddetli aktivite. Hassas ölçüm cihazlarını kontrol edin."
    else:
        return "✅ NORMAL: Güneş aktivitesi stabil. Saha operasyonlarına devam edilebilir."

# 2026 Güneş Maksimumu tahmini için test:
mevcut_durum = 8
print(gunes_firtinasi_kontrol(mevcut_durum))
