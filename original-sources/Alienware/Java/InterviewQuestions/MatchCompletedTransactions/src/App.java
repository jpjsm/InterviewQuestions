import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

import java.util.Optional;

import java.util.stream.Stream;
import java.util.stream.Collectors;

public class App {
    private static final String BEGIN = "********************** BEGIN MAIN **********************";
    private static final String END = "######################  END MAIN  ######################\n\n";

    public static void main(String[] args) {
        PendingTransaction nullPendingTransaction = null;
        Stream<PendingTransaction> nullPending = null;
        List<PendingTransaction> pendingListOfNulls = Arrays.asList(nullPendingTransaction, nullPendingTransaction,
                nullPendingTransaction, nullPendingTransaction);
        List<PendingTransaction> pendingList = Arrays.asList(null, new PendingTransaction("one"),
                new PendingTransaction("two"), new PendingTransaction("three"), new PendingTransaction("four"));

        List<ProcessedTransaction> nullProcessed = null;
        Stream<Stream<ProcessedTransaction>> nullStreamOfStreams = null;
        Stream<Stream<ProcessedTransaction>> StreamOfStreamsOfNull = Arrays
                .asList(nullProcessed, nullProcessed, nullProcessed).stream().map(List::stream);
        List<ProcessedTransaction> processedList = Arrays.asList(null, new ProcessedTransaction("1", "one", "done"),
                new ProcessedTransaction("", "two", "done"), new ProcessedTransaction("3", "three", null),
                new ProcessedTransaction(null, "four", "done"));

        Stream<PendingTransaction> actual;
        Reconciler reconciler = new Reconciler();

        System.out.println(BEGIN);
        actual = reconciler.reconcile(nullPending, nullStreamOfStreams);
        actual.forEach(System.out::println);
        System.out.println(END);

        System.out.println(BEGIN);
        actual = reconciler.reconcile(pendingListOfNulls.stream(), nullStreamOfStreams);
        actual.forEach(System.out::println);
        System.out.println(END);

        System.out.println(BEGIN);
        actual = reconciler.reconcile(pendingListOfNulls.stream(), StreamOfStreamsOfNull);
        actual.forEach(System.out::println);
        System.out.println(END);

    }
}
