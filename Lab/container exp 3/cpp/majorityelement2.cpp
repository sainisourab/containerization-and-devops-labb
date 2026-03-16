//it is by using moore algorithm 
#include<iostream>
using namespace std;
int majorityelement(vector<int> v){
    int n=v.size();
    int el;
    int count=0;
    for(int i=0; i<n; i++){
        if(count==0){
            count=1;
            el=v[i];
        }
        else if(el==v[i])
        count++;
        else count--;
    }

    int count2=0;
    for(int i=0; i<n; i++){
        if(v[i]==el)
        count2++;
    }
    if(count2>(n/2))
    return el; 
}
int main()
{
    vector<int> arr={2,2,1,1,1,2,2};
    int ans=majorityelement(arr);
    cout<<"the majority element in the array is"<<ans<<endl;

}
