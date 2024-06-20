// playfair
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cout << "\nEnter plain text" << endl;
    getline(cin, s);
    string st;
    for (int i = 0; i < s.length(); i++)
        if (s[i] != ' ')
            st += s[i];
    s = st;
    string k;
    cout << "\nEnter key" << endl;
    cin >> k;

    char mat[5][5];
    int row = 0, col = 0;
    map<char, int> m;
    for (int i = 0; i < k.size(); i++)
    {
        if (m.find(k[i]) != m.end() || k[i] == 'j')
            continue;
        mat[row][col] = k[i];
        m[k[i]] = 1;
        col++;
        if (col == 5)
        {
            col = 0;
            row++;
        }
    }
    for (int i = 0; i < 26; i++)
    {
        char ch = 'a' + i;
        if (ch == 'j')
            continue;
        if (m.find(ch) != m.end())
            continue;
        m[ch] = 1;
        mat[row][col] = ch;
        col++;
        if (col == 5)
        {
            col = 0;
            row++;
        }
    }
    map<char, pair<int, int>> loc;
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << mat[i][j] << " ";
            loc[mat[i][j]] = {i, j};
        }
        cout << endl;
    }
    st = "";
    string pos = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (i == (s.length() - 1))
        {
            st += s[i];
            // Check if the current character and next character are the same
            if (s[i] == s[0])
            {
                pos += '*';
                st += 'x';
                pos += '#';
            }
            else
            {
                pos += '*';
                st += 'x';
                pos += '*';
            }
        }
        else
        {
            st += s[i];
            pos += '*';
            // Check if the current character and next character are the same
            if (s[i] == s[i + 1])
            {
                st += 'x';
                pos += '#';
            }
            else
            {
                st += s[i + 1];
                i++;
                pos += '*';
            }
        }
    }

    s = st;
    cout << "\nPlain text is: " << s << endl;
    cout << "\nKey is: " << k << endl;
    // Print plaintext in groups of two
    for (int i = 0; i < s.length(); i += 2)
    {
        cout << s[i] << s[i + 1] << " ";
    }
    cout << endl;
    for (int i = 0; i < pos.length(); i += 2)
    {
        cout << pos[i] << pos[i + 1] << " ";
    }
    for (int i = 0; i < s.length(); i += 2)
    {
        char ft = s[i];           // Current character
        int ftR = loc[ft].first;  // Row of the current character in the matrix
        int ftC = loc[ft].second; // Column of the current character in the matrix
        char sd = s[i + 1];       // Next character
        int sdR = loc[sd].first;  // Row of the next character in the matrix
        int sdC = loc[sd].second; // Column of the next character in the matrix

        // Check if both characters are in the same row
        if (ftR == sdR)
        {
            s[i] = (mat[ftR][(ftC + 1) % 5]);     // Replace the current character with the character to its right
            s[i + 1] = (mat[ftR][(sdC + 1) % 5]); // Replace the next character with the character to its right
            continue;
        }
        // Check if both characters are in the same column
        if (ftC == sdC)
        {
            s[i] = (mat[(ftR + 1) % 5][ftC]);     // Replace the current character with the character below it
            s[i + 1] = (mat[(sdR + 1) % 5][sdC]); // Replace the next character with the character below it
            continue;
        }

        // Characters are in different rows and columns
        s[i] = mat[ftR][sdC];     // Replace the current character with the character in the same row and column as the next character
        s[i + 1] = mat[sdR][ftC]; // Replace the next character with the character in the same row and column as the current character
    }

    string cip = s;
    transform(cip.begin(), cip.end(), cip.begin(), ::toupper);
    cout << "\nCipher testt is: " << cip;
    for (int i = 0; i < s.length(); i += 2)
    {
        char ft = s[i];
        int ftR = loc[ft].first;
        int ftC = loc[ft].second;
        char sd = s[i + 1];
        int sdR = loc[sd].first;
        int sdC = loc[sd].second;
        if (ftR == sdR)
        {
            s[i] = (mat[ftR][(ftC - 1 + 5) % 5]);
            s[i + 1] = (mat[ftR][(sdC - 1 + 5) % 5]);
            continue;
        }
        if (ftC == sdC)
        {
            s[i] = (mat[(ftR - 1 + 5) % 5][ftC]);
            s[i + 1] = (mat[(sdR - 1 + 5) % 5][sdC]);
            continue;
        }
        s[i] = mat[ftR][sdC];
        s[i + 1] = mat[sdR][ftC];
    }
    string ans = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (pos[i] == '*')
            ans += s[i];
    }
    s = ans;
    cout << "\n\nPlain text after decription is: " << s;

    return 0;
}