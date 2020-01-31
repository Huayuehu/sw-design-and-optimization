// 还不确定生成的随机数是不是uniformed

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

double Uniform(double min, double max, long int *seed);
double UniformRand(double min, double max);

int main(int argc, char* argv[])
{
	double z, zd, dz, e;

	double x = atof(argv[1]);
	double y = atof(argv[2]);
	double d = atof(argv[3]);

	z = pow(x,2) + pow(y,2);
	// printf("z: %.3f\n", z);

	// generate uniform random number e between [1, d*z]
	dz = d * z;
	// printf("dz: %.3f\n", dz);
	e = UniformRand(1, dz);
	// printf("e: %.3f\n", e);

	// final result
	zd = z + e;
	printf("%.3f", zd);

}

/*
* To uniform the number generated
*/
double Uniform(double min, double max, long int *seed) {
    double e = 0;
    *seed = 2045 * (*seed) + 1;
    *seed = *seed - (*seed / 1048576) * 1048576;
    e = (*seed) / 1048576.0;
    e = min + (max - min) * e;
    return e;
}

/*
* To generate random number
*/
double UniformRand(double min, double max) {
    long int s = 0;
    double r = 0;

    srand((unsigned int)time(NULL));
	s = rand();
    // printf("s: %ld\n", s);
    r = Uniform(min, max, &s);

    return (r);
}