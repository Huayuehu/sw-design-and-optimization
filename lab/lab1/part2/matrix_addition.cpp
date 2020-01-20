# include <iostream>
# include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
   ifstream filea("a.txt");
   ifstream fileb("b.txt");
   ofstream outfile("result.txt");
   
   if(!(filea) || !(fileb)) {
      cout<<"Unable to open input files";
   }
   if(!outfile) {
      cout<<"Unable to open output result file";
   }
   
   // creat arrays to store result
   int row = 5, col = 5;
   int **res;
   res = new int*[row];
   for (int i = 0; i < row; i++) 
   {
      res[i] = new int[col];
   }
   
   // compute the result and store into res
   for (int i = 0; i < row; i++)
   {
      for (int j = 0; j < col; j++)
      {
         int a, b;
         filea>>a;
         fileb>>b;
         res[i][j] = a + b;
      }
   }
   filea.close();
   fileb.close();
   
   // cout the result
   for (int i = 0; i < row; i++)
   {
      for (int j = 0; j < col; j++)
      {
         cout<<res[i][j]<<" ";
      }
      cout<<endl;
   }
   
   // output the result
   for (int i = 0; i < row; i++)
   {
      for (int j = 0; j < col; j++)
      {
         outfile<<res[i][j]<<" ";
      }
      outfile<<endl;
   }
   
   // release array res
   for (int i = 0; i < row; i++) 
   {
      delete[] res[i];
   }
   delete[] res;
   
}
