using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


//////////////////////////////////////    RECURSION     ////////////////////////////



//                   Iterative Recursion


//namespace section1dsa
//{
//    class Recursion
//    {
//        public void calculateiterative(int n)
//        {
//            while (n > 0)
//            {
//                int k = n * n;
//                Console.WriteLine(k);
//                n = n - 1;
//            }
//        }

//        static void Main(string[] args)
//        {
//            Recursion r = new Recursion();
//            r.calculateiterative(4);
//            Console.ReadKey();
//        }
//    }
//}




//                         Recursive Recursion            //
//namespace section1dsa
//{
//    class Recursion2
//    {
//        public void calculaterecursive(int n)
//        {
//            if (n > 0)
//            {
//                int k = n * n;
//                Console.WriteLine(k);
//                calculaterecursive(n - 1);
//            }
//        }

//        static void Main(string[] args)
//        {
//            Recursion2 r = new Recursion2();
//            r.calculaterecursive(4);
//            Console.ReadKey();
//        }
//    }
//}

//////////////////////////////////////    SumofNumbers     ////////////////////////////


namespace section1dsa
{
    class SumofNumbers
    {
        public int sumn(int n)
        {
            return n * (n + 1) / 2;
        }

        public int sumiteration(int n)
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

        public int sumnrecursion(int n)
        {
            if (n == 0)
                return 0;
            return sumnrecursion(n - 1) + n;
        }

        static void Main(string[] args)
        {
            SumofNumbers s = new SumofNumbers();
            Console.WriteLine("Sum: " + s.sumn(5));
            Console.WriteLine("Sum: " + s.sumiteration(5));
            Console.WriteLine("Sum: " + s.sumiteration(5));
            Console.ReadKey();

        }
    }
}