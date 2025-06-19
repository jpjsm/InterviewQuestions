namespace InMemoryDatabase;

internal class InMemoryDbValue
{
    private long _timestamp;
    private long _ttl;

    private int _value;

    public int Value => _value;
    public long Timestamp => _timestamp;
    public long TTL => _ttl;

    public InMemoryDbValue(long timestamp, int value)
    {
        _value = value;

        // operations support
        _timestamp = timestamp;
        _ttl = long.MaxValue;
    }

    public InMemoryDbValue(long timestamp, int value, long ttl)
    {
        _value = value;

        // operations support
        _timestamp = timestamp;
        _ttl = timestamp + ttl;
        if (_ttl < 0)
        {
            _ttl = long.MaxValue;
        }
    }

    public void SetValue(long timestamp, int value)
    {
        _value = value;

        // operations support
        _timestamp = timestamp;
        _ttl = long.MaxValue;
    }

    public void SetValueWithTtl(long timestamp, int value, long ttl)
    {
        _value = value;

        // operations support
        _timestamp = timestamp;
        _ttl = timestamp + ttl;
        if (_ttl < 0)
        {
            _ttl = long.MaxValue;
        }
    }

    public bool UpdateValue(long timestamp, int value)
    {
        if (timestamp > _ttl)
        {
            return false;
        }

        _value = value;

        // operations support
        _timestamp = timestamp;
        _ttl = long.MaxValue;
        return true;
    }

    public bool UpdateValueWithTtl(long timestamp, int value, long ttl)
    {
        if (timestamp > _ttl)
        {
            return false;
        }

        _value = value;

        // operations support
        _timestamp = timestamp;
        _ttl = timestamp + ttl;
        if (_ttl < 0)
        {
            _ttl = long.MaxValue;
        }
        return true;
    }

}