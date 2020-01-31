#include <stdio.h>

int ten_to_three (int * res,int num)
{
	int i = 0;
	if (num == 0) res[i++] = 0;
	else if (num == 1) res[i++] = 1;
	else if (num == 2) res[i++] = 2;
	else {
		while(num)
		{
			res[i] = num%3;
			num/=3;
			i++;
		}
	}
	return i;
}

int main()
{
	int input;
	int res[80];
	printf("Enter a number: ");
	scanf("%d",&input);
	int len = ten_to_three(res, input);
	for(int i = len - 1; i >= 0; i--) {
		if (res[i] == 0) printf("-");
		if (res[i] == 1) printf("0");
		if (res[i] == 2) printf("+");
	}
	printf("\n");
	return 0;
}

