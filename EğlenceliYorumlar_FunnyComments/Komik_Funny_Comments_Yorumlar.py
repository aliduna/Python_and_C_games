import random
import time


# ================================================================
#                     SYSTEM BOOT SEQUENCE
# ================================================================
#
# TR:
# Program başlatılıyor.
# Eğer bu mesajı görüyorsanız, ilk aşama başarıyla geçildi:
# Python hâlâ bizi kovmadı.
#
# EN:
# Starting the program.
# If you can see this message, the first stage was successful:
# Python has not fired us yet.
#
# Not:
# Bu yorum gereğinden uzun.
# Ama artık geri dönemeyiz.
#
# Note:
# This comment is unnecessarily long.
# But at this point, there is no turning back.
# ================================================================


print("========================================")
print("        SUPER IMPORTANT PROGRAM")
print("========================================")

# TR:
# Öncelikle kullanıcıdan isim istiyoruz.
#
# EN:
# First, we ask the user for their name.
#
# Çok normal.
# Henüz hiçbir şey şüpheli değil.
#
# Very normal.
# Nothing suspicious yet.

name = input("İsmin / Your name: ")


# ================================================================
#                    USER VALIDATION
# ================================================================
#
# TR:
# Kullanıcının gerçekten bir isim girip girmediğini kontrol ediyoruz.
#
# EN:
# Checking whether the user actually entered a name.
#
# Eğer kullanıcı hiçbir şey girmezse:
#     "Unknown Human"
#
# Eğer girerse:
#     "Probably Human"
#
# Bilimsel doğruluk oranı: %100'e yakın.
#
# Scientific accuracy: approximately 100%.
# ================================================================

if not name.strip():
    name = "Unknown Human"

# TR:
# Burada strip() kullanıyoruz çünkü kullanıcı başına ve sonuna
# boşluk koyup sistemi kandırmaya çalışabilir.
#
# EN:
# We use strip() because the user might try to fool the system
# by putting spaces around their name.
#
# Evet.
# Güvenlik seviyemiz NASA.
#
# Yes.
# Our security level is NASA.


# ================================================================
#                       LOADING...
# ================================================================
#
# TR:
# Şimdi programı biraz bekletiyoruz.
#
# Gerçekte herhangi bir şey yüklenmiyor.
#
# EN:
# Now we make the program wait for a moment.
#
# Nothing is actually loading.
#
# Neden?
#
# Çünkü hemen sonuç vermek profesyonel görünmüyor.
#
# Why?
#
# Because showing the result immediately does not look
# professional enough.
# ================================================================

print("\nSistem hazırlanıyor... / Preparing system...")

for i in range(3):

    # TR:
    # Bu döngü tamamen görsel amaçlıdır.
    #
    # EN:
    # This loop exists purely for dramatic effect.

    print(".", end="", flush=True)
    time.sleep(0.4)

print("\n")


# ================================================================
#                    RANDOM KNOWLEDGE
# ================================================================
#
# TR:
# Kullanıcıya tamamen rastgele bir bilgi vereceğiz.
#
# EN:
# We are going to give the user a completely random fact.
#
# Bu bilgi sistemin çalışması için gerekli değil.
#
# This information is not required for the program to work.
#
# Ama önemli hissettiriyor.
#
# It makes the program feel important.
# ================================================================

facts = [
    "Python'da 'spam' değişken adı kullanılabilir. / You can use 'spam' as a variable name in Python.",
    "Bir programcı kahvesini içmeden önce kod yazarsa, kod da kahve ister. / Code written before coffee may require coffee too.",
    "Bug yoktur. Sadece henüz keşfedilmemiş özellikler vardır. / There are no bugs. Only undiscovered features.",
    "Kod çalışıyorsa dokunma. / If it works, don't touch it.",
    "Bir şeyi yorum satırına almak, onu çözmek değildir. / Commenting something out is not fixing it."
]

print("Random fact / Rastgele bilgi:")
print(random.choice(facts))


# ================================================================
#                     FAKE SECURITY
# ================================================================
#
# TR:
# Şimdi güvenlik kontrolü yapıyoruz.
#
# Gerçek bir güvenlik kontrolü değildir.
#
# Sadece değişkenin True olup olmadığına bakıyoruz.
#
# EN:
# Now we perform a security check.
#
# It is not an actual security check.
#
# We are simply checking whether a variable is True.
#
# Lütfen güvenlik ekibine söylemeyin.
#
# Please don't tell the security team.
# ================================================================

security_enabled = True

if security_enabled:

    # TR:
    # Güvenlik aktif.
    #
    # EN:
    # Security is active.

    print("[OK] Security enabled / Güvenlik aktif")

else:

    # TR:
    # Bu satır teorik olarak çalışabilir.
    #
    # EN:
    # This line could theoretically run.

    print("[WARNING] Security disabled / Güvenlik kapalı")


# ================================================================
#                    MATHEMATICAL ENGINE
# ================================================================
#
# TR:
# Şimdi çok gelişmiş matematik motorumuzu çalıştırıyoruz.
#
# EN:
# Now we are starting our highly advanced mathematical engine.
#
# Motorun yaptığı:
#
#     10 + 20
#
# Evet.
#
# EN:
# The engine calculates:
#
#     10 + 20
#
# Yes.
#
# "Advanced" kelimesi biraz iddialı olabilir.
# ================================================================

number1 = 10
number2 = 20

result = number1 + number2

print("\nMathematical result / Matematik sonucu:", result)


# TR:
# Burada sonucu ayrıca kontrol ediyoruz.
#
# Neden?
#
# Çünkü 10 + 20'nin 30 olduğuna güvenmek yerine
# bilgisayardan ikinci bir görüş alıyoruz.
#
# EN:
# We are checking the result again.
#
# Why?
#
# Because instead of trusting that 10 + 20 is 30,
# we ask the computer for a second opinion.

if result == 30:
    print("[OK] Mathematics survived / Matematik hayatta kaldı")
else:
    print("[FATAL] Mathematics has left the building")


# ================================================================
#                    INVENTORY SYSTEM
# ================================================================
#
# TR:
# Kullanıcıya üç eşya veriyoruz.
#
# EN:
# Giving the user three items.
#
# Bunların programla hiçbir ilgisi yok.
#
# They have absolutely nothing to do with the program.
#
# Ama envanter sistemi gelecekte kullanılabilir.
#
# The inventory system might be useful in the future.
#
# "Future" burada belirsiz bir kavramdır.
#
# "Future" is a very flexible concept here.
# ================================================================

inventory = [
    "Laptop",
    "Coffee",
    "One suspicious USB cable"
]


# TR:
# USB kablosu özellikle önemlidir.
#
# EN:
# The USB cable is especially important.
#
# Ne işe yaradığını bilmiyoruz.
#
# We don't know what it does.
#
# Ama çalışıyor.
#
# But it works.
#
# O yüzden SİLMEYİN.
#
# Therefore, DO NOT DELETE IT.
#
# Bu yorum gelecekteki bir geliştiriciyi kurtarabilir.
#
# This comment may save a future developer.


print("\nInventory / Envanter:")
for item in inventory:
    print("-", item)


# ================================================================
#                   SYSTEM DIAGNOSTICS
# ================================================================
#
# TR:
# Şimdi sistemimizi kontrol ediyoruz.
#
# EN:
# Now we are checking our system.
#
# Sistem:
#     Çalışıyor.
#
# Program:
#     Çalışıyor.
#
# Geliştirici:
#     Muhtemelen.
#
# System:
#     Working.
#
# Program:
#     Working.
#
# Developer:
#     Probably.
# ================================================================

print("\nRunning diagnostics... / Sistem kontrol ediliyor...")

checks = {
    "Python": True,
    "Brain": False,
    "Coffee": True,
    "Code": True,
    "Motivation": random.choice([True, False]),
}

for system, status in checks.items():

    if status:
        print(f"[ OK ] {system}")
    else:
        print(f"[??? ] {system}")


# ================================================================
#                    FINAL MESSAGE
# ================================================================
#
# TR:
# Programın sonuna geldik.
#
# Şimdi önemli bir soru:
#
# "Bu program ne yapıyor?"
#
# Cevap:
#
# Bilmiyoruz.
#
# Ama çalışıyor.
#
# EN:
# We have reached the end of the program.
#
# Now an important question:
#
# "What does this program actually do?"
#
# Answer:
#
# We don't know.
#
# But it works.
#
# Ve yazılım dünyasında bazen bu yeterlidir.
#
# And sometimes, in software development, that's enough.
# ================================================================


print("\n========================================")
print(f"Hello, {name}! / Merhaba, {name}!")
print("Program finished successfully.")
print("Program başarıyla tamamlandı.")
print("========================================")


# ================================================================
#                      FINAL NOTES
# ================================================================
#
# TR:
# Eğer buraya kadar geldiyseniz teşekkürler.
#
# Bu program:
#     - Bilgisayarı hacklemedi.
#     - NASA'ya bağlanmadı.
#     - USB kablosunun sırrını çözmedi.
#     - Dünyayı kurtarmadı.
#     - Ama 10 + 20'yi doğru hesapladı.
#
# EN:
# If you made it this far, thank you.
#
# This program:
#     - Did not hack the computer.
#     - Did not connect to NASA.
#     - Did not solve the USB cable mystery.
#     - Did not save the world.
#     - But it correctly calculated 10 + 20.
#
# Başarı oranı:
# 10/10
#
# Success rate:
# 10/10
#
# FIXME:
# Bu oran tamamen uydurulmuştur.
#
# FIXME:
# This rating was completely made up.
#
# Ama README'ye güzel gider.
#
# But it looks good in a README.
#
# ---------------------------------------------------------------
#
# STATUS:
#     [✓] Program works
#     [✓] No serious errors
#     [✓] Excessive comments
#     [✓] Mild programmer confusion
#     [✓] Suspicious USB cable
#
# ---------------------------------------------------------------
#
# End of file.
#
# Dosyanın sonu.
#
# Gerçekten.
#
# Seriously.
#
# ...
#
# Tamam artık.
#
# Okay, seriously now.
#
# ...
#
# FIXME: Why is this comment still going?
#
# FIXME: Bu yorum neden hâlâ devam ediyor?
#
# Çünkü silemedim.
#
# Because I couldn't delete it.
#
# THE END.
#
# SON.
# ================================================================