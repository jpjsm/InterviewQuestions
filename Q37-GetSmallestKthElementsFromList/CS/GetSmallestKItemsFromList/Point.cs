namespace jpjsm.GetSmallestKItemsFromList;

public struct Point
{
    private readonly double _x;
    private readonly double _y;
    public readonly double X => _x;
    public readonly double Y => _y;

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