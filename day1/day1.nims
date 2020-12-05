import strutils, sequtils

const lines = readFile("input.txt").strip.splitLines.map(parseInt)

func solve1(lines: seq[int]): int =
    for line1 in lines:
        for line2 in lines:
            if (line1 + line2) == 2020:
                return line1 * line2
    return 0


func solve2(lines: seq[int]): int =
    for line1 in lines:
        for line2 in lines:
            for line3 in lines:
                if (line1 + line2 + line3) == 2020:
                    return line1 * line2 * line3
    return 0

echo "Solve 1 :", solve1(lines)
echo "Solve 2 :", solve2(lines)
