using InMemoryDatabase;

namespace InMemoryDatabaseTests;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        // Arrange
        InMemoryDB db = new InMemoryDB();

        // Act
        var result = db.Scan(1L, "");
        Assert.Equal(result, Array.Empty<string>());
    }
}
