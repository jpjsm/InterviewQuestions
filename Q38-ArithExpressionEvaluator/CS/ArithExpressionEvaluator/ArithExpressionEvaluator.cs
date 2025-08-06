namespace ArithExpressionEvaluator;

public static class ExpressionEvaluator
{
    public static (int begin, int end) GetExpression(string expression, int start)
    {
        while (start < expression.Length && expression[start] != '(') start++;

        if (start >= expression.Length) return (-1, -1);

        int balance = 1;
        int begin = start;
        start++;
        while (start < expression.Length && balance > 0)
        {
            switch (expression[start])
            {
                case '(':
                    balance++;
                    break;
                case ')':
                    balance--;
                    break;
                default:
                    // Ignore char
                    break;
            }

            start++;
        }

        if (balance != 0) return (-1, -1);

        return (begin, start - 1);
    }
    public static long PrefixExpression(string expression)
    {
        // expression => operator leftExpression rightExpression | value
        // all expressions are well formed and numbers are integers

        int begin;
        int end;
        (begin, end) = GetExpression(expression, 0);

        if (begin == -1) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");

        int i = 0;
        while (expression[++i] == ' ');

        char operador = expression[i];

        while (expression[++i] == ' ');

        long left = 0;
        if (char.IsDigit(expression[i]))
        {
            while (char.IsDigit(expression[i]))
            {
                left = (expression[i] - '0') + 10 * left;
                i++;
            }
        }
        else
        {
            (begin, end) = GetExpression(expression, i);
            left = PrefixExpression(expression.Substring(begin, end - begin + 1));
            i = end + 1;
        }


        while (expression[++i] == ' ');

        long right = 0;
        if (char.IsDigit(expression[i]))
        {
            while (char.IsDigit(expression[i]))
            {
                right = (expression[i] - '0') + 10 * right;
                i++;
            }
        }
        else
        {
            (begin, end) = GetExpression(expression, i);
            right = PrefixExpression(expression.Substring(begin, end-begin+1));
            i = end + 1;
        }

        long result;
        switch (operador)
        {
            case '+':
                result = left + right;
                break;

            case '*':
                result = left * right;
                break;

            default:
                throw new ApplicationException($"Unexpected operator: '{operador}'");
        }


        return result;
    }

}
