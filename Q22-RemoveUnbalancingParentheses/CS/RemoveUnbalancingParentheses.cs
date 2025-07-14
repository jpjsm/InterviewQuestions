namespace RemoveUnbalancingParentheses;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Begin Task");
        (string input, string output)[] TestCases = new (string input, string output)[]
            { 
                ("1. hi,(H(e)l)lo)", "1. hi,(H(e)l)lo"),
                ("2. hi,(((( Hello", "2. hi, Hello"),
                ("3. hi, Hello)))", "3. hi, Hello"),
                ("4. (h(i,)) (H)(e)((l(l(o))))", "4. (h(i,)) (H)(e)((l(l(o))))"),
                ("5. hi, (H)(e)((l)((l)o", "5. hi, (H)(e)((l)l)o"),
                ("5. hi, ((H)(e)((l)((l)o", "5. hi, ((H)(e)(l)l)o"),
            };
        foreach ((string input, string output) in TestCases)
        {
            if (RemoveUnbalancingParentheses(input) != output) Console.WriteLine($"Failed test: actual='{RemoveUnbalancingParentheses(input)}' != '{output}=expected'");            
        }
        Console.WriteLine("Task Completed");
    }

    public static string RemoveUnbalancingParentheses(string txt)
    {
        int balance = 0;
        string newText = txt;

        int charIndex = 0;
        while (charIndex < newText.Length)
        {
            char indexChar = newText[charIndex];
            switch (indexChar)
            {
                case '(':
                    balance++;
                    break;

                case ')':
                    balance--;
                    if (balance < 0)
                    {
                        newText = newText.Remove(charIndex, 1);
                        balance++;
                        continue;
                    }
                    break;
                default:
                    // do nothing
                    break;
            }

            charIndex++;
        }
        
        if(balance > 0) // we have to remove '(' from the right until balance is zero
        {
            charIndex = newText.Length - 1;
            while (balance > 0 && charIndex >= 0)
            {
                char indexChar = newText[charIndex];
                if (indexChar == '(')
                {
                    string tmpText = newText.Remove(charIndex, 1);
                    newText = tmpText;
                    balance--;
                }

                charIndex--;
            }
        }
        
        return newText;        
    }
}
