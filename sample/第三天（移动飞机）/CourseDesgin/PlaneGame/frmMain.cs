using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace PlaneGame
{
    public partial class FormMain : Form
    {
        FightPlace fp = new FightPlace();

        public FormMain()
        {
            InitializeComponent();
                        
            this.Size = new Size(420, 630);         
       
            this.DoubleBuffered = true;            
        }

        private void gameTimer_Tick(object sender, EventArgs e)
        {
            fp.Move();//改变相关数据值
            this.Invalidate();//刷新重绘图片，导致调用FormMain_Paint，使得重绘数据改变的图片，产生动画效果
        }

        private void FormMain_Paint(object sender, PaintEventArgs e)
        {
            fp.Draw(e.Graphics);
        }

        //class three
        private void FormMain_KeyDown(object sender, KeyEventArgs e)
        {
            Mykeyboard.KeyDown(e.KeyCode);
        }
        //class three
        private void FormMain_KeyUp(object sender, KeyEventArgs e)
        {
            Mykeyboard.KeyUp(e.KeyCode);
        }

        private void FormMain_Load(object sender, EventArgs e)
        {

        }
    }
}
