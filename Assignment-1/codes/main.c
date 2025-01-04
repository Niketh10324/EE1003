#include <stdio.h>

void finite_difference(double x0, double y0, double x_end, double h, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }

    double x = x0, y = y0;
    fprintf(file, "# x\t\ty\n");  // Comment header for .dat file

    while (x <= x_end) {
        fprintf(file, "%lf\t%lf\n", x, y);  // Write x and y values to file
        y = y + h * (2 * (y + 3) / (x + 4));  // Update y using finite differences
        x = x + h;                           // Increment x by step size h
    }

    fclose(file);
}

int main() {
    double x0 = -2.0;   // Initial x
    double y0 = 1.0;    // Initial y (y(x0) = y0)
    double x_end = 5.0; // End of x range
    double h = 0.01;    // Step size
    const char *filename = "data.dat";

    finite_difference(x0, y0, x_end, h, filename);
    printf("Data written to %s\n", filename);

    return 0;
}

