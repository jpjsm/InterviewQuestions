package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Wrong number of arguments!\nUsage: ExcelHeaders <number-of-columns>\n")
		panic(-1)
	}

	n, err := strconv.ParseUint(os.Args[1], 10, 32)
	if err != nil {
		panic(err)
	}

	labels := excelHeaders(int(n))

	for _, label := range labels {
		fmt.Println(label)
	}
}

func excelHeaders(n int) []string {
	const LettersInEnglish = 26
	letters := []rune("abcdefghijklmnopqrstuvwxyz")
	var results []string = make([]string, n)

	prefix := ""
	prefixIndex := -1
	for iteration := 0; iteration < n; iteration++ {
		for i := 0; i < LettersInEnglish; i++ {
			results[iteration] = prefix + string(letters[i])
			iteration++
			if iteration >= n {
				break
			}
		}

		iteration--
		prefixIndex++
		prefix = results[prefixIndex]
	}

	return results
}
