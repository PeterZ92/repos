// lab 1_2.cpp : Лабораторна работа 1.2 вариант 14(сельское хозяйсво).
//#include "pch.h"
#include <iostream>
#include <string>
using namespace std;

class cows {
public:
	int qua; double milk_vol; double milk_fat; int eat_24; int bull; int young; double price; string name;
	void qality()
	{
		cout << " Количесво коров = " << qua - (bull + young) << " шт" << endl;
		cout << " Количесво молока = " << milk_vol << " л.\n "
			<< " Количесво сливок в молоке = " << milk_vol*milk_fat << " шт" << endl;
	}
	void all_eat()
	{
		cout << " Всего сена в день " << eat_24 << " кг \n"
			 << " Потребление сена день одной еденицей скота = " << eat_24 / qua << " кг " << " В год = " << (eat_24 / qua) * 365 << " кг " << endl;
	}
	double market(int a, double b)
	{
		double c = (a/2) * b;
		return c;
	}
	void sales()
	{
		cout << " Планируется продать половину телят: " << young/2 << " Шт \n";
	}
	

};

class chikens {
public:
	int qua; int eggs_vol;  double eat_24; int rosters; int young; double price; string name;

	void qality()
	{
		cout << " Количесво куриц несушек = " << qua - (rosters + young) << " шт" << endl;
		cout << " Количесво яиц общее = " << eggs_vol << " шт.\n "
			<< " Количесво яиц на одну курицу = " << eggs_vol / (qua - (rosters + young)) << " шт" << endl;
	}
	void all_eat()
	{
		cout << " Всего потребляется пшеницы в день " << eat_24 << " кг \n"
			<< " Среднее потребление одной курицей в день = " << eat_24 / qua << " кг " << " В год = " << (eat_24 / qua) * 365 << " кг " << endl;
	}
	double market(int a, double b)
	{
		double c = a * b;
		return c;
	}
	void sales()
	{
		cout << " Планируется продать всех цыплят: " << young << " Шт \n";
	}


};

class pigs {
public:
	int qua; int meat; int walking; double eat_24; int young; double price; string name;
	void qality()
	{
		cout << " Количесво свиней всего = " << qua << " шт" << endl;
		cout << " Количесво взрослых свиней = " << qua - young << " шт. " << " Количесво взрослых поросят = " << young << " шт.\n "
			<< "Rоличество корма среднее на одного хрюшу в сутки = " << eat_24/qua << " кг" << endl;
	}
	void all_eat()
	{
		cout << " Свиней на домашнем пастбище " << qua - (walking+meat) << " шт \n"
			<< " Свиней на мясокомбинате " << meat << " шт \n" 
			<< " Свиней на дальнем пастбище " << walking << " шт " << endl;
	}
	double market(int a, double b)
	{
		double c = (a/2) * b;
		return c;
	}
	void sales()
	{
		cout << " Планируется продать половину поросят: " << young/2 << " Шт \n";
	}

	
};

class sheeps {
public:
	int qua; int wool; int walking; double eat_24; int young;  double price; string name;
	void qality()
	{
		cout << " Количесво овец всего = " << qua - young << " шт" << endl;
		cout << " Количесво съедаемой травы одной овцой в сутки = " <<eat_24/qua << " кг.\n "
			<< " Количесво шерсти = " << wool << " кг.\n "
			 << " Количесво шерсти с одной взрослой овцы = " <<wool/( qua - young) << " шт" << endl;
	}
	void all_eat()
	{
		cout << " Овец на домашнем пастбище " << qua- walking << " шт \n"
			<< " Овец на дальнем пастбище " << walking << " шт " << endl;
	}
	double market(int a, double b)
	{
		double c = a * b;
		return c;
	}
	void sales()
		{
			cout << " Планируется продать всех овечек: " << young << " Шт \n";
		}
};

class dogs {
public:
	int qua; int sec_ty; int at_home; int toys; int young; double price; string name;
	void qality()
	{
		cout << " Количесво собак всего = " << qua << " шт" << endl;
		cout << " Количесво щенков = " <<  young << " шт" << endl;
		cout << " Количесво игрушек = " << toys << " шт";
			
	}
	void all_eat()
	{
		cout << " Собак на охране пастбища " << sec_ty << " шт \n"
			<< " Собак на охране дома " << at_home << " шт\n " 
			<< " Собак свободно " <<qua-( at_home+sec_ty) << " шт\n " << endl;
	}
	double market(int a, double b)
	{
		double c = a * b;
		return c;
	}
	void sales()
	{
		cout << " Планируется продать всех щенков: " << young << " Шт \n";
	}
};

struct space
{
	void spaces()
	{
		cout << "**************************************************************************************"<<endl;
	}
};


int main()
{
	setlocale(LC_ALL, "Russian");
	cows a{ 100,2000,5,400,10,20,1500,"Мурка" };
	chikens b{ 400,1600,50,40,100,15,"Цыпа" };
	pigs c{ 100,10,50,200,20,600,"Хрюша" };
	sheeps d{ 200,400,50,450,140,300,"Пушок" };
	dogs e{ 30,10,5,40,10,150,"Жучёк" };
	space star;

	star.spaces();//разделитель звёздочками ****
	// класс с коровами
	a.qality();
	a.all_eat();
	a.sales();
	star.spaces();//разделитель звёздочками ****
	//класс с курами
	b.qality();
	b.all_eat();
	b.sales();
	star.spaces();//разделитель звёздочками ****
	//класс хрюши
	c.qality();
	c.all_eat();
	c.sales();
	star.spaces();//разделитель звёздочками ****
    // класс овечки
	d.qality();
	d.all_eat();
	d.sales();
	star.spaces();//разделитель звёздочками ****
	//класс собаки
	e.qality();
	e.all_eat();
	e.sales();
	star.spaces();//разделитель звёздочками ****
	//выручка с продажи
	cout << "\n Выручка с продажи телят = " << a.market(a.young, a.price) << " $ "
		<< "\n Выручка с продажи телят = " << b.market(b.young, b.price) << " $ "
		<< "\n Выручка с продажи телят = " << c.market(c.young, c.price) << " $ "
		<< "\n Выручка с продажи телят = " << d.market(d.young, d.price) << " $ "
		<< "\n Выручка с продажи телят = " << e.market(e.young, e.price) << " $ \n";
	    
	star.spaces();//разделитель звёздочками ****
	cout << " Количество животных на ферме = " << a.qua+ b.qua+ c.qua+ d.qua+ e.qua << " голов \n";
	
	star.spaces();//разделитель звёздочками ****
	cout << " ИМИ ГОРДИТСЯ НАШЕ ХОЗЯЙСТВО!!! \n"
		<<" "<< a.name << "\n"
		<< " " << b.name << "\n"
		<< " " << c.name << "\n"
		<< " " << d.name << "\n"
		<< " " << e.name << "\n";

	star.spaces();//разделитель звёздочками ****   
}


