import java.util.Optional;

public class ProcessedTransaction {
    private String id = null;
    private String description = null;
    private Optional<String> status = null;

    public ProcessedTransaction() {
    }

    public ProcessedTransaction(String newId, String description, String newStatus) {
        String idStr = newId == null ? "" : newId.trim();
        try {
            long idLong = Long.parseLong(idStr);
            this.id = String.valueOf(idLong);
        } catch (NumberFormatException e) {
            this.id = Constants.NullString;
        }

        this.description = description;
        this.status = newStatus == null || newStatus.trim().isEmpty() ? Optional.empty() : Optional.of(newStatus);
        ;
    }

    public String getId() {
        return this.id;
    }

    public Optional<String> getStatus() {
        return status;
    }

    public void setStatus(String s) {
        this.status = s == null || s.trim().isEmpty() ? Optional.empty() : Optional.of(s);
    }

    public String getDescription() {
        return this.description;
    }

    public void setDescription(String newDescription) {
        this.description = newDescription;
    }

}
