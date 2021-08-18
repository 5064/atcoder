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
    int W, N, K;
    cin >> W >> N >> K;

    vector<int> A(N);
    vector<int> B(N);
    vector<vector<vector<int>>> dp(N + 10, vector<vector<int>>(W + 10, vector<int>(K + 10)));
    rep(i, N + 10) rep(j, W + 10) rep(l, K + 10) dp[i][j][l] = (-1 * INF);
    dp[0][0][0] = 0;

    rep(i, N) cin >> A[i] >> B[i];

    rep(i, N + 1)
    {
        rep(sum_w, W)
        {
            rep(sum_k, K)
            {
                if (sum_w - A[i] >= 0)
                {
                    chmax(dp[i + 1][sum_w + A[i]][sum_k + 1], dp[i][sum_w][sum_k] + B[i]);
                }
                chmax(dp[i + 1][sum_w][sum_k], dp[i][sum_w][sum_k]);
            }
        }
    }

    // 必ずしもWとKを使い切らなくても価値を出せるので、探索する必要がある
    int best = 0;
    rep(i, W)
    {
        rep(j, K)
        {
            chmax(best, dp[N][i][j]);
        }
    }
    cout << best << endl;
}
