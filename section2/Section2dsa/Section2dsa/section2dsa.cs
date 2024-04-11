using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Section2dsa
{
    internal class section2dsa
    {
        public int CalculateSum(int n)
        {
            int total = 0;
            int i = 1;
            while (i <= n)
            {
                total = total + i;
                i = i + 1;
            }
            return total;
        }
    }
}

