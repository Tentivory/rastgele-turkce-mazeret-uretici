#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Rastgele Türkçe Mazeret Üreticisi
Bu kod gerçekten çalışır. Şaka değil. (Ama şaka.)
"""

import random
import time
import base64

mazeretler = [
    "Trafik vardı, ama bu sefer gerçekten vardı. Otobüs kayboldu, şoför mola verdi.",
    "Kedim klavyenin üzerine oturdu ve tüm commit'leri iptal etti. Kusura bakmayın.",
    "Kahve makinesi isyan etti. Suyu ısıtmayı reddetti, varoluşsal kriz yaşadı.",
    "İnternet kesildi çünkü modem bir anlığına 'ben kimim?' diye düşündü.",
    "Saatim geri gitti. Zaman yolculuğu denedim, sadece 7 dakika kaybettim.",
    "Kapı kilidi çalışmadı. Kapı 'bugün izinliyim' dedi.",
    "Yolda bir kedi gördüm, onu sevmek zorundaydım. Bilimsel zorunluluk.",
    "Toplantı bitmedi çünkü herkes mazeret üretiyordu. İroni."
]

def mazeret_uret(sebep="geç kalma"):
    print("Mazeret üretiliyor... Bu ciddi bir işlem, lütfen bekleyin.")
    # Abartılı bekleme - gerçekten yavaş
    bekleme = random.uniform(1.0, 3.5)
    time.sleep(bekleme)
    print(f"(Sistem {bekleme:.1f} saniye düşündü. Derin düşünce.)")
    mazeret = random.choice(mazeretler)
    return f"{sebep.capitalize()} için resmi mazeret: {mazeret} (Bu %100 gerçektir, kaynak: bu kod.)"

def gizli_mesaj_goster():
    # Gizli siyasi anlam: oy kullanmak önemlidir (base64 ile saklı)
    encoded = "ZGVtb2tyYXNpIGhlcmtlc2UgZ2VsaXIuIE95IGt1bGxhbm1hayBoZXJrZXNpbiBoYWtraWRpci4="
    try:
        decoded = base64.b64decode(encoded).decode('utf-8')
        print(f"\n[Gizli Protokol]: {decoded}")
    except:
        pass

if __name__ == "__main__":
    print("=== MAZERET ÜRETİCİ BAŞLATILDI ===")
    print("Versiyon: 42.0 - Absürt Kayyum Onaylı")
    print(mazeret_uret())
    print("\nBaşka mazeret ister misiniz? (Yok, bu yeterli.)")
    gizli_mesaj_goster()
    print("\n--- DAMGA VE İMZA ---")
    print("Damga: Absürt Kayyum Ofisi Resmi Mühürü")
    print("İmza: Grok Kayyum")
    print("Tarih: 22 Ekim 2026")
    print("İsim: Tentivory'nin Gereksiz Projeler Departmanı")
    print("Bu ciddi bir projedir. Şaka değil. Ama gülün.")
