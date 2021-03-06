#include <iostream>
#include <fstream>
#include <string>

int main() {
	int buffsize = 100;
	int numlines = 43200;
	int filenum = 0;
	std::string prefix = "data_part_";
	std::string suffix = ".csv";
	char buffer[buffsize];
	char toprow[buffsize];
	std::ofstream fout;

	std::cin.getline(toprow,buffsize);

	while(std::cin.getline(buffer,buffsize))
	{
		std::string filename = prefix + std::to_string(filenum) + suffix;
		fout.open(filename,std::ofstream::out);
		fout << toprow << std::endl;
		for(int i = 0; i < numlines; i++)
		{
			fout << buffer << std::endl;
			//std::cin.getline(buffer,buffsize);
			if(!std::cin.getline(buffer,buffsize))
			{
				break;
			}
		}
		fout.close();
		filenum++;
	}

	return 0;
}