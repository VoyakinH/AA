#include <vector>
#include <string>

using namespace std;

static vector<int> ComputePrefixFunction(string P) {
	size_t len = P.length();
	vector<int> s;
	for (int i = 0; i < len; i++) s.push_back(0);
	int border = 0;
	for (int i = 1; i < len; i++) {
		while ((border > 0) && (P[i] != P[border])) {
			int index = border - 1;
			border = s[index];
		}
		if (P[i] == P[border]) border = border + 1;
			else border = 0;
		s[i] = border;
	}
	return s;
}

static vector<int> FindAllOccurrences(string P, string T) {
	string S = P + '#' + T;
	vector<int> s = ComputePrefixFunction(S);
	vector<int> result;
	int len_pattern = P.length();
	for (int i = (len_pattern + 1); i < S.length(); i++) {
		if (s[i] == len_pattern) {
			int find = 1 + i - 2 * len_pattern;
			result.push_back(find);
		}	
	}
	return result;
}

void KMP(string Pattern, string Text, string &result) {
	vector<int> res = FindAllOccurrences(Pattern, Text);
	int len = Pattern.length();
	for (int i = 0; i < res.size(); i++) {
		int start = res[i];
		int end = start + len - 1;
		string buffer = "   " + to_string(start) + "-" + to_string(end);
		result += buffer;
	}
} 
