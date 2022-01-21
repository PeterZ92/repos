//практич №2,2 Задворных П.А. вариант 14
//#include "pch.h"
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Sqare
{
public:
	double get_side();
	void set_side();
	void sq_and_per();
	void percent();
	void diagon();
	double perc;
	char simb;

private:
	double side;
	
};



double Sqare::get_side()// взять сторону квадрата
{

	return side;
}
void Sqare::set_side()// задать сторону квадрата
{
again1://метка го ту 1
	double a;
	cout << " Введите сторону квадрата: " << "  \n";
	cin >> a;
	if (a <= 0)
	{
		cout << " Попробуйте снова!!!" << "  \n";
		goto again1;//го ту 1
	}
	side = a;

}
void Sqare::percent()//расчет изменения стороны на процент
{
again2://метка го ту 3
	cout << " введите процент " << "  \n";
	cin >> perc;
	if (perc <= 0)
goto again2;// го ту 2
	cout << endl;
again3: //метка го ту 3
	cout << " если уменьшить введите - , если увеличить введите + " << "  \n";
	cin >> simb;
	if ((simb != '-') && (simb != '+'))
goto again3;// го ту 3
	cout << endl;
	if (simb != '-')
	{
		side +=(side) * (perc / 100);// проценты укзаны на оборот, по этому вместо -= идет +=
		cout << " Измененная сторона ровна: " << side << "  \n";
	}

	if (simb != '+')
	{
		side -=(side) * (perc / 100);// проценты укзаны на оборот, по этому вместо += идет -=
		cout << " Измененная сторона ровна: " << side << "  \n";
	}
}
void Sqare::sq_and_per() //расчет площади квадрата
{
	cout<<" Площадь равна: "<< side * side<<"  \n";
	cout << " Периметр равен: " << side * 4 << "  \n";
}
void Sqare::diagon()
{
	cout <<" Диагональ равна: "<< (side) * 1.41421356237 << "  \n";
}



int main()
{
	setlocale(LC_ALL, "Russian");
	Sqare* sq = new Sqare();

	sq->set_side();
	sq->percent();
	sq->sq_and_per();
	sq->diagon();
}
