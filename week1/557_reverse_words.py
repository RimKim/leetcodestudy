# https://leetcode.com/problems/reverse-words-in-a-string-iii/
def reverse_words(s: str) -> str:
    reversed_list = [s[::-1] for s in s.split()]
    return " ".join(reversed_list)


if __name__ == "__main__":
    assert reverse_words("Let's take Leetcode contest"), "s'teL ekat edoCteeL tsetnoc"
    assert reverse_words("God Ding"), "doG gniD"
