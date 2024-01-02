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

int dfss(int steps, int maxSteps, int curr, int first[], int second[], int n,int furthest){
    if (steps == maxSteps){
        return curr;
    }

    int firstStep = 0;
    if (furthest < n){
        firstStep = dfss(steps+1,maxSteps,curr+first[furthest], first, second, n, furthest+1);
    }

    int secondMax = 0;
    for(int i = 0; i < furthest; i++ ){
        secondMax = max(secondMax, second[i]);
    }

    int secondStep = dfss(steps+1, maxSteps, curr+secondMax, first, second,n, furthest);
    //cout << steps << " " << curr << " " << furthest << " " << max(firstStep, secondStep) << "\n";
    return max(firstStep, secondStep);

}

static void testcase() {
    int n,k; // number of quests, maximum he can complete
    cin >> n >> k; 
    int first[n];
    int second[n];

    //for (int i = 0)
    for( int i = 0; i < n; i++){
        cin >> first[i];
    }
    for( int i = 0; i < n; i++){
        cin >> second[i];
    }

    int total = dfss(0,k,0, first, second, n,0);
    cout << total << "\n";
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