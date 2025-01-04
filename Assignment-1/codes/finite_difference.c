#include <stdio.h>
#include <stdlib.h>

// Define a structure to hold the x and y values
typedef struct {
    double x;
    double y;
} DataPoint;

// Global variables to store data
DataPoint *data = NULL;
int data_size = 0;

// Function to compute finite differences and store results
void finite_difference(double x0, double y0, double x_end, double h) {
    int capacity = 100;  // Initial capacity
    data = malloc(capacity * sizeof(DataPoint));
    if (data == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    double x = x0, y = y0;
    data_size = 0;

    while (x <= x_end) {
        if (data_size >= capacity) {
            capacity *= 2;
            data = realloc(data, capacity * sizeof(DataPoint));
            if (data == NULL) {
                printf("Memory reallocation failed!\n");
                return;
            }
        }
        data[data_size].x = x;
        data[data_size].y = y;
        data_size++;

        y += h * (2 * (y + 3) / (x + 4));  // Update y using finite differences
        x += h;                           // Increment x by step size h
    }
}

// Function to get the size of the stored data
int get_data_size() {
    return data_size;
}

// Function to get the data array
const DataPoint *get_data() {
    return data;
}

// Cleanup function to free allocated memory
void cleanup() {
    if (data != NULL) {
        free(data);
        data = NULL;
    }
    data_size = 0;
}

