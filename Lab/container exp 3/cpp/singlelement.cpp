//we have to find the single element that is not repeating in an array 
//bruteforce approach
//have to do optimal approach also 
#include<iostream>
using namespace std;
int singleelement(vector<int> &arr)
{
  int n=<arr.size();
  int num;
  for(int i=0; i<n; i++)
  {
    num=arr[i];
    int count=0;
    for(j=0; j<n; j++)
    {
      if(arr[j]==num)
      count++;
    }
    if(count==1)
    return num;
  }
  return -1;
}

int main()
{
    vector<int> arr={4,1,2,1,2};
    int ans =singleelement(arr);
    cout<<"the single element is"<<ans<<endl;
    return 0;

}