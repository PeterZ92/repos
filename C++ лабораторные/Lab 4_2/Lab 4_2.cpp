//практич №4_2 Задворных П.А. вариант 14
//#include "pch.h"
#include <iostream>
#include <cmath>
#include <string>
#include<ctime>
#include<clocale>
#include<Windows.h>

using namespace std;

class transport
{
public:
	string model;
	int numder;
	void tr()
	{
		cout << " Вид транспорта самолет!\n";
	}

};
class plane: public transport
{
public:
	
	void p_model()
	{
		again:
		cout << " Выберите модель самолета: 1= (Ту); 2= (Як); 3= (Ил); 4= (Boeing).    "
			<< "( цифры соответствует модели!)\n"
			<< " введите выбранную цифру \n ";
		cin >> numder;
		switch (numder)
		{
		case 1:
		{
			cout << " Выбор принят \n";
			model = " ТУ ";
			break;
		}
		case 2:
		{
			cout << " Выбор принят \n";
			model = " ЯК ";
			break;
		}
		case 3:
		{
			cout << " Выбор принят \n";
			model = " ИЛ ";
			break;
		}
		case 4:
		{
			cout << " Выбор принят \n";
			model = " BOEING ";
			break;
		}
		default:
			goto again;
		}
	}

};
class pilot
{
public:
	string name;
	string s_name;

	void g_name()
	{
		cout << " Введите ваше имя!\n ";
	    cin>>name;
		cout << " Введите вашу фамилию!\n ";
		cin>> s_name;
		
	}
	

};
class plane_pilot : public plane, public pilot
{
public:
	void capitan()
	{
		cout 
			 << "           Капитан воздушного судна: " << name << "  " << s_name << "\n"
			 << "           Самолет: " << model << "\n"
			 << "           Налет: "<< 1 + rand() % 200 <<" часов. " << endl;
	}
	void capitan_civ()
	{
	    cout<< "           Ставка: " << 1 + rand() % 900 << "$/чаc. " << endl;
	}

};
class mil_pilot : public plane_pilot
{
public:
	void info_m()
	{
		tr();
		p_model();
		g_name();


	}
	void m_inf()
	{
		cout<<"\n\n\n\n"
			<< "           Карточка военного пилота\n";
		capitan();
		cout << "\n\n           ОСТАЛЬНОЕ ЗАСЕКРЕЧЕНО!!!\n";
	
	}

};
class civ_pilot : public plane_pilot
{
public:
	void info_c()
	{
		tr();
		p_model();
		g_name();


	}
	void c_inf()
	{
		cout << "\n\n\n\n"
			<< "           Карточка ражданского пилота \n";
		capitan();
		capitan_civ();
	}

};

int main()
{
	srand(time(NULL));
	setlocale(LC_ALL, "Russian");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);

	int c_or_w;
again2:
	cout << " Посмотреть информацию о гражданском пилоте - 1.\n"
		 << " Посмотреть информацию о военном пилоте - 2.\n"
		 << " Введите число: \n ";
	cin >> c_or_w;


	switch (c_or_w)
	{
	case 1:
	{
		civ_pilot b;
		b.info_c();
		system("cls");
		b.c_inf();
		
		break;
	}
	case 2:
	{
		mil_pilot a;
		a.info_m();
		system("cls");
		a.m_inf();
		
		break;
	}
	
	default:
		goto again2;
	}
  
}

