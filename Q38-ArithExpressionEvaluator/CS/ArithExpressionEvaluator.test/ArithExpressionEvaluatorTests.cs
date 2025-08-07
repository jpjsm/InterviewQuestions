namespace ArithExpressionEvaluator.test;

public class ArithExpressionEvaluatorTests
{
    [Theory]
    [InlineData("()", 0, 0, 1)]
    [InlineData("(())", 0, 0, 3)]
    [InlineData("(())", 1, 1, 2)]
    [InlineData("((()())()()())", 0, 0, 13)]
    [InlineData("((()())()()())", 1, 1, 6)]
    [InlineData("((()())()()())", 2, 2, 3)]
    [InlineData("((()())()()())", 9, 9, 10)]
    [InlineData("(((", 0, -1, -1)]
    [InlineData("", 0, -1, -1)]

    public void GetExpressionTests(string expression, int start, int begin, int end)
    {
        Assert.Equal((begin, end), ExpressionEvaluator.GetExpression(expression, start));
    }

    [Theory]
    [InlineData("( + 1 2 )", 3)]
    [InlineData("( + 1 ( * 2 3 ) )", 7)]
    [InlineData("( * ( + 1 2 ) 3 )", 9)]
    [InlineData("( * ( + 1 2 ) ( * 3 4 ) )", 36)]
    [InlineData("( * ( * ( + 1 2 ) ( * 3 4 ) )  2 )", 72)]
    public void PrefixExpressionTests(string expression, long expected)
    {
        Assert.Equal(expected, ExpressionEvaluator.PrefixExpression(expression));
    }

    [Theory]
    [InlineData("( + 1 2 )", 3)]
    [InlineData("( + 1 ( * 2 3 ) )", 7)]
    [InlineData("( * ( + 1 2 ) 3 )", 9)]
    [InlineData("( * ( + 1 2 ) ( * 3 4 ) )", 36)]
    [InlineData("( * ( * ( + 1 2 ) ( * 3 4 ) )  2 )", 72)]
    public void PrefixExpression2Tests(string expression, long expected)
    {
        Assert.Equal(expected, ExpressionEvaluator.PrefixExpression2(expression));
    }
}
