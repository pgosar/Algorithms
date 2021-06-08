#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
using namespace std;
int main() {

    unordered_map<string, int> ourmap;
    //insert
    pair<string, int> p ("abc",1);
    ourmap.insert(p);
    ourmap["def"]=2;
    //find or accessmv
    cout << ourmap["abc"] << endl;
    cout << ourmap.at("abc") << endl;
    //cout <<ourmapat("ghi") << endl; this line returns an error because ghi is not present in the map
    cout << ourmap["ghi"] << endl; //this line does not return an error because since ghi is not present in maps it to a default value of zero and then returns it
    //size
    cout << ourmap.size() << endl;
    //check presence
    if(ourmap.count("ghi")>0)cout <<"present"<<endl;
    cout << ourmap.count("ghi") <<endl;
    //erase
    ourmap.erase("ghi");
    
    cout << ourmap.size() << endl;
    if(ourmap.count("ghi")>0)cout <<"present"<<endl;
    cout << ourmap.count("ghi") <<endl;
    // int n; cin>>n;
    // vector<int>A(n+5,0);
    // long long S=0;
    // for(auto i=0;i<n;i++)cin>>A[i], S+=A[i];
    // if(S&1)printf("NO\n");
    // map<long long,int> first,second;
    // first[A[0]]=1;
    // for(int i=1;i<n;i++)second[A[i]]++;
    // long long sdash=0;
    // for(int i=0;i<n;i++){
    //     sdash+=A[i];
    //     if(sdash==S/2){
    //         printf("YES\n");
    //         return 0;}
    //     if(sdash<S/2) {
    //         long long x=S/2-sdash;
    //         if(second[x]>0){
    //             printf("YES\n");
    //             return 0;}}
    //     else{
    //         long long y=sdash-S/2;
    //         if(first[y]>0){
    //             printf("YES\n");
    //             return 0;}}
    //     first[A][i+1]]++;
    //     second[A[i+1]];}}
    return 0;
}