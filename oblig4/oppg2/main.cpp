#include <iostream>
#include <string>
using namespace std;


string replace (string sentence, string old_w, string new_w);

int main()
{

    string sentence("< > & > &");
	cout << "Old sentence: " << sentence << endl;

	sentence = replace(sentence, "&", "&amp");
	sentence = replace(sentence, "<", "&lt");
	sentence = replace(sentence, ">", "&gt");


	cout << "New sentence: " << sentence << endl;


    return 0;
}

string replace (string sentence, string old_w, string new_w) {

	int index = 0;

    while (true) {
		index = sentence.find(old_w, index);
		
		if (index == -1) {
			break;
		}

        sentence.replace(index, old_w.length(), new_w);
		index++;
	}

    return sentence;	

}

