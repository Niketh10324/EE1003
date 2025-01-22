#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate PMF using Z-transform
void calculate_pmf_z_transform(double *pmf) {
    int n = 3; // Number of tosses
    double p = 0.5; // Probability of heads for a fair coin

    // Compute coefficients of Z-transform: (p + (1-p)z)^n
    // Z-transform expansion: (p + qz)^n = \sum_{k=0}^{n} C(n, k) * p^(n-k) * q^k * z^k
    // PMF corresponds to the coefficients of z^k

    for (int k = 0; k <= n; k++) {
        // Calculate binomial coefficient C(n, k)
        double binomial_coefficient = 1;
        for (int i = 0; i < k; i++) {
            binomial_coefficient *= (n - i) / (double)(i + 1);
        }

        // Compute PMF value for k heads using Z-transform
        pmf[k] = binomial_coefficient * pow(p, k) * pow(1 - p, n - k);
    }
}

// Function to calculate the probability of getting at least 2 heads
double probability_at_least_two_heads() {
    int n = 3; // Number of tosses
    double pmf[n + 1];

    // Calculate PMF using Z-transform
    calculate_pmf_z_transform(pmf);

    // Sum probabilities for k >= 2 (2 or 3 heads)
    double probability = pmf[2] + pmf[3];
    return probability;
}

// Main function
int main() {
    double result = probability_at_least_two_heads();
    printf("Probability of getting at least two heads: %.6f\n", result);
    return 0;
}

