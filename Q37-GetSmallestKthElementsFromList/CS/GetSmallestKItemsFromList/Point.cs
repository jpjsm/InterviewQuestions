namespace jpjsm.GetSmallestKItemsFromList;

public class Point
{
    private readonly double _x;
    private readonly double _y;
    public double X => _x;
    public double Y => _y;

    public Point(double x, double y)
    {
        _x = x;
        _y = y;
    }

    public double DistanceToOrigin()
    {
        return Math.Sqrt(X * X + Y * Y);
    }

    public override string ToString()
    {
        return $"({_x}, {_y})";
    }
}