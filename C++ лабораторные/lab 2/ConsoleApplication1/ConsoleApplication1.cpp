//практич №2 Задворных П.А. вариант общий
//#include "pch.h"
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Worker
{
public: 
	int age;
	string name;
	void eat(float how_muth);
	float get_weight();
	int get_mood();// настроение
	void set_mood(int a);
	void walk(int how_muth);
	void dance(int how_muth);
	void work(int how_muth);
	
private:
	float weight;
	int mood;
};

void Worker::walk(int how_muth)// метод гулять :)
{
	mood= ( mood + (1* how_muth));
}
void Worker::dance(int how_muth)// метод танцевать :))
{
	mood =( mood +(2 * how_muth));
}
void Worker::work(int how_muth)// метод работать :((
{
	mood =( mood - (2 *how_muth));
	
}

void Worker::eat(float how_muth)// метод кушать
{
	if (how_muth > 10)
	{
	weight = weight +( how_muth / 2);
	age ++;
    }
	else  
	  weight = weight + how_muth;
  }
  float Worker::get_weight()//взять вес
  {
	  return weight;
  }
  int Worker::get_mood()// взять настроение
  {
	  if (mood < 0)
	  {
		  return mood = 0;// условие возвращения 0 отрицательного настроения не бывает!
	  }
	  return mood;
  }
  void Worker::set_mood(int a)// взять настроение
  {
	  mood=a;
  }


int main()
{
   setlocale(LC_ALL, "Russian");
   Worker* wrk1 = new Worker();
   wrk1-> age = 34; 
   wrk1->name = "Иванов";
   wrk1->set_mood(10);
   cout << " Свединия о работнике: " << wrk1->age << ", " << wrk1->name << endl;
   //wrk1->weight = 70;// попытка изменения приват переменной
   /*wrk1->eat(2);
   wrk1->eat(3);*/
   wrk1->eat(15);

   float ves;//вес
   ves = wrk1->get_weight();
  
   int day_mood;//настроение
   day_mood= wrk1->get_mood();//??? не меняется???

   cout << " Работник накушал: " << ves << " кг.\n";
   cout << " Возраст: " << wrk1->age << " лет.\n";
   // манипеляции с настроением :)
   cout << " Настроение с утра: " << day_mood << " баллов\n";
   wrk1->walk(2);
   cout << " По закону Aрхимеда после сытного обеда надо 2 раза погулять.\n Настроение: " << wrk1->get_mood() << " баллов \n";
   wrk1->dance(3);
   cout << " И три раза потанцевать.\n Настроение: " << wrk1->get_mood() << " баллов\n";
   wrk1->work(9);
   cout << " Чуть- чуть переработал ;(((\n Настроение: " << wrk1->get_mood() << " баллов\n";// тест минусового настроения (отрицателього не бывает)
   wrk1->dance(4);//проверка
   cout << " Восполним настроение.\n Настроение: " << wrk1->get_mood() << " баллов\n";  
}

