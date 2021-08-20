// RE,TLE
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int INF = 1e9;
const int MOD = 1e9 + 7;

#define overload4(_1, _2, _3, _4, name, ...) name
#define rep1(n) for (ll i = 0; i < (n); ++i)
#define rep2(i, n) for (ll i = 0; i < (n); ++i)
#define rep3(i, a, b) for (ll i = (a); i < (b); ++i)
#define rep4(i, a, b, c) for (ll i = (a); i < (b); i += (c))
#define rep(...) overload4(__VA_ARGS__, rep4, rep3, rep2, rep1)(__VA_ARGS__)
#define rrep1(n) for (ll i = (n); i--;)
#define rrep2(i, n) for (ll i = (n); i--;)
#define rrep3(i, a, b) for (ll i = (b); i-- > (a);)
#define rrep4(i, a, b, c) for (ll i = (a) + ((b) - (a)-1) / (c) * (c); i >= (a); i -= c)
#define rrep(...) overload4(__VA_ARGS__, rrep4, rrep3, rrep2, rrep1)(__VA_ARGS__)
//x:コンテナ
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())

// aよりもbが大きいならばaをbで更新する
// (更新されたならばtrueを返す)
template <typename T>
bool chmax(T &a, const T &b)
{
    if (a < b)
    {
        a = b; // aをbで更新
        return true;
    }
    return false;
}
// aよりもbが小さいならばaをbで更新する
// (更新されたならばtrueを返す)
template <typename T>
bool chmin(T &a, const T &b)
{
    if (a > b)
    {
        a = b; // aをbで更新
        return true;
    }
    return false;
}

//---------------------------------------

vector<priority_queue<ll, vector<ll>, greater<ll>>> pq(2 * 10001);
vector<ll> addition(20002);

int main()
{
    rep(i, 20002) addition[i] = 0;
    int Q = 0;
    cin >> Q;
    int query;
    int current = 0;
    ll min_i = 0, min_top = 0;
    ll X;

    vector<ll> ans;

    rep(i, Q)
    {
        cin >> query;
        if (query == 1)
        {
            cin >> X;
            pq[current].push(X);
        }
        else if (query == 2)
        {
            cin >> X;
            current++;
            rep(i, current)
            {
                addition[i] += X;
            }
        }
        else //3
        {
            min_i = 0, min_top = (1LL << 50);
            rep(j, current + 1)
            {
                ll top = 0;
                if (!pq[j].empty())
                {
                    top = pq[j].top() + addition[j];
                    if (top < min_top)
                    {
                        min_i = j;
                        min_top = top;
                    }
                }
            }
            ans.push_back(min_top);
            pq[min_i].pop();
        }
    }
    rep(an, sz(ans))
    {
        cout << ans[an] << endl;
    }
}
