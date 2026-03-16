//Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
#include<iostream>
using namespace std;
int linearsearch(int arr[],int n,int keyval){
    for(int i=0; i<n; i++){
        if(arr[i]==keyval){
            return i;
        }
        return -1;
    }
}
  int main(){
    int arr[]={4,5,6,7,8};
    int keyval=6;
    int n=sizeof(arr)/sizeof(arr[0]);
    int value=linearsearch(arr,n,keyval);
    cout<<value;

}