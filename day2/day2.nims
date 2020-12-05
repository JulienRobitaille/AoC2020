import strutils, sequtils

const passwords = readFile("input.txt").strip.splitLines


func solve(passwords: seq[string]): tuple[firstCount: int, secondCount: int] =
    var validCount1 = 0
    var validCount2 = 0

    for password in passwords:
        let metadata = password.split(" ")
        let startEnd = metadata[0].split("-").map(parseInt)
        let start = startEnd[0]
        let eend = startEnd[1]

        let letter = metadata[1][0]
        let a = metadata[2][start - 1]
        let b = metadata[2][eend - 1]
        let amount = metadata[2].count(letter)

        if start <= amount and eend >= amount:
            validCount1 = validCount1 + 1

        if (a == letter) xor (b == letter):
            validCount2 = validCount2 + 1
    return (validCount1, validCount2)

echo "Solve 1 :", solve(passwords)[0]
echo "Solve 2 :", solve(passwords)[1]
