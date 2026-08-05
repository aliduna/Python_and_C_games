#include <stdio.h>

int main() {
    float kilo, boy, vki;

    printf("=========================================\n");
    printf("      VKI (Vucut Kitle Indeksi)\n");
    printf("=========================================\n\n");

    printf("Kilonuzu giriniz (kg): ");
    scanf("%f", &kilo);

    printf("Boyunuzu giriniz (metre): ");
    scanf("%f", &boy);

    if (boy <= 0 || kilo <= 0) {
        printf("\nGecersiz deger girdiniz!\n");
        return 1;
    }

    vki = kilo / (boy * boy);

    printf("\n-----------------------------------------\n");
    printf("VKI Degeriniz: %.2f\n", vki);

    if (vki < 18.5)
        printf("Kategori: Zayif\n");
    else if (vki < 25)
        printf("Kategori: Normal Kilolu\n");
    else if (vki < 30)
        printf("Kategori: Fazla Kilolu\n");
    else if (vki < 35)
        printf("Kategori: Obezite Sinif I\n");
    else if (vki < 40)
        printf("Kategori: Obezite Sinif II\n");
    else
        printf("Kategori: Obezite Sinif III\n");

    printf("-----------------------------------------\n");

    return 0;
}