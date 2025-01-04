#ifndef FINITE_DIFFERENCE_H
#define FINITE_DIFFERENCE_H

typedef struct {
    double x;
    double y;
} DataPoint;

void finite_difference(double x0, double y0, double x_end, double h);
int get_data_size();
const DataPoint *get_data();
void cleanup();

#endif // FINITE_DIFFERENCE_H

