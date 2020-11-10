#include <stdio.h>
#include <math.h>
#include <iostream>
#include <limits>


int main() {

    int a;
    a = 111111111 * 111111111;
    printf("%d\n", a);

    float fa;
    fa = 111111111.0 * 111111111.0;
    printf("%f\n", fa);

    double c = 111111111.0 * 111111111.0;
    printf("%f\n", c);

    long long int cc = 111111111 * 111111111;
    printf("%lld\n", cc);

    long int x = 111111111;
    long int ccc = x * x;
    printf("ccc: %ld\n", ccc);

    int d = sqrt(-10);
    printf("%d\n", d);

    float e = sqrt(-1);
    printf("%f\n", e);

    std::cout << std::numeric_limits<long long int>::max() << std::endl;
    std::cout << std::numeric_limits<unsigned long long int>::max() << std::endl;

    return 0;
}
