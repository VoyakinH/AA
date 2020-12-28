// main.cpp

#include <fstream>
#include <iostream>
#include <chrono>
#include <omp.h>
#include "KMP.h"

using namespace std;

static vector<string> parcerFileInput(string nameOfInputFile, int flag) {
	vector<string> result;
	ifstream inputFile(nameOfInputFile);
	if (!inputFile) printf("\n\tERROR: InputFile not exist\n");
	while (inputFile) {
		string line = "";
		getline(inputFile, line);
		if ((flag == 0) && (line == "")) continue;
		result.push_back(line);
	}
	inputFile.close();
	return result;
}

static void parcerFileOutput(string nameOfOutputFile, vector<string> result) {
	ofstream outputFile(nameOfOutputFile);
	if (!outputFile) { printf("\n\tERROR: OutputFile not exist\n"); return; }
	size_t size = result.size();
	for (int i = 0; i < size; i++)
		outputFile << result[i] << "\n";
	outputFile.close();
	return;
}

static vector<string> mainFunc(vector<string> patterns, vector<string> text, const int threads) {
	vector<string> result;
	string startTheProgram = "\t\t\t The program to find patterns in text\n";
	result.push_back(startTheProgram);
	size_t numberOfStrings = text.size(); 

	omp_set_num_threads(threads);
	#pragma omp parallel for num_threads(threads) 
	for (int i = 0; i < numberOfStrings; i++) {
		/*
		#pragma omp critical 
		{
			printf("\tNumber of thread = %d, number of string = %d\n", omp_get_thread_num(), i);
		}
		*/
		for (int j = 0; j < patterns.size(); j++) {
			string resultOfLine = "";
			if (text[j] == "") continue;
			KMP(patterns[j], text[i], resultOfLine);
			if (!resultOfLine.empty()) {
				string numberLine = "\n\t Pattern \"" + patterns[j] + "\", number of line: " + to_string(i + 1);
				#pragma omp critical 
				{
					result.push_back(numberLine);
					result.push_back(resultOfLine);
					result.push_back(text[i]);
				}
			}
		}
	}
	return result;
}

int main() {

	int arrayOfThreads[] = { 1, 2, 3, 4, 5, 6, 8, 10, 12, 16 };
	const int size = 10;

	printf("\t\t\t The program to find patterns in text\n");
	while (true) {
		string inputFilePatterns = "";
		string inputFileText = "";
		string outputFile = "";
		printf("\n Enter name of inputFile with Array of Patterns\n> ");
		cin >> inputFilePatterns;
		printf("\n Enter name of inputFile with Text\n> ");
		cin >> inputFileText;
		printf("\n Enter name of outputFile\n> ");
		cin >> outputFile;
		vector<string> patterns = parcerFileInput(inputFilePatterns, 0);
		vector<string> text = parcerFileInput(inputFileText, 1);
		chrono::system_clock::duration resultTime[size];
		for (int i = 0; i < size; i++) {
			auto begin = chrono::system_clock::now();
			vector<string> result = mainFunc(patterns, text, arrayOfThreads[i]);
			parcerFileOutput(outputFile, result);
			auto end = chrono::system_clock::now() - begin;
			resultTime[i] = end;
		}
		for (int i = 0; i < size; i++) {
			if (i == 0)
				cout << "\n\t Time for work with not parallel: " << chrono::duration_cast<chrono::milliseconds>(resultTime[i]).count() << " ms\n";
			else
				cout << "\n\t Time for work with " << arrayOfThreads[i] << " threads: " << chrono::duration_cast<chrono::milliseconds>(resultTime[i]).count() << " ms\n";
		}
		printf("\n   Press key \"Y\" to repeat or any other to end the program: ");
		char input = ' ';
		cin >> input;
		if (input != 'Y') break;
	}
	printf("\n   End :) \n");
	return 0;
}
