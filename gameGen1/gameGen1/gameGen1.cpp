#include <iostream>
#include <cstdlib>
#include <cmath>
#include <time.h>
#define PI 3.14159265
using namespace std;

void gen()
{
    srand(time(NULL));
    const int z= 5;
    const int x = 5;
    int arr[z][x];
    int i;
    int j;
    int q = 0;
    int e = 0;
    int r = 0;
    


    while (1)
    {
        cout << " введите число 0-9: ";
        cin >> q;
        if (q >= 0 && q <= 9)
        {
            break;
        }
        cout << " Неверное число !";
    }

    while (1)
    {
        cout << " введите кол-во предпологаемых повторений 0-25: ";
        cin >> r;
        if (r >= 0 && r <= 25)
        {
            break;
        }
        cout << " Неверное число !";
    }

    for (i = 0; i < 5; i++)
        for (j = 0; j < 5; j++)
        {
            arr[i][j] = rand() % 10;
            
            cout << "\t\t\t" << "  |  " << arr[i][j] ;
            
            if (arr[i][j] == q)
            {
                e++; cout << "+";
            }

        }
    cout << "\n \n ваш прогноз : количества повторений числа: " << q << " равно: " << r;
    cout << "\n \n результат : количество повторений числа: " << q << " равно: " << e;
    if (e == r)
    {
        cout << "\n \n поздраляем, вы угадали :)  " << endl;
    }
    else
    {
        cout << "\n \n вы  не угадали ;(  " << endl;
    }
    


}


int main()
{
    //Изменение кодировки консоли
    setlocale(LC_ALL, "Russian");
    char yn;

    while (1)
    {
        cout << " Хотите поиграть в игру на угадывание чесел!)\n (y/n)" << endl;
        cin >> yn;
        if (yn == 'y')
        {
            gen();
        }
        else
        {
            cout << " досвидания !)\n \n \n";
            break;
        }
    }
    return 0;
}

