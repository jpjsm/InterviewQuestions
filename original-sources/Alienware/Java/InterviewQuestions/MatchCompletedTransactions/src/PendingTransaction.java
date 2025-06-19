import java.util.Optional;

public class PendingTransaction {
    private Long id = null;
    private String description = null;
    private Optional<String> status = null;
    private static long lastGivenId = 0;

    public PendingTransaction() {
    }

    public PendingTransaction(String description) {
        lastGivenId++;
        this.id = lastGivenId;
        this.description = description;
        this.status = Optional.of("InProgress");
    }

    public long getId() {
        return (long) this.id;
    }

    public Optional<String> getStatus() {
        return status;
    }

    public void setStatus(String s) {
        this.status = Optional.of(s);
    }

    public String getDescription() {
        return this.description;
    }

    public void setDescription(String newDescription) {
        this.description = newDescription;
    }

}
