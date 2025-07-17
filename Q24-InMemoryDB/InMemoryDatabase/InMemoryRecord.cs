namespace InMemoryDatabase;

internal class InMemoryRecord
{
    private long _timestamp;
    private long _ttl;

    private Dictionary<string, InMemoryDbValue> dbFields = new Dictionary<string, InMemoryDbValue>();

    public long Timestamp => _timestamp;
    public long TTL => _ttl;

    public InMemoryRecord(long timestamp)
    {
        _timestamp = timestamp;
        _ttl = long.MaxValue;
    }

    public InMemoryRecord(long timestamp, long ttl)
    {
        _timestamp = timestamp;
        _ttl = timestamp + ttl;
        if (_ttl < 0)
        {
            _ttl = long.MaxValue;
        }
    }

    public bool HasField(long timestamp, string fieldname) => (
        _ttl >= timestamp &&
        dbFields.ContainsKey(fieldname) &&
        dbFields[fieldname].TTL >= timestamp
    );

    public int? Get(long timestamp, string fieldname)
    {
        return HasField(timestamp, fieldname) ?  dbFields[fieldname].Value : null;
    }

    public void Set(long timestamp, string fieldname, int value)
    {
        dbFields[fieldname] = new InMemoryDbValue(timestamp, value);
    }

    public void Set(long timestamp, string fieldname, int value, long ttl)
    {
        dbFields[fieldname] = new InMemoryDbValue(timestamp, value, ttl);
    }

    public Tuple<string, int>[] Scan(long timestamp)
    {
        List<Tuple<string, int>> results = new List<Tuple<string, int>>();

        List<string> fieldNames = dbFields.Keys.Select(k => k).ToList();
        foreach (string fieldname in fieldNames)
        {
            if (dbFields[fieldname].TTL < timestamp)
            {
                dbFields.Remove(fieldname);
                continue;
            }

            results.Add(new Tuple<string, int>(fieldname, dbFields[fieldname].Value));
        }

        return results.ToArray();
    }

    public Tuple<string, int>[] ScanFor(long timestamp, string fieldNameStartsWith)
    {
        List<Tuple<string, int>> results = new List<Tuple<string, int>>();
        List<string> fieldNames = dbFields.Keys.Select(k => k).ToList();
        foreach (string fieldname in fieldNames)
        {
            if (dbFields[fieldname].TTL < timestamp)
            {
                dbFields.Remove(fieldname);
                continue;
            }

            if (fieldname.StartsWith(fieldNameStartsWith))
            {
                results.Add(new Tuple<string, int>(fieldname, dbFields[fieldname].Value));
            }

        }

        return results.ToArray();
    }

}