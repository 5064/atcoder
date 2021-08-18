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

    int a, b;
    cin >> a >> b;
    vector<int> A(a);
    vector<int> B(b);
    rep(i, a)
    {
        cin >> A[i];
    }
    rep(i, b)
    {
        cin >> B[i];
    }

    vector<vector<int>> dp(a + 1, vector<int>(b + 1)); // dp[i][j] = Aからi個、Bからj個取った状態から最後までの先攻の最適スコア
    dp[a][b] = 0;
    rrep(i, a + 1)
    {
        rrep(j, b + 1)
        {
            if (i == a && j == b)
                continue;

            if ((i + j) % 2 == 0) // 先行番
            {
                if (i == a)
                {
                    // Aの山が空
                    dp[i][j] = B[j] + dp[i][j + 1];
                }
                else if (j == b)
                {
                    // Bの山が空
                    dp[i][j] = A[i] + dp[i + 1][j];
                }
                else
                {
                    // 先攻は先攻スコアを最大化
                    dp[i][j] = max(A[i] + dp[i + 1][j], B[j] + dp[i][j + 1]);
                }
            }
            else // 後攻番
            {
                if (i == a)
                {
                    // Aの山が空->Bから取る
                    dp[i][j] = dp[i][j + 1];
                }
                else if (j == b)
                {
                    // Bの山が空->Aから取る
                    dp[i][j] = dp[i + 1][j];
                }
                else
                {
                    // 後攻は先攻スコアを最小化
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
    }
    cout << dp[0][0] << endl;
}