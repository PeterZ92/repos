//практич №3 Задворных П.А. вариант 14
//#include "pch.h"
#include <iostream>
#include <cmath>
#include <string>
#include<fstream>

using namespace std;
class MyString 
{

public:
    void set_lab();
    string get_lab();
    void update();
    void print();
    //конструкторы
//конструктор без параметров
    MyString();
//конструктор c параметрами
    MyString(void(MyString::*fun)());
//конструктор копирования
    MyString(const MyString & Str_SubStr);
// деструктор
    ~MyString();
private:
    string* lab = new string;
    string* sublab = new string;
 };

void MyString::set_lab()
{
    string b;
    string sub_b;
    cout << " Введите строку, жалательно использовать пробелы \n";
    getline(cin,b);
    *lab = b;
    *sublab = sub_b;
}
string MyString::get_lab()
{
    return *lab; return *sublab;

}
void MyString::update()
{
    int space = (*lab).find(" ");//поиск пробела 
    int r = (*lab).size();// размер строки


    ofstream MyStr;
    MyStr.open("MyStr.txt",ios_base::out|ios_base::app); // создание открытие .txt для записи
    MyStr << " Введенная строка: " << *lab << endl;
    
    if ((space == string::npos)|| (r % 4 != 0))
        MyStr << " Получение подстроки не удовлетворяет условиям: "  << endl;
    else
        MyStr << " Полученная подстрока: " << *sublab << endl;
    MyStr << " ---------------------------------------------------------- " << endl;
    MyStr.close();
  

}
void MyString::print()
{
    int space = (*lab).find(" ");
    if (space == string::npos)//поиск пробела 
    {
        cout << " строка не содержит пробела \n";
    }
    else
    {
        int y = (*lab).find_last_of(" ");//поиск последнего пробела
        int r = (*lab).size();// размер строки
        

        if (r % 4 == 0)// проверка кратности 4
        {
            
            *sublab = (*lab).substr(y + 1) ;

            cout << " Cтрока годная, вывод строки: " << *lab << "   \n"
                << " Вывод подстроки: " << *sublab;

        }
        else
            cout << *lab << " Данная не удовлетворяет условиям %4 " << "   \n";
    }
}
//конструкторы*****************************
MyString::MyString()//без пар-в
{}
MyString::MyString(void(MyString::* fun)())// с пар-и
{   
    cout << "\n **** Конструктор c параметрами *****************************************\n";
    (this->*fun)();
    MyString::print();
    MyString::update();
}
MyString::MyString(const MyString& Str_SubStr)// к-р копирования
{
    cout << "\n **** Конструктор копирования ******************************************\n";
    
    lab = Str_SubStr.lab;
    sublab = Str_SubStr.sublab;
    MyString::print();
    MyString::update();    
}
// деструктор******************************
MyString::~MyString()
{
    cout << "\n Деструктор \n";
 
}

int main()
{
    setlocale(LC_ALL, "Russian");
    MyString* mss = new MyString(&MyString::set_lab);// к-р с параметрами
    mss;
    MyString* mss_c = new MyString(*mss);// к-р с копирования
    mss_c;
    delete mss_c;
    delete mss;
   
    
    MyString* M = new MyString();// к-р без параметров
    cout << "\n **** Конструктор без параметров ******************************************\n";
    M->set_lab();
    M->get_lab();
    M->print();
    M->update();
    delete M;
 
}


