using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace PlaneGame
{
    class Mykeyboard
    {
        private static List<Keys> listkey = new List<Keys>();

        public static void KeyUp(Keys key)
        {
            listkey.Remove(key);
        }

        public static void KeyDown(Keys key)
        {
            if (!listkey.Contains(key))
            {
                listkey.Add(key);
            }
        }

        public static bool IsKeyDown(Keys key)
        {
            return listkey.Contains(key);
        }
    }
}
