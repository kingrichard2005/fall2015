using System.IO;
using System;
using System.Linq.Expressions;
using System.Linq;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
        // Lambdas
        Func<int, int> f = x => x * 2;
        
        Func<int, int> h =  (x) => {
            Console.WriteLine("...");
            return x * 2;    
        };
        
        Console.WriteLine(f(3));
        
        Console.WriteLine(h(3));
        
        Expression<Func<int, int>> g = x => x *2;
        
        Console.WriteLine(g);
        
        // List comprehensions
        var xs = new[] {1,2,3,4,5};
        var ys = from x in xs
                    where x < 4
                    select x * 2;
                    
        Console.WriteLine(ys);
        // In C# you can't declare local functions
        /* THIS DOESN"T WORK
        int k ( int x ){
           return x+1; 
        }
        */
        // Higher order functions 'Select' and 'Where' analagous to Haskell's
        // 'Map' and 'Filter' functions, respectively.
    }
}
