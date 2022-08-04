// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.
// Package bob should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
// Bob answers 'Sure.' if you ask him a question, such as "How are you?".
// Any string that ends in a ?
// He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
// Any string all in caps
// He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
// Any string in all caps ending in a ?
// He says 'Fine. Be that way!' if you address him without actually saying anything.
// Any blank strings
// He answers 'Whatever.' to anything else.
// Default = whatever
package bob

import (
	// "regexp"
	"strings"
	"unicode"
)

func containsLetter(remark string) bool {
	for _, v := range remark {
		if unicode.IsLetter(v) {
			return true
		}
	}
	return false
}

// Hey should have a comment documenting it.
func Hey(remark string) string {
	greeting := strings.TrimSpace(remark)
	switch {
	case len(greeting) == 0:
		return "Fine. Be that way!"
	case containsLetter(remark) && strings.ToUpper(greeting) == greeting && greeting[len(greeting)-1] == '?':
		return "Calm down, I know what I'm doing!"
	case greeting[len(greeting)-1] == '?':
		return "Sure."
	case containsLetter(remark) && strings.ToUpper(greeting) == greeting:
		return "Whoa, chill out!"
	default:
		return "Whatever."
	}
}
