#include <bits/stdc++.h>

using namespace std;

int main()
{
cout<<"Enter number of elements:"<<endl;
    int n;
    cin>>n;
    int a[n];
    cout<<"Enter elements:"<<endl;
    for(int i=0;i<n;i++){
        cin>>a[i];
        
    }
    int min;
    for(int i=0;i<n-1;i++){
        min=i;
        for(int j=i+1;j<n;j++){
            if(a[j]<a[min]){
                min=j;
            }
        }
        swap(a[min],a[i]);
    }
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }

    return 0;
}
