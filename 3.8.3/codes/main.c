#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to simulate three coin tosses and compute probabilities
void simulate_three_coin_toss(int n, double *probabilities, double *cdf) {
    int outcomes[4] = {0}; // Counts for 0, 1, 2, 3 heads

    // Simulate the trials
    for (int i = 0; i < n; i++) {
        int head_count = 0;
        for (int toss = 0; toss < 3; toss++) {
            if (rand() % 2 == 1) { // Random 0 or 1; 1 represents head
                head_count++;
            }
        }
        outcomes[head_count]++;
    }

    // Calculate probabilities
    for (int i = 0; i < 4; i++) {
        probabilities[i] = (double)outcomes[i] / n;
    }

    // Calculate CDF
    cdf[0] = probabilities[0];
    for (int i = 1; i < 4; i++) {
        cdf[i] = cdf[i - 1] + probabilities[i];
    }
}

// Function exposed for external use (e.g., Python interface)
__attribute__((visibility("default"))) __attribute__((used))
void calculate_probabilities(int n, double *probabilities, double *cdf, double *prob_at_least_2_heads) {
    srand(time(NULL)); // Seed the random number generator
    simulate_three_coin_toss(n, probabilities, cdf);
    
    // Calculate probability of getting at least 2 heads
    *prob_at_least_2_heads = probabilities[2] + probabilities[3];
}

// Test function
int main() {
    int n = 100000; // Number of trials
    double probabilities[4], cdf[4], prob_at_least_2_heads;

    calculate_probabilities(n, probabilities, cdf, &prob_at_least_2_heads);

    // Print results
    printf("Probability Distribution:\n");
    for (int i = 0; i < 4; i++) {
        printf("P(%d heads) = %.5f\n", i, probabilities[i]);
    }
    
    printf("\nCumulative Distribution Function (CDF):\n");
    for (int i = 0; i < 4; i++) {
        printf("F(%d heads) = %.5f\n", i, cdf[i]);
    }

    printf("\nProbability of getting at least 2 heads: %.5f\n", prob_at_least_2_heads);

    return 0;
}

