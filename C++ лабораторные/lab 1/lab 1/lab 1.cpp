//практич №1 Задворных П.А. вариант 14
//

//#include "pch.h"
#include <iostream>
#include <cmath>
using namespace std;

class Fig {
public:
	int i;//счетчик
	int rep;// кол-во сторон квадрата
	int num;// номер элемента
	double per;// проценты
	double side[100];//массив со сторонами
	int q;// перменная для swith/case
	char b;
	int sq(double side[])// ф-ция вывода массива сторон

	{
		for (i = 0; i < rep; i++)
		{

			cin >> side[i]; // Вводим с клавиатуры значение ячейки массива
			
		}
		return side[i];
	}
}; 
int main()
{
	Fig a;
	setlocale(LC_ALL, "Russian");
    again4://метка го ту 4
	cout << " введите кол-во  сторон квадрата" << endl;
	cin >> a.rep;
	cout << " введите стороны квадрата" << endl;

	a.sq(a.side);// ф-ция вывода массива сторон
    again:// метка го ту
	cout << " введите желаемый элемент" << endl;
	cin >> a.num;
	if (a.num > a.rep || a.num <= 0)
		goto again;// го ту
	cout<<" ваш выбранный элемент = " << a.side[a.num - 1];
	again2:// метка го ту 2
	cout << " что хотите сделать?\n"
		<< "1- узнать периметр и площадь\n"
		<< "2- узменить на определеный процент\n"
		<< "3 -найти диагональ\n";
	cin >> a.q;
	if(a.q <0||a.q>3 )
		goto again2;// го ту 2
	switch (a.q)
	{
	case 1: // если count = 1
	{
		cout << (a.side[a.num - 1]) * 4<<" - периметр \n";
		cout << (a.side[a.num - 1]) * (a.side[a.num - 1]) << " - площадь \n";
		break;
	}
	case 2: // если count = 2
	{   cout << "введите процент ";
	cin >> a.per;
	cout << endl;
	again3: //метка го ту 3
	cout << " если уменьшить введите - , если увеличить введите + ";
	cin >> a.b;
	if ((a.b != '-') && (a.b != '+'))
		goto again3;// го ту 3
	cout << endl;
	if (a.b != '-')
	cout << (a.side[a.num - 1])+((a.side[a.num - 1]) * (a.per / 100));
	if (a.b != '+')
	cout << (a.side[a.num - 1]) - ((a.side[a.num - 1]) * (a.per / 100));
	break;
	}
	case 3: // если count = 3
	{
		cout << (a.side[a.num - 1]) * 1.41421356237;
		break;
	}

	default: // если count равно любому другому значению
		cout << "неправильно" << endl;
	}
	
	cout << " Хотите попробовать снова? y/n" << endl;
	cin >> a.b;
	if (a.b == 'y')
		goto again4;// го ту 4



}
