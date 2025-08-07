using System.Text;
using System.Text.RegularExpressions;

namespace ArithExpressionEvaluator;

public static class ExpressionEvaluator
{
    public static HashSet<char> operators = new HashSet<char>() {'+', '*' };

    /// <summary>
    /// Returns a string that represents a number, or a string that starts and ends in balanced parenthesis
    /// </summary>
    /// <param name="expression">The string expression to evaluate</param>
    /// <param name="start">The position on the string to start evaluation</param>
    /// <returns>The expression or the number</returns>
    public static (int begin, int end) GetExpression(string expression, int start, int last = -1)
    {
        if (last == -1)
        {
            last = expression.Length - 1;
        }            
        while (start <= last && expression[start] == ' ') start++;

        if (start > last) return (-1, -1);

        int begin = start;
        switch (expression[start])
        {
            case char c when char.IsDigit(c):
                // Process digits;
                while (char.IsDigit(expression[start])) start++;
                return (begin, start - 1);

            case '(':
                // process expression
                int balance = 1;
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

            default:
                // Unexpected expression format
                return (-1, -1);
        }

    }

    /// <summary>
    /// Evaluates a prefix expression for the '+' or '*' operators.
    /// This function is recursive
    /// </summary>
    /// <param name="expression">
    /// A string of the form: ( operator leftExpression rightExpression ) 
    /// where 'leftExpression', or 'rightExpression' are of the form: expression | integer value
    /// </param>
    /// <returns>The integer value of the expression evaluated</returns>
    /// <exception cref="ArgumentException"></exception>
    /// <exception cref="ApplicationException"></exception>
    /// <remarks>all expressions are well formed and values are integers</remarks>
    public static long PrefixExpression(string expression)
    {
        // expression => operator leftExpression rightExpression | value
        // all expressions are well formed and numbers are integers

        int begin;
        int end;
        (begin, end) = GetExpression(expression, 0);

        if (begin == -1) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");

        int i = 0;
        while (expression[++i] == ' ') ;

        char operador = expression[i];

        while (expression[++i] == ' ') ;

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


        while (expression[++i] == ' ') ;

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
            right = PrefixExpression(expression.Substring(begin, end - begin + 1));
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

    /// <summary>
    /// Evaluates a prefix expression for the '+' or '*' operators.
    /// This function is iterative (non-recursive)
    /// </summary>
    /// <param name="expression">
    /// A string of the form: ( operator leftExpression rightExpression ) 
    /// where 'leftExpression', or 'rightExpression' are of the form: expression | integer value
    /// </param>
    /// <returns>The integer value of the expression evaluated</returns>
    /// <exception cref="ArgumentException"></exception>
    /// <exception cref="ApplicationException"></exception>
    /// <remarks>all expressions are well formed and values are integers</remarks>
    public static long PrefixExpression2(string expression)
    {
        (int begin, int end) = GetExpression(expression, 0);

        if (begin == -1) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");

        string[] expressions = new string[expression.Length / 7 + 1];
        expressions[0] = expression;

        int current = 0;
        int next = 1;
        // Expand expressions
        while (current < next)
        {
            StringBuilder newExpression = new StringBuilder();
            // Find operator
            int i = 1;
            while (expressions[current][i] == ' ') i++;
            if (!operators.Contains(expressions[current][i])) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");
            i++;

            newExpression.Append(expressions[current][0..i]);

            // Find Left value or expression
            (begin, end) = GetExpression(expressions[current], i);
            if (begin == -1) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");

            if (expressions[current][begin] == '(')
            {
                expressions[next] = expressions[current][begin..(end + 1)];
                newExpression.Append($" [{next}] ");
                next++;
            }
            else
            {
                newExpression.Append($" {expressions[current][begin..(end + 1)]} ");
            }

            i = end + 1;
            // Find Right value or expression
            (begin, end) = GetExpression(expressions[current], i);
            if (begin == -1) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");

            if (expressions[current][begin] == '(')
            {
                expressions[next] = expressions[current][begin..(end + 1)];
                newExpression.Append($" [{next}] ");
                next++;
            }
            else
            {
                newExpression.Append($" {expressions[current][begin..(end + 1)]} ");
            }


            newExpression.Append(" )");
            expressions[current] = newExpression.ToString();

            current++;
        }

        // Eval expressions from last to first
        for (int index = next - 1; index >= 0; index--)
        {
            // Find operator
            int i = 1;
            while (expressions[index][i] == ' ') i++;
            if (!operators.Contains(expressions[index][i])) throw new ArgumentException($"{nameof(expression)} is not a valid expression!");
            char op = expressions[index][i];
            i++;

            // find left operand
            while (expressions[index][i] == ' ') i++;

            long left = 0;
            if (expressions[index][i] == '[')
            {
                int r = expressions[index].IndexOf(']', i + 1);
                int valueIndex = Convert.ToInt32(expressions[index][(i + 1)..r]);
                left = Convert.ToInt64(expressions[valueIndex]);
                i = r + 1;
            }
            else
            {
                while (char.IsDigit(expressions[index][i]))
                {
                    left = (expressions[index][i] - '0') + left * 10;
                    i++;
                }
            }


            // find right operand
            while (expressions[index][i] == ' ') i++;

            long right = 0;
            if (expressions[index][i] == '[')
            {
                int r = expressions[index].IndexOf(']', i + 1);
                int valueIndex = Convert.ToInt32(expressions[index][(i + 1)..r]);
                right = Convert.ToInt64(expressions[valueIndex]);
                i = r + 1;
            }
            else
            {
                while (char.IsDigit(expressions[index][i]))
                {
                    right = (expressions[index][i] - '0') + right * 10;
                    i++;
                }
            }

            // Evaluate expression
            expressions[index] = op switch
            {
                '+' => (left + right).ToString(),
                '*' => (left * right).ToString(),
                _ => throw new ApplicationException($"Unexpected operator: '{op}'")
            };
        }

        return Convert.ToInt64(expressions[0]);
    }

}
