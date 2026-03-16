//here we will find missing element in an array 
int misssingelement(int n, int arr[]){
    for(int i=1;i<=n;i++)
    int key=0;

    {
        for(int j=0; j<n; j++)
        {
            if(arr[j]==i)
            {
                key=1;
                break;
            }
        }
        if (key==0)
        return i;
        
    }

}