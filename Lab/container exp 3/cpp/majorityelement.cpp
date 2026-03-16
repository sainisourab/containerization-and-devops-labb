#include<iostream>
using namespace std;

int majorityelement(vector<int> v){

    int n=arr.size();
    for(int i=0; i<n; i++){
        int count=0;
        for(int j=0;j<n;j++){
            if(v[j]==v[i]){
                count++
            }
        }
        if(count>(n/2))
        return v[i];
    }
    return -1;
}



int main(){
    vector<int> arr={2,2,1,1,1,2,2};
    int ans=majorityelement(arr);
    cout<<"the majority element is"<<ans<<endl;
    return 0;
}