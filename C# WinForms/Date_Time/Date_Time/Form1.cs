using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Date_Time
{
    

    public partial class Form1 : Form
    {
        public class VerticalProgressBar : ProgressBar
        {
            protected override CreateParams CreateParams
            {
                get
                {
                    CreateParams cp = base.CreateParams;
                    cp.Style |= 0x04;
                    return cp;
                }
            }
        }
        int d=0;
        
        int sec=20;
        public Form1()
        {
            InitializeComponent();
            progressBar1.Value = 100;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //timer1.Enabled = true;
          
            d++;
          
            label1.Text = Convert.ToString(d);




        again:
            timer1.Enabled = true;


            sec--;
           
            progressBar1.Value -= 5;
            progressBar2.Value += 5;
            progressBar3.Value += 5;

            if (sec <= 0)
            { timer1.Enabled = false;
                sec = 20;
                progressBar1.Value = 100;
                progressBar2.Value = 0;
                progressBar3.Value = 0;
                goto again;
            }

        }

        private void progressBar1_Click(object sender, EventArgs e)
        {
          
        }
    }
}
