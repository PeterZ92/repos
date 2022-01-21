using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _33333
{
    public partial class Form1 : Form
    {
        string fn = string.Empty;//переменная для сохранения строки названия
        List<River> mylist = new List<River>()
        {  
        };//список для хранения расчетов
        static List<double> max = new List<double>();//список для хранения расчетов загрязнений
        double se;//переменая для списка
       
        //словарь(ключ/знач. для связи макс загрязнеия и данных реки
        Dictionary<double, string> maximal = new Dictionary<double, string>();

        public Form1()
        {
            InitializeComponent();
            

        }
        private void Save_Doc()//фунция сохранения документа
        {
            try//если все правильно
            {
                System.IO.StreamWriter sw = new System.IO.StreamWriter(fn, false,
                System.Text.Encoding.GetEncoding(1251));
                sw.Write(richTextBox1.Text);
                sw.Close();
            }
            catch//если ошибка, вызов сообщ ошибки
            {
                MessageBox.Show(" Ошибка сохранения!!!", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }


        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {    //кнопка добавить, добавление в ричтекстбокс
            //если все правильно идет добавление в списки и словарь(ключ/знач),
            //заполнение ричтексбокса
            try
            {
                River R = new River(Convert.ToDouble(textBox2.Text),
                Convert.ToDouble(textBox3.Text),
                Convert.ToDouble(textBox1.Text),
                comboBox1.Text);               
                richTextBox1.Text += R.ToString() + '\n';
                mylist.Add(R);

                se = River.Percent(mylist);
                max.Add(se);
                maximal.Add(se, R.ToString());

                

                Convert.ToString(River.Percent(mylist));
                richTextBox1.Text += "Загрязнение: " + River.Percent(mylist) + " % \n";
            }
            catch//если ошибка, вызов сообщ ошибки
            {
                MessageBox.Show("Ошибка ввода, проверьте поля!!!", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button2_Click(object sender, EventArgs e)
            //кнопка очистить, чистит все поля списки
        {
            richTextBox1.Clear();
            maximal.Clear();
            mylist.Clear();
            max.Clear();
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
           
        


        }

        private void label4_TextChanged(object sender, EventArgs e)
            //блокировка кнопок,если поля не заполнены
        {
            if (textBox1.Text == "" || textBox2.Text == "" || textBox3.Text == "" || comboBox1.Text == "")
            {
                button1.Enabled = false;
                button3.Enabled = false;
            }

            else
            {
                button1.Enabled = true;
                button3.Enabled = true;

            }
        }

        private void button3_Click(object sender, EventArgs e)
        {   //кнопка расчета, ищет максимально грязную реку
            //и выводит инфу по нен

            try //если все правильно вывод инфы в ричтекстбокс
            {
                string riv_max = maximal[max.Max()];


                richTextBox1.Text += "\n**************************\n" +
                   "Макс. загрязнение: " + max.Max() + " % \n" + riv_max
                   + "\n**************************\n";
            }
            catch//если ошибка, вызов сообщ ошибки
            {
                MessageBox.Show(" Ничего не добавлено!!!", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }



        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {   //кнопка сохранения
            //вызывает функцию окна сохранения документа
            SaveFileDialog save = new SaveFileDialog();
            save.Filter = " Текст| * .txt";
            if ( save.ShowDialog()== DialogResult.OK)
            {
                fn = save.FileName;
                Save_Doc();
            }




        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {  //ричтекстбокс, если в нем содержаться какие-то символы,
            //то становится активна кнопка сохранения

            if (richTextBox1.Text != "")
            {
                button4.Enabled = true;

            }

            else
            {
                button4.Enabled = false;


            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        //********** пердупреждение о сохранениии при выходе******
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (richTextBox1.Text != "")
            {
                // пердупреждение о сохранениии
                DialogResult y_n = MessageBox.Show(" Сохранить изменения? ", " Предупреждение",
                MessageBoxButtons.YesNo);
                if (y_n==DialogResult.Yes)//если да то вызов окна сохранения
                {
                    SaveFileDialog save_y_n = new SaveFileDialog();
                    save_y_n.Filter = " Текст| * .txt";
                    if (save_y_n.ShowDialog() == DialogResult.OK)
                    {
                        fn = save_y_n.FileName;
                        Save_Doc();
                    }

                }

            }
        }
        //*** пердупреждение о сохранениии при выходе конец******

        //*******************проверка ввода*********************
        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)//тбокс 2
        {//фильтр ввода (разреш символы '1-9', backspace и ',' не сначала строки
            if ((e.KeyChar >= '0') && (e.KeyChar <= '9'))
                return;
           
            if(Char.IsControl(e.KeyChar))
            {
                if (e.KeyChar == (char)Keys.Back)//разрешаем backspace
                    return;
            }
            e.KeyChar = '\0';//остальные символы запрет
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)//тбокс3
        {//фильтр ввода (разреш символы '1-9', backspace и ',' не сначала строки
            if ((e.KeyChar >= '0') && (e.KeyChar <= '9'))
                return;
            if (e.KeyChar == '.') e.KeyChar = ',';//'.'меняем на','
            if (e.KeyChar == ',')
            {
                if ((textBox3.Text.IndexOf(',') != -1) || (textBox3.Text.Length == 0))
                    e.KeyChar = '\0';//',' только одна и не сначала строки
                return;

            }
            if (Char.IsControl(e.KeyChar))
            {
                if (e.KeyChar == (char)Keys.Back)//разрешаем backspace
                    return;
            }
            e.KeyChar = '\0';//остальные символы запрет

        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)//тбокс1
        {
            //фильтр ввода (разреш символы '1-9', backspace и ',' не сначала строки
            if ((e.KeyChar >= '0') && (e.KeyChar <= '9'))
                return;
            if (e.KeyChar == '.') e.KeyChar = ',';//'.'меняем на','
            if (e.KeyChar == ',')
            {
                if ((textBox1.Text.IndexOf(',') != -1) || (textBox1.Text.Length == 0))
                    e.KeyChar = '\0';//',' только одна и не сначала строки
                return;

            }
            if (Char.IsControl(e.KeyChar))
            {
                if (e.KeyChar == (char)Keys.Back)//разрешаем backspace
                    return;
            }
            e.KeyChar = '\0';//остальные символы запрет
        }
        //************проверка ввода конец*********************
    }
}
