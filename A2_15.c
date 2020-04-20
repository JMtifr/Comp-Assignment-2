#include <stdio.h>
#include <math.h>
float f(float x, float y) // y'
{return y-pow(x,2)+1.0;}
float ex(float x) // exact solution
{return pow((x+1.0),2)-0.5*exp(x) ;
}
float eb(float x) // y" 
{return 2.0*(x+1.0)-0.5*exp(x);}
int main(void)
{ 
	
	int  i;
	float  h,t;
	float  x[11],y_numerical[11],y_exact[11],error_bound[11],error[11];
	h=0.2;
	i=1;
	error_bound[0]=0.0; error[0]=0.0;
	x[0]=0.0;y_numerical[0]=0.5;y_exact[0]=0.5; // initial values
	for (t=0.2;t<=2.1;t=t+h) // loop to calculate numeric and exact solutions
    {
		x[i]=t;
		y_numerical[i]=y_numerical[i-1]+h*f(x[i-1],y_numerical[i-1]);
		y_exact[i]=ex(t);
		error_bound[i]=error_bound[i-1]+h*h*fabs(eb(x[i]))/2.0; // error bound = previous+h^2*y"/2
		error[i]=fabs(y_exact[i]-y_numerical[i]);
		i=i+1;};
		
		printf("   x     y_numerical   y_exact   abs error   error bound \n");
		printf("\n");
		for(i=0;i<11;i++)
		{
		printf("%f   %f   %f   %f     %f\n",x[i],y_numerical[i],y_exact[i],error[i],error_bound[i]);
		}
		return 0;
	}
		
