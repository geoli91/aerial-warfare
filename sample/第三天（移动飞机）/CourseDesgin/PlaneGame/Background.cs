using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace PlaneGame
{
    class Background
    {   
        const int planeOffset = 2;//设置每次定时器触发时发生偏移的位置

        private Image[] bgrounds;//设置多张图片，每次运行程序随机产生背景图片

        private int pix_x = 0;

        private int pix_y = 0;

        private int index;

        public int Pix_x
        {
            get { return pix_x; }
            set { pix_x = value; }
        }

        public int Pix_y
        {
            get { return pix_y; }
            set { pix_y = value; }
        }

        public int Index
        {
            get { return index; }
            set { index = value; }
        }

       
        //随机生成背景图片
        public Background()
        {
            bgrounds = new Image[4];
            Index = new Random().Next(0, 4);
            bgrounds[0] = GamesResource.background1;
            bgrounds[1] = GamesResource.background2;
            bgrounds[2] = GamesResource.background3;
            bgrounds[3] = GamesResource.background4;
        }

        //按照图片的大小设定图片，并通过定时位置让图片发生偏移。防止有空白，两张图片同时移动。
        public void Draw(Graphics e)
        {
            e.DrawImage(bgrounds[Index], Pix_x, Pix_y, 420, 630);
            e.DrawImage(bgrounds[Index], Pix_x, Pix_y - 630, 420, 630);
        }

        public void Move()
        {
            Pix_y += planeOffset;
            if (Pix_y > 630)
            {
                Pix_y = 0;
            }
        }
    }
}
