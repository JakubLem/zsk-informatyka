#include <iostream>
#include <fstream>

using namespace std;

int main(){
	int * tab;
	tab = new int[5];
	fstream file;
	file.open("data.txt", ios::in);
	for(int i = 0 ; i < 5 ; i++){
		file >> tab[i];
	}
	for(int i = 0 ; i < 5 ; i++){
		cout << tab[i];
	}
    return 0;
}
