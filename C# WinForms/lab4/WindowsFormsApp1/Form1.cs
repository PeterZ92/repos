using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Random rnd = new Random();

        public Form1()
        {
            InitializeComponent();
        }
        /// <summary>
        /// расчет ср арифм полож эл-тов массива
        /// </summary>
        /// <param name="mas">исходный одномерный массив  типа double</param>
        /// <returns>метод возвр ср арифм полож эл-тов массива</returns>
        /// <exception cref="в массиве нет положит"> Искл возсие если ср арифм посчит нельзя нет положит
        public double averagePositiv(double[] mas)
        {
            double s = 0;
            int k = 0;
            for (int i = 0; i < mas.Length; i++)
            {
                if (mas[i] > 0)
                {
                    s += mas[i];
                    k++;
                }
            }
            if (k == 0)
                throw new Exception("В массиве нет положительных!");
            return s / k;
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            dataGridView1.RowCount = 1;
            dataGridView1.ColumnCount = Convert.ToInt32(numericUpDown1.Value);
            for (int i = 0; i < dataGridView1.ColumnCount; i++)
            {
                dataGridView1.Columns[i].Name = i.ToString();
                if (radioButton1.Checked)
                    dataGridView1.Rows[0].Cells[i].Value = 0;
                if (radioButton2.Checked)
                    dataGridView1.Rows[0].Cells[i].Value = (rnd.NextDouble()*200-100).ToString("F1");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridView1.RowCount = 1;
            dataGridView1.ColumnCount = Convert.ToInt32(numericUpDown1.Value);
            for(int i=0;i<dataGridView1.ColumnCount;i++)
            {
                dataGridView1.Columns[i].Name = i.ToString();
                dataGridView1.Rows[0].Cells[i].Value = 0;
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            dataGridView1.RowCount = 1;
            dataGridView1.ColumnCount = Convert.ToInt32(numericUpDown1.Value);
            for (int i = 0; i < dataGridView1.ColumnCount; i++)
            {
                if(radioButton1.Checked)
                dataGridView1.Rows[0].Cells[i].Value = 0;
                if (radioButton2.Checked)
                    dataGridView1.Rows[0].Cells[i].Value = (rnd.NextDouble() * 200 - 100).ToString("F1");

            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                double[] myArray = new double[dataGridView1.ColumnCount];
                for (int i = 0; i < dataGridView1.ColumnCount; i++)
                {
                    myArray[i] = Convert.ToDouble(dataGridView1.Rows[0].Cells[i].Value);
                }
                double Sr = averagePositiv(myArray);
                label2.Text = "Среднее арифметическое полож эл-тов массива  " + Sr;
            }
            catch
            {
                MessageBox.Show(" Некорректный ввод");
            }
        }
    }
}
