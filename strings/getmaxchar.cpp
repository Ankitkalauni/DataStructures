#include <iostream>
#include <vector>
using namespace std;

char getmax(string s) {
	int arr[26] = {0};

	for (int i = 0; i < s.length(); i++) {
		char j = s[i];

		int number = 0;
		if (j >= 'a' && j <= 'z') {
			number = j - 'a';
		} else {
			number = j - 'A';
		}

		arr[number]++;
	}
	int maxi = -1, ans = 0;
	for (int i = 0; i < 26; i++) {
		if (maxi < arr[i]) {
			ans = i;
			maxi = arr[i];
		}
	}
	char finalans = 'a' + ans;
	return finalans;
}

int main() {
	string s;
	cin >> s;

	cout << getmax(s);

	return 0;
}
