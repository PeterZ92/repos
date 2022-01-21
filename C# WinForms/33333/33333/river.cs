using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _33333
{
    class River// класс река
    {    //переменные для работы со ввводом
        double fabrics;
        double population;
        double height;      
        string name;

        public River(double fabrics, double population, double height, string name)
        {// конструктор класса
            this.fabrics = fabrics;
            this.population = population;
            this.height = height;      
            this.name = name;
        }

        public override string ToString()//функция возврата строки инфы по реке
        {
            return "Река: " + name + "; Население (тыс.ч): " + population +  "; Фабрики (шт): " + fabrics + "; Протяженность (км): " + height+";";
        }
       public static double Percent(List<River>L)//возвращает значение загрязнения
          {
            double summ = 0.0;
            for(int i=0;i<L.Count;i++)
            {
                summ =((L[i].fabrics) *(L[i].population))/ (L[i].height);
               

            }
            return summ; 
        } 

    }
}
