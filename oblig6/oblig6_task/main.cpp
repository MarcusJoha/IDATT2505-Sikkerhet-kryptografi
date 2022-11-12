#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

#include <openssl/evp.h>

using namespace std;

string hex(const string &input) {

    stringstream hex_stream;
    hex_stream << std::hex << std::internal << setfill('0');
    for (auto &byte : input) {
        hex_stream << setw(2) << (int)(unsigned char)byte;
    }
    return hex_stream.str();
}

string pbkdf2(const string &passwd, const string &salt, int keylen) {
    string hash;
    hash.resize(keylen); // 
    PKCS5_PBKDF2_HMAC_SHA1((const char *)&passwd[0], passwd.size(), (const unsigned char *) &salt[0], salt.size(), 2048, keylen, (unsigned char *)&hash[0]);
    return hash;
}

string rec_crack(const string &hash, const string &salt, int limit, int current_len, string attempt) {
     // Alphabet A-Z and a-z
     for (unsigned char i = 65; i < 123; ++i) {
        attempt[current_len-1] = i;
        if (current_len < limit) {
            string res = rec_crack(hash, salt, limit, current_len+1, attempt);
            if (res != "") return res;
        } else {
            cout << attempt << endl;
            string attempt_hash = hex(pbkdf2(attempt, salt, 20)); 
            if (attempt_hash == hash) return attempt;
        }
     }
     return "";
}

string crack(const string &hash, const string &salt, int limit) {
    string attempt;
    int i;
    for (i = 1; i <= limit; ++i) {
        attempt = "";
        attempt.resize(i);
        string res = rec_crack(hash,salt, i, 1, attempt);
        if (res != "") return res;
    }
    return "";
}

int main() {

    const string salt = "Saltet til Ola";
    const string hash = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6";
    string passwd = crack(hash, salt, 5); // assume password is mac 5 characters long
    cout << "\nPassordet er: " << passwd;

    return 0;
}

