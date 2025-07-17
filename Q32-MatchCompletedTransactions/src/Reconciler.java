import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

import java.util.Optional;

import java.util.stream.Stream;
import java.util.stream.Collectors;

public class Reconciler {
    public static String BEGIN = "********************** BEGIN reconcile **********************";
    public static String END = "######################  END reconcile  ######################";

    public Reconciler() {
    }

    Stream<PendingTransaction> reconcile(Stream<PendingTransaction> pending,
            Stream<Stream<ProcessedTransaction>> processed) {
        List<PendingTransaction> pendingList = new ArrayList<>();
        Set<Long> processedDone = new HashSet<>();
        List<PendingTransaction> completedList = new ArrayList<>();

        System.out.println(BEGIN);
        // Let's prepare pending first
        if (pending == null) {
            System.out.println("pending stream is null.");
            System.out.println(END);
            return Stream.empty();
        }

        // Retrieve pending trx
        pendingList = pending.collect(Collectors.toList());

        // exit if list is empty
        if (pendingList == null || pendingList.size() == 0) {
            System.out.println("pendingList stream is null or zero length.");
            System.out.println(END);
            return Stream.empty();
        }

        System.out.println(String.format("pendingList has %d items.", pendingList.size()));

        // Let's prepare processed Streams
        if (processed == null) {
            System.out.println("processed stream of streams is null.");
            System.out.println(END);
            return Stream.empty();
        }

        List<ProcessedTransaction> processedList = processed.filter(p -> p != null).flatMap(p -> p)
                // .filter(t -> t != null)
                .collect(Collectors.toList());

        // exit if flattened list is empty
        if (processedList == null || processedList.size() == 0) {
            System.out.println("processedList (from processed stream) is null or zero length.");
            System.out.println(END);
            return Stream.empty();
        }

        System.out.println(String.format("processedList has %d trx.", processedList.size()));

        // Find Ids of completed trx
        // Let's populate processedDone set with the information in processedList
        int j = 0; // let's count the processed trx received
        for (ProcessedTransaction processedTransaction : processedList) {
            if (processedTransaction == null) {
                System.out.println(String.format("processedTransaction # %d is null or empty.", j++));
                continue;
            }

            String idStr = processedTransaction.getId();

            // check Id exists in trx
            if (idStr == null || idStr.trim().isEmpty()) {
                System.out.println(String.format("processedTransaction # %d has null or empty  'Id'.", j++));
                continue;
            }

            // check status is DONE in trx
            Optional<String> optionalStatus = processedTransaction.getStatus();
            if (!optionalStatus.isPresent()) {
                System.out.println(String.format("getStatus() not present in processedTransaction  # %d.", j++));
                continue;
            }

            String status = optionalStatus.get();
            if (status == null || !status.equalsIgnoreCase("DONE")) {
                System.out.println(String.format("processedTransaction # %d has a NOT DONE status.", j++));
                continue;
            }

            long id = Long.parseLong(idStr);
            processedDone.add(id);

            j++;
        }

        System.out.println(String.format("There are %d completed trx", processedDone.size()));

        if (processedDone.isEmpty()) {
            System.out.println("processed stream of streams yield NO Processed trx.");
            System.out.println(END);
            return Stream.empty();
        }

        // Extract completed trx
        for (PendingTransaction pendingTransaction : pendingList) {
            long id = 0;
            if (!processedDone.contains(id)) {
                System.out.println(String.format("pendingTransaction # %d is not complete yet.", id));
                continue;
            }

            pendingTransaction.setStatus("done");
            completedList.add(pendingTransaction);
        }

        System.out.println(END);
        return completedList.stream();
    }

}
