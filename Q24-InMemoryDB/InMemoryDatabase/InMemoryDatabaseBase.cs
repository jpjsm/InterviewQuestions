namespace InMemoryDatabase;

public abstract class InMemoryDatabaseBase
{
    public abstract void Set(long timestamp, string key, string property, int value);

    public abstract bool Update(long timestamp, string key, string property, int value);

    public abstract int? Get(long timestamp, string key, string property);

    public abstract string[] Scan(long timestamp, string key);

    public abstract string[] ScanFor(long timestamp, string key, string propertyStartsWith);

    public abstract void SetWithTtl(long timestamp, string key, string property, int value, int ttl);

    public abstract bool UpdateWithTtl(long timestamp, string key, string property, int value, int ttl);

}
