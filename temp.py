#include <bits/stdc++.h>
#define pb push_back
using namespace std;

const int maxn = 1e5 + 5;

int n,res;int col[maxn],spl[maxn];
vector<int> adj[maxn];

void dfs(int u,int c){
        if(col[u]==c){
                if(!spl[u])res++;
                spl[u] = 1;
        }
        for(int v:adj[u]) dfs(v,c);
}
int main() {
   ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;

    int a,b;
    cin>>a>>b;

    if(a==1) adj[a].pb(b);
    else adj[b].pb(a);

        for(int i=2;i<n;i++){
                cin>>a>>b;
                adj[a].pb(b);
        }

        for(int i=1;i<=n;i++){
                cin>>col[i];
        }

        int q;
        cin>>q;
        
        while(q--){
                int x;
                cin>>x;
                if(!spl[x]){
                        dfs(x,col[x]);
                }
                cout<<res<<endl;
        }

        return 0;
}