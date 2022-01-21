#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
#include <stdio.h>
#include <conio.h>
using namespace std;
/*Подключение Windows.h обязательно!*/
#include <Windows.h>
int main() {
	srand(static_cast<unsigned int>(time(0)));//генератор чисел
	char q;// переменная для курсора
	int score =0;//переменная для хранения очков
	int eat_X = rand() % 55 +5;//задание рандомных координат цели Х
	int eat_Y = rand() % 22 +3;//задание рандомных координат цели У
	COORD position;	//объявление структуры позиции для персонажа
	COORD position2;// объявление  структуры для пробела(стирание следа)
	COORD position3;// объявление  структуры для целей
	COORD position4;// объявление  структуры для вывода очков
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);	// Получение дескриптора устройства стандартного вывода
	position.X = 20;									// Установка координаты X персонаж
	position.Y = 20;									// Установка координаты Y персонаж
	position2.X = 20;									// Установка координаты X пробел
	position2.Y = 20;									// Установка координаты Y пробел
	position3.X = eat_X;									// Установка координаты X цели
	position3.Y = eat_Y;									// Установка координаты Y цели
	position4.X = 80;									// Установка координаты X пробел
	position4.Y = 2;
	



	cout << "///||||||||||||||||||||||||||||||||||||||||||||||||||||||||||///"
		<< "\n///||||||||||||||||||||||||||||||||||||||||||||||||||||||||||///"
		<< "\n///|                                                        |///       SCORE:"
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |///       TO START w,a,s,d !  "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |///"
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///|                                                        |/// "
		<< "\n///||||||||||||||||||||||||||||||||||||||||||||||||||||||||||///"
		<< "\n///||||||||||||||||||||||||||||||||||||||||||||||||||||||||||///";
		
	
	position3.Y; position3.X; SetConsoleCursorPosition(hConsole, position3); cout << "*";
	
	
	q = _getch();
	while (1) {
		
		
		//Упарвление начало
		if (_kbhit()) {
			q = _getch();
		}
	
		if (q == 'w')

		{
			while (1) {
				position.Y--; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts("O"); Sleep(200);
				position2.Y; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts(" ");
				;
				if (_kbhit()) { q = _getch(); break; }
				if (position3.Y == position.Y - 1 && position3.X == position.X)
				{
				position3.Y = rand() % 22 + 3; position3.X = rand() % 55 + 5; SetConsoleCursorPosition(hConsole, position3); cout << "*";
				score ++;// очки
				if (score++)
				{
					position4.Y; position4.X; SetConsoleCursorPosition(hConsole, position4); cout << score/2;
				}
			    }
				if (position.Y <= 2)
				{
					system("cls");
					cout << "          game  over        \n"
						 << "          score: "<<score;
					break;
				}
			}
			
			
		}
		if (q == 's')
		{
			
			while (1) {
				position.Y++; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts("O"); Sleep(200);
				position2.Y; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts(" "); 
				if (_kbhit()) { q = _getch(); break; }
				if (position3.Y == position.Y+1 && position3.X == position.X)
				{
					position3.Y = rand() % 22 + 3; position3.X = rand() % 55 + 5; SetConsoleCursorPosition(hConsole, position3); cout << "*";
					score++;// очки
					if (score++)
					{
						position4.Y; position4.X; SetConsoleCursorPosition(hConsole, position4); cout << score/2;
					}
				}
				if (position.Y >= 24)
				{
					system("cls");
					cout << "          game  over        \n"
						 << "          score: " << score;
					break;
				}
			}
		}
		if (q == 'a')
		{
			
			while (1) {
				position.X--; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts("O"); Sleep(200);
				position2.X; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts(" ");
				if (_kbhit()) { q = _getch(); break; }
				if (position3.Y == position.Y && position3.X == position.X-1)
				{
					position3.Y = rand() % 22 + 3; position3.X = rand() % 55 + 5; SetConsoleCursorPosition(hConsole, position3); cout << "*";
					score ++;// очки
					if (score++)
					{
						position4.Y; position4.X; SetConsoleCursorPosition(hConsole, position4); cout << score/2;
					}
					
				}
				if (position.X <= 4)
				{
					system("cls");
					cout << "          game  over        \n"
						<< "          score: " << score;
					break;
				}
				
			}
		}
		if (q == 'd')
		{
			while (1) {
				position.X++; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts("O"); Sleep(200);
				position2.X; SetConsoleCursorPosition(hConsole, position);		// Перемещение каретки по заданным координатам
				puts(" "); 
				if (_kbhit()) { q = _getch();break; }
				if (position3.Y == position.Y && position3.X == position.X+1)
				{
					position3.Y = rand() % 22 + 3; position3.X = rand() % 55 + 5; SetConsoleCursorPosition(hConsole, position3); cout << "*";
					score ++;// очки
					if (score++)
					{
						position4.Y; position4.X; SetConsoleCursorPosition(hConsole, position4); cout << score/2;
					}
				}
				if (position.X >= 59)
				{
					system("cls");
					cout << "          game  over        \n"
						<< "          score: " << score<<"        ";
					break;
				}
				
			}
		}
	
		// управление конец
		//карта
		
	}
	/*while (1) {
		cout << "///|                                                        |/// ";
		Sleep(2000);
	}*/
	return 0;
}
