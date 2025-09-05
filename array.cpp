#include <iostream>

using namespace std;

int main(){

int a;

 cout<<"How many numbers you want to add :";

 cin>>a;

int arr [a];

for(int i=0;i<a;i++){

cout<<"Enter number "<<i+1<<" : ";
 cin>> arr[i];
}
for(int i=0;i<a;i++){


cout<<arr[i]<<" ";
}

  

}