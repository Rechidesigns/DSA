// See https://aka.ms/new-console-template for more information

//Console.WriteLine("Hello, World!");

namespace Section2dsa
{
    class Program
    {
        static void Main(string[] args)
        {
            Section2dsa.section2dsa calculator = new Section2dsa.section2dsa();
            int result = calculator.CalculateSum(10);
            Console.WriteLine("Sum from 1 to 10: " + result);
        }
    }
}
