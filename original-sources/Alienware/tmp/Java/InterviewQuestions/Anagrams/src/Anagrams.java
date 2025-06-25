import java.util.List;
import java.util.Collections;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.math.BigInteger;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.File;

public class Anagrams {
    public static int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
            83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
            197, 199 };
    public static String letters = "abcdefghijklmnopqrstuvwxyz'";

    public static Map<Character, Integer> letter2prime = new HashMap<>(32);

    public static String GetKeyFromWord1(String word) {
        char[] keyarray = word.toLowerCase().toCharArray();
        Arrays.sort(keyarray);
        return new String(keyarray);
    }

    public static String previousWord = "";

    public static BigInteger GetKeyFromWord2(String word) {
        char[] chararray = word.toLowerCase().toCharArray();
        BigInteger key = BigInteger.ONE;
        for (int i = 0; i < chararray.length; i++) {
            // key *= letter2prime.get(chararray[i]);
            char c = chararray[i];
            if (!letter2prime.containsKey(c)) {
                throw new Error(
                        String.format("char %1$s not in letters2prime. check word: '%2$s', previous word '%3$s'", c,
                                word, previousWord));
            }
            key = key.multiply(BigInteger.valueOf(letter2prime.get(chararray[i])));
        }

        previousWord = word;
        return key;
    }

    public static List<List<String>> GetAnagramGroups1(List<String> words) {
        HashMap<String, List<String>> anagramgroups = new HashMap<String, List<String>>(words.size());
        List<String> current = new ArrayList<String>();

        for (String word : words) {
            String key = GetKeyFromWord1(word);
            if (!anagramgroups.containsKey(key)) {
                anagramgroups.put(key, new ArrayList<String>());
            }

            current = anagramgroups.get(key);
            current.add(word);
            anagramgroups.put(key, current);
        }

        List<List<String>> results = new ArrayList<List<String>>();
        for (List<String> anagrams : anagramgroups.values()) {
            if (anagrams.size() < 2) {
                continue;
            }

            results.add(anagrams);
        }

        return results;
    }

    public static List<List<String>> GetAnagramGroups2(List<String> words) {
        HashMap<BigInteger, List<String>> anagramgroups = new HashMap<BigInteger, List<String>>(words.size());
        List<String> current = new ArrayList<String>();

        for (String word : words) {
            BigInteger key = GetKeyFromWord2(word);
            if (!anagramgroups.containsKey(key)) {
                anagramgroups.put(key, new ArrayList<String>());
            }

            current = anagramgroups.get(key);
            current.add(word);
            anagramgroups.put(key, current);
        }

        List<List<String>> results = new ArrayList<List<String>>();
        for (List<String> anagrams : anagramgroups.values()) {
            if (anagrams.size() < 2) {
                continue;
            }

            results.add(anagrams);
        }

        return results;
    }

    public static void main(String[] args) {
        // Initialize letter2prime map
        // for GetAnagramGroups2
        for (int i = 0; i < letters.length(); i++) {
            letter2prime.put(letters.charAt(i), primes[i]);
        }

        String filePath = "C:\\tmp\\Java\\Anagrams\\src\\words.txt";
        File words_file = new File(filePath);

        ArrayList<String> words = new ArrayList<String>();
        words.add("Pores");
        words.add("Fear");
        words.add("Poser");
        words.add("one");
        words.add("Prose");
        words.add("Ropes");
        words.add("two");
        words.add("Spore");
        words.add("Fare");

        if (words_file.exists()) {
            words.clear();

            try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
                String line;
                while ((line = br.readLine()) != null) {
                    String trimmed = line.trim();
                    if (trimmed.length() == 0) {
                        continue;
                    }
                    words.add(line);
                }

            } catch (IOException e) {
                e.printStackTrace();
                return;
            }
        }

        int group = 0;
        List<List<String>> anagramgroups = GetAnagramGroups1(words);
        Collections.sort(anagramgroups, Comparator.comparingInt(List::size));
        for (List<String> anagramgroup : anagramgroups) {
            if (anagramgroup.size() < 10) {
                continue;
            }
            System.out.println(String.format("1  | Group[%1$6d] size: %2$2d: %3$s", ++group, anagramgroup.size(),
                    String.join(", ", anagramgroup)));
        }

        group = 0;
        anagramgroups = GetAnagramGroups2(words);
        Collections.sort(anagramgroups, Comparator.comparingInt(List::size));
        for (List<String> anagramgroup : anagramgroups) {
            if (anagramgroup.size() < 10) {
                continue;
            }
            System.out.println(String.format("2  | Group[%1$6d] size: %2$2d: %3$s", ++group, anagramgroup.size(),
                    String.join(", ", anagramgroup)));
        }
    }

}
