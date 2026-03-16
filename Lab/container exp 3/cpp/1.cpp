#include<iostream>
using namespace std;

//largest element in an array 
int largestelement(int arr[],int n){
    int largest =arr[0];
    for (int i=0; i<n; i++)
    {
        if(arr[i]>largest){
            largest=arr[i];
        }
    }
    return largest;
}

int main(){
    int n;
    cout<<"enter size of array";
}