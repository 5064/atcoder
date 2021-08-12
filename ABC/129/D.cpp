#include <bits/stdc++.h>
using namespace std;

int H, W;
vector<string> fi;
int Left[2100][2100], Right[2100][2100], Up[2100][2100], Down[2100][2100];

int main()
{
    // 入力
    cin >> H >> W;
    fi.resize(H);
    for (int i = 0; i < H; ++i)
        cin >> fi[i];

    // 前処理
    for (int i = 0; i < H; ++i)
    {
        int cur = 0;
        for (int j = 0; j < W; ++j)
        {
            if (fi[i][j] == '#')
                cur = 0;
            else
                ++cur;
            Left[i][j] = cur;
        }
    }
    for (int i = 0; i < H; ++i)
    {
        int cur = 0;
        for (int j = W - 1; j >= 0; --j)
        {
            if (fi[i][j] == '#')
                cur = 0;
            else
                ++cur;
            Right[i][j] = cur;
        }
    }
    for (int j = 0; j < W; ++j)
    {
        int cur = 0;
        for (int i = 0; i < H; ++i)
        {
            if (fi[i][j] == '#')
                cur = 0;
            else
                ++cur;
            Up[i][j] = cur;
        }
    }
    for (int j = 0; j < W; ++j)
    {
        int cur = 0;
        for (int i = H - 1; i >= 0; --i)
        {
            if (fi[i][j] == '#')
                cur = 0;
            else
                ++cur;
            Down[i][j] = cur;
        }
    }

    // 集計
    int res = 0;
    for (int i = 0; i < H; ++i)
    {
        for (int j = 0; j < W; ++j)
        {
            if (fi[i][j] == '#')
                continue;
            res = max(res, Left[i][j] + Right[i][j] + Up[i][j] + Down[i][j] - 3);
        }
    }
    cout << res << endl;
}