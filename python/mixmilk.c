/*
ID: happyn61
TASK: mixmilk
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("mixmilk.out");
    ifstream fin ("mixmilk.in");
    int a, aa,b,bb,c,cc;
    fin >> aa >> a;
    fin >> bb >> b;
    fin >> cc >> c;
    for(int i=0;i<100;i++){
        if (i%3==0)
        {
            if (b+a<=bb){
                 b=b+a;
                 a=0;
             }
             else{
                 a=a+b-bb;
                 b=bb;
             }
        }
        if (i%3==1)
        {
            if (c+b<=cc){
                 c=b+c;
                 b=0;
             }
             else{
                 b=c+b-cc;
                 c=cc;
             }
        }
        if (i%3==2)
        {
            if (c+a<=aa){
                 a=c+a;
                 c=0;
             }
             else{
                 c=a+c-aa;
                 a=aa;
             }
        }
        cout << a <<" "<<b<<" " <<c<<endl;
    }
    fout << a <<endl<<b<<endl <<c<<endl;
    return 0;
}
