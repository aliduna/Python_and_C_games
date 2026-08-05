#include <stdio.h>

int main() {
    float weight, height, bmi;

    printf("=========================================\n");
    printf("      BMI (Body Mass Index) Calculator\n");
    printf("=========================================\n\n");

    printf("Enter your weight (kg): ");
    scanf("%f", &weight);

    printf("Enter your height (meters): ");
    scanf("%f", &height);

    if (height <= 0 || weight <= 0) {
        printf("\nInvalid values entered!\n");
        return 1;
    }

    bmi = weight / (height * height);

    printf("\n-----------------------------------------\n");
    printf("Your BMI: %.2f\n", bmi);

    if (bmi < 18.5)
        printf("Category: Underweight\n");
    else if (bmi < 25)
        printf("Category: Normal Weight\n");
    else if (bmi < 30)
        printf("Category: Overweight\n");
    else if (bmi < 35)
        printf("Category: Obesity Class I\n");
    else if (bmi < 40)
        printf("Category: Obesity Class II\n");
    else
        printf("Category: Obesity Class III\n");

    printf("-----------------------------------------\n");

    return 0;
}