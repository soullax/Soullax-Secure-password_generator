using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;


namespace Soullax_Secure
{
    public partial class PasswordGen : Form
    {
        public PasswordGen()
        {
            InitializeComponent();
        }

        private void metroButton1_Click(object sender, EventArgs e)
        {
            About objUI = new About();
            objUI.Show();
        }

        private void metroButton3_Click(object sender, EventArgs e)
        {
            Process.Start("genpass.bat");
            this.Close();
        }

        private void PasswordGen_Load(object sender, EventArgs e)
        {
            richTextBox1.LoadFile("password.txt",
            RichTextBoxStreamType.PlainText);
        }
    }
}
