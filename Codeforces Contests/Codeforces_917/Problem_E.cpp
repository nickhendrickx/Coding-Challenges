#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i, n) for (i = 0; i < n; i++)
#define Fo(i, k, n) for (i = k; k < n ? i < n : i > n; k < n ? i += 1 : i -= 1)
#define ll long long
#define deb(x) cout << #x << "=" << x << endl
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, false, sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it, a) for (auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
#define mod 1000000007
typedef pair<int, int> pii;
typedef pair<ll, ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vpii;
typedef vector<pl> vpl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;

const int nmax = 1e6 + 5;
const int inf = 1e9 + 5;
//int n, k, m, q;
vector<int> g[nmax];
int v[nmax];

static void testcase() {
    int n;
    cin >> n;
    ll first[n];
    ll second[n];

    for(int i = 0; i < n; i++) {
        cin >> first[i];
    } 
    
    for(int i = 0; i < n; i++) {
        cin >> second[i];
    } 
    
    ll max = 0;
    int c = n;
    while(n--){
        ll currMax = 0;
        ll otherMax = 0;
        ll currIndex = 0;
        //Alice step
        ll sum = 0;
        for(int i=0; i < c;i++){
            //cout << "current i " << second[i] << "\n";
            sum = first[i] + second[i];
            if (sum > currMax){
                currMax = sum;
                currIndex = i;
            }
        }
        ll aliceP = first[currIndex];
        ll bobP = second[currIndex];

        max = max + aliceP - 1;
        first[currIndex] = -1;
        second[currIndex] = -1;

        if(n > 0){
            ll currMax = 0;
            ll otherMax = 0;
            ll currIndex;
            //Bob step
            ll sum = 0;
            for(int i=0; i < c;i++){
                //cout << "current i " << second[i] << "\n";
                sum = first[i] + second[i];
                if (sum > currMax){
                    currMax = sum;
                    currIndex = i;
                }
            }
            ll aliceP = first[currIndex];
            ll bobP = second[currIndex];
            max = max - (bobP - 1);
            first[currIndex] = -1;
            second[currIndex] = -1;
            n--;
            }
    }

    cout << max << "\n";

    return;
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        testcase();

    return 0;
}