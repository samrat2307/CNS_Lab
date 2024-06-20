#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main()
{
    string plainText, key;

    cout << "\n Choose an option:\n";
    cout << "  1. Encryption\n";
    cout << "  2. Decryption\n";
    int choice;
    cin >> choice;
    cin.ignore();

    if (choice == 1)
    {
        // Encryption
        cout << "\n Enter plain text : ";
        getline(cin, plainText);

        cout << "\n Enter key : ";
        getline(cin, key);

        // Removing spaces and converting to lowercase from plaintext
        string temp = "";
        for (int i = 0; i < plainText.size(); i++)
        {
            if (plainText[i] != ' ')
                temp += tolower(plainText[i]);
        }
        plainText = temp;

        // Removing spaces and converting to lowercase from key
        string temp2 = "";
        for (int i = 0; i < key.size(); i++)
        {
            if (key[i] != ' ')
                temp2 += tolower(key[i]);
        }
        key = temp2;

        // Encryption
        map<char, vector<char>> mp;
        int keyCounter = 0;

        for (int i = 0; i < plainText.size(); i++)
        {
            mp[key[keyCounter++]].push_back(plainText[i]);

            if (keyCounter == key.size())
                keyCounter = 0;
        }

        // Print the key letters at the top
        for (const auto &it : mp)
        {
            cout << it.first << "\t";
        }
        cout << endl;
        cout<<endl;

        int maxColumnSize = 0;
        for (const auto &it : mp)
        {
            maxColumnSize = max(maxColumnSize, static_cast<int>(it.second.size()));
        }

        for (int i = 0; i < maxColumnSize; i++)
        {
            for (const auto &it : mp)
            {
                if (i < it.second.size())
                {
                    cout << it.second[i] << "\t";
                }
                else
                {
                    cout << " \t"; // Fill with spaces if there's no value in this column
                }
            }
            cout << endl;
        }
        cout << "\nCipher text is: ";
        string cipherText;
        for (const auto &it : mp)
        {
            for (char c : it.second)
            {
                cipherText += c;
            }
        }
        cout << cipherText << endl;
    }
    else if (choice == 2)
    {
        // Decryption
        cout << "\n Enter cipher text : ";
        getline(cin, plainText);

        cout << "\n Enter key : ";
        getline(cin, key);

        // Removing spaces and converting to lowercase from key
        string temp2 = "";
        for (int i = 0; i < key.size(); i++)
        {
            if (key[i] != ' ')
                temp2 += tolower(key[i]);
        }
        key = temp2;

        // Decryption
        map<int, int> dmp;

        int common = plainText.size() / key.size();
        int extra = plainText.size() % key.size();

        for (int i = 0; i < key.size(); i++)
        {
            if (i < extra)
                dmp[i] = common + 1;
            else
                dmp[i] = common;
        }

        map<int, vector<char>> dmp2;

        int start = 0;

        string sortedKey = key;
        sort(sortedKey.begin(), sortedKey.end());

        for (int i = 0; i < sortedKey.size(); i++)
        {
            for (int j = 0; j < key.size(); j++)
            {
                if (sortedKey[i] == key[j])
                {
                    for (int k = 0; k < dmp[j]; k++)
                    {
                        dmp2[key[j]].push_back(plainText[start++]);
                    }
                }
            }
        }

        string afterDecryption;

        vector<int> counters(key.size(), 0);

        int i = 0;

        while (afterDecryption.size() < plainText.size())
        {
            for (int i = 0; i < key.size(); i++)
            {
                if (counters[i] < dmp[i])
                    afterDecryption += dmp2[key[i]][counters[i]++];
            }
        }

        cout << "\n\n Text after decryption is : " << afterDecryption << endl;
    }
    else
    {
        cout << "\n Invalid choice" << endl;
    }

    return 0;
}
