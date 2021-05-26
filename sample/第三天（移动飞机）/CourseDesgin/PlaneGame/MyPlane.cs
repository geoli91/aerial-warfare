using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Windows.Forms;

namespace PlaneGame
{

    class MyPlane
    {
        public Image myplane;//飞机图片
        Image redplane;//飞机图片
        Image notredplane;//飞机图片

        Image headimage;//用户头像

        public int Health = 100;//飞机血量

        public int planex = 175;//飞机坐标
        public int planey = 500;//飞机坐标

        //初始化图片
        public MyPlane()
        {
            redplane = GamesResource.planeRedTail;
            notredplane = GamesResource.plane;
            myplane = redplane;
            headimage = GamesResource.imgHeadSheep;
        }


        public void Draw(Graphics mp)
        {
            if (Health > 0)
            {
                mp.DrawImage(myplane, new Point(planex, planey));
            }
            else if (Health < 0)
            {
                mp.DrawImage(myplane, new Point(0, -500));
            }

            mp.DrawImage(headimage, new Point(10, 10));//画头像

            mp.DrawRectangle(new Pen(Color.Black, 1), 10, 90, 102, 10);//画血量条
            mp.FillRectangle(Brushes.Red, 11, 91, Health, 9);//填充血量条

            mp.DrawRectangle(new Pen(Color.Blue, 1), 10, 110, 102, 10);//画完整血量条
            mp.FillRectangle(Brushes.Green, 11, 111, 100, 9);//填充完整血量条

            //显示字符串
            mp.DrawString("Player: 肖斌", new Font("宋体", 9, FontStyle.Bold), Brushes.Yellow, new Point(10, 130));
            mp.DrawString("Score: 100", new Font("宋体", 9, FontStyle.Bold), Brushes.Yellow, new Point(10, 150));
        }


        //class three 
        //改变我的飞机的坐标
        public void Move()
        {
            myplane = myplane == redplane ? notredplane : redplane;

            if (Mykeyboard.IsKeyDown(Keys.A))
            {
                myplane = GamesResource.planeLeft;

                if (planex < 0)
                {
                    planex = 0;
                }

                planex -= 13;

            }
            if (Mykeyboard.IsKeyDown(Keys.D))
            {
                myplane = GamesResource.planeRight;

                if (planex > 360)
                {
                    planex = 360;
                }

                planex += 13;

            }
            if (Mykeyboard.IsKeyDown(Keys.W))
            {               

                if (planey < 0)
                {
                    planey = 0;
                }

                planey -= 13;

            }
            if (Mykeyboard.IsKeyDown(Keys.S))
            {               

                if (planey > 535)
                {
                    planey = 535;
                }

                planey += 13;

            }
        }

    }
}
