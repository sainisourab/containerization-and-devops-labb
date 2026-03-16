//in this we have to remove duplictes in a sorted array 
#include<iostream>
using namespace std;

int removeduplicates(vector<int> &arr, int n){
    int i=0;
    for(j=1; j<n; j++){
        if(arr[i]!=arr[j]){
            arr[i+1]=arr[j];
            i++;
        }
    }
    return i+1;
}

int main(){
    int n;
}