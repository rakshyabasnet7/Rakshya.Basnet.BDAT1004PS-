#!/usr/bin/env python
# coding: utf-8

# Question number 1 C#
# 
# 

# 5 : 5 is an integer data type.
# 5.0 : 5.0 is a float data type.
# 5 > 1 : This is a Boolean data type.
# '5' : This is string data type. 
# 5 * 2 : This is integer data type as the result is 10 which is an integer.
# '5' * 2 : This is invalid as we cannot perform string and integer multiplication. 
# '5' + '2': This is string data type.
# 5 / 2 : This is float data type.
# 5 % 2:This is integer data type.
# {5, 2, 1} :This is array data type.
# 5 == 3 : This is Boolean as it gives False output.
# Pi (the number) : This is double or float data type.
# 

# Question number 2 C#

# In[ ]:



namespace Test
{
    class Program
    {
       
       public static void Main(string [] args)
        {
            Program p = new Program();
            p.Q2a("Supercalifragilisticexpialidocious"); // For Question 2a
            p.contains_substring("Supercalifragilisticexpialidocious", "ice");//For Question 2b
            p.longest_word("Supercalifragilisticexpialidocious", "Honorificabilitudinitatibus", "Bababadalgharaghtakamminarronnkonn"); // For Question 2c
            p.dictionary(); // For Question 2d
            
           
        }
        // Calls this function for Question 2a from Main function above
        public void Q2a(String names)
        {

            Console.WriteLine(names.Length);
           

        }

        // Calls this function for Question 2b from Main function above
        public void contains_substring(String word, String substring)
        {
            Boolean containssubstring;

            // using String.Contains() Method
            if (word.Contains(substring))
            {
                containssubstring = true;
                Console.WriteLine(substring + " is present in " + word + ":" + containssubstring);
            }
            else
            {
                containssubstring = false;
                Console.WriteLine(substring + " is not present in " + word + ":" + containssubstring);
            }

        }
        
        // Calls this function for Question 2c from Main function above
        public void longest_word(string word1, string word2, string word3)
        {
            int length1 = (word1.Length);
            int length2 = (word2.Length);
            int length3 = (word3.Length);
            if (length1 > length2 && length1 > length3)

            {
                Console.WriteLine(word1 + " was longest among all.");
            }
            else if (length2 > length1 && length2 > length3)
            {
                Console.WriteLine(word2 + " was longest among all.");
            }
            else
            {
                Console.WriteLine(word3 + " was longest among all.");
            }
        }
        // Calls this function for Question 2d from Main function above
        public void dictionary()
        {
            string[] names = new string[] { "Berlioz", "Borodin", "Brian", "Bartok", "Bellini", "Bernstein", "Buxtehude" };

            Array.Sort(names);
            Console.WriteLine(names[0] + "comes first in dictionary order");
            int len = names.Length;
            Console.WriteLine(names[len - 1] + " is the last composer in dictionary order");// As array start with starting index 0 so taking lenth -1 to get last ordered index value

        }

    }

}


# ![Q2.PNG](attachment:Q2.PNG)

# Question 3 C#

# In[ ]:


namespace Test
{
    class Program
    {
       
       public static void Main(string [] args)
        {
            Program p = new Program();
            p.triangleArea(2, 2, 2); // Calls triangleArea() function for Q3 
        }

        public void triangleArea(int a, int b, int c)
        {
            Console.WriteLine($"Value of side1 = {a}, side2 = {b}, and side3 = {c}");
            double s = (a + b + c) / 2;
            double Area = Math.Sqrt(s * (s - a) * (s - b) * (s - c));

            Console.Write("Area of a Triangle = " + Area);

        }
    }
}


# ![Q3.PNG](attachment:Q3.PNG)

# Question 4 C#

# In[ ]:


namespace Test
{
    class Program
    {
       
       public static void Main(string [] args)
        {
            Program p = new Program();
            p.odd_even();
        }

        public void odd_even()
        {
            int i, n, j = 0, k = 0;//, even = 0, odd = 0;
            Console.WriteLine("Input the number of elements to be stored in the array : ");
            n = Convert.ToInt32(Console.ReadLine()); 
            int[] a = new int[n];
            int[] even = new int[n];
            int[] odd = new int[n];
            Console.WriteLine("Input  elements in the array "); //
            for (i = 0; i < n; i++)
            {
                a[i] = Convert.ToInt32(Console.ReadLine());
            }
            for (i = 0; i < n; i++)
            {
                if (a[i] % 2 == 0)
                {
                    even[j] = a[i]; //store even numbers that satisfies the condition in new array i.e even[]
                    j++;

                }
                else
                {
                    odd[k] = a[i]; //store odd numbers that satisfies the condition in new array i.e odd[]
                    k++;

                }
            }
            //Print all the even numbers from the array
            Console.WriteLine("The Even elements are :");
            for (i = 0; i < j; i++)
            {
                Console.Write("{0}  ", even[i]);

            }
            Console.WriteLine("\n");
            //Print all the even numbers from the array
            Console.WriteLine("The Odd elements are :");
            for (i = 0; i < k; i++)
            {

                Console.Write("{0}  ", odd[i]);
            }
        }
    }


# ![Q4.PNG](attachment:Q4.PNG)

# Question 5 C#

# In[ ]:


namespace Test
{
    class Program
    {
       
       public static void Main(string [] args)
        {
            Program p = new Program();
           
            Console.WriteLine("Answer 5a: \n");
            Boolean result = p.inside(1, 1, 0, 0, 2, 3); // Calling inside function to verify
            Console.WriteLine(result);
            Boolean result1 = p.inside(-1, -1, 0, 0, 2, 3);
            Console.WriteLine(result1);
            Console.WriteLine("-----------------------------------------------");
            Console.WriteLine("Answer 5b: \n");
            Boolean test1 = p.inside(1, 1, 0.3, 0.5, 1.1, 0.7);
            Console.WriteLine(test1);
            Boolean test2 = p.inside(1, 1, 0.5, 0.2, 1.1, 2);
            Console.WriteLine(test2);
            if (test1 == true && test2 == true)
            {
                Console.WriteLine("(1,1) lies in rectangle in between (0.3,0.5) and (1.1,0.7) and also in rectangle in between (0.5,0.2) and (1.1,2)");
            }
            else
            {
                Console.WriteLine("Not satisfied ");
            }

            
        }

        public Boolean inside(int x, int y, double x1,
                      double y1, double x2, double y2)
        {

            if (x > x1 && x < x2 && y > y1 && y < y2)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}


# ![Q5.PNG](attachment:Q5.PNG)

# In[ ]:




