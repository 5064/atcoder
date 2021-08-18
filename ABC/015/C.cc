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

int main()
{
    int N, K, cint;
    cin >> N >> K;

    vector<vector<int>> T(N + 1, vector<int>(K));
    vector<vector<int>> memo(N + 1, vector<int>(0));
    rep(i, N)
    {
        rep(j, K)
        {
            cin >> cint;
            T[i][j] = cint;
        }
    }
    string ans = "Nothing";
    rep(n, N)
    {
        vector<int> acc;
        if (n == 0)
        {
            acc = T[0];
        }
        else
        {
            acc = memo[n];
        }

        for (int t : acc)
        {
            for (int t2 : T[n + 1])
            {
                int xort = (t ^ t2);
                if (xort == 0)
                {
                    ans = "Found";
                    break;
                }
                else
                {
                    memo[n + 1].push_back(xort);
                }
            }
            if (ans == "Found") // 大域脱出
                break;
        }
        if (ans == "Found") // 大域脱出
            break;
    }

    cout << ans << endl;
}
