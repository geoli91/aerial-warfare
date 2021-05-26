using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace PlaneGame
{
    class FightPlace
    {
        Background bg = new Background();

        MyPlane mp = new MyPlane();//class two

        public void Move()
        {
            bg.Move();

            //class three
            mp.Move();
        }

        public void Draw(Graphics e)
        {
            bg.Draw(e);

            mp.Draw(e);//class two
          
        }



    }
}
