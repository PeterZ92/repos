//ДКР №1 Задворных П.А. вариант 14
//#include "pch.h"
#include <iostream>
#include <cmath>
#include <string>
#include<fstream>
#include<ctime>

using namespace std;
// Родительский класс для записи чисел в файл
class Recording
{
protected:
    int rec_rand = 20;//кол-во рандомных чисел
    int counter = 0;//счетчик для цикла записи
    string stars;// строка для звёздочек
public:
    //Recording();
    void record_numb();

    ~Recording()
    {
    }

};
// дочерний класс для чтения с файла и вывода на экран
class Reading: public Recording
{
public:
    
   
    int* r_numb = new int[rec_rand];// динам. массив для записи/ выода чисел
    void read_numb();


};

void Recording::record_numb()
{
    ofstream  Rec;
    Rec.open("Rand_Numbers.txt", ios_base::out | ios_base::trunc); // создание открытие .txt для записи
    if (Rec.is_open())//если фаил открывается

    {
        while (counter < rec_rand)
        {
            Rec << 1 + rand() % 72 << endl;
            counter++;
        }
    }
    else//если фаил не открывается или не создается
    {
        cout << " Файл  не открыт/не создан";
    }
    Rec.close();
}

void Reading::read_numb()
{
   // r_numb[rec_rand];
    
    ifstream Read;
    Read.open("Rand_Numbers.txt", ios_base::in); // открытие .txt для чтения
    if (Read.is_open())//если фаил открывается
       
    { 
        cout << " Числа из файла: ";
        for (int i = 0; i < rec_rand; i++)
        {
            Read >> r_numb[i];//запись в массив
            cout << r_numb[i] << " " ;//вывод чисел
        }
        cout << "\n Результат: \n";
        for (int j = 0; j < rec_rand; j++)
        {
            int star_int = r_numb[j];
            cout<<" Число №"<<j+1<<" = "<< r_numb[j] << " "<<stars.append(star_int,'*') << endl;//вывод чисел со звёздочками
           stars.clear();// чистим строк, чтобы "*" не накапливались
        }
       
    

    }
    else//если фаил не открывается
    {
        cout << " Файл  не открыт";
    }

    Read.close();
  
}

int main()
{
    setlocale(LC_ALL, "Russian");
    srand(time(NULL));

    Recording Rec;
    Rec.record_numb();
    Reading R;
    R.read_numb();

}

