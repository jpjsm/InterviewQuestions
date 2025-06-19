namespace InMemoryDatabase;

public class InMemoryDB : InMemoryDatabaseBase
{
    private Dictionary<string, InMemoryRecord> _db = new Dictionary<string, InMemoryRecord>();

    public InMemoryDB() { }
    public override void Set(long timestamp, string key, string property, int value)
    {
        if (!_db.ContainsKey(key))
        {
            _db[key] = new InMemoryRecord(timestamp);
        }

        _db[key].Set(timestamp, property, value);
    }

    public override int? Get(long timestamp, string key, string property)
    {
        if (!_db.ContainsKey(key) || !_db[key].HasField(timestamp, property))
        {
            return null;
        }

        return _db[key].Get(timestamp, property);
    }

    public override bool Update(long timestamp, string key, string property, int value)
    {
        if (!_db.ContainsKey(key) || !_db[key].HasField(timestamp, property))
        {
            return false;
        }

        _db[key].Set(timestamp, property, value);
        return true;
    }

    public override string[] Scan(long timestamp, string key)
    {
        if (!_db.ContainsKey(key))
        {
            return Array.Empty<string>();
        }

        return _db[key].Scan(timestamp)
                       .Select(kv => $"{kv.Item1}({kv.Item2})")
                       .ToArray();
    }

    public override string[] ScanFor(long timestamp, string key, string propertyStartsWith)
    {
        if (!_db.ContainsKey(key))
        {
            return Array.Empty<string>();
        }

        return _db[key].ScanFor(timestamp, propertyStartsWith)
                       .Select(kv => $"{kv.Item1}({kv.Item2})")
                       .ToArray();
    }

    public override void SetWithTtl(long timestamp, string key, string property, int value, int ttl)
    {

    }


    public override bool UpdateWithTtl(long timestamp, string key, string property, int value, int ttl)
    {
        return false;
    }

}
