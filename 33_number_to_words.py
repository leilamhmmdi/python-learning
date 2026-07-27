# Convert numbers to Persian words
# This program converts a number into its Persian text form.


ones = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}


tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


hundreds = {
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred"
}


levels = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion"
]



# Convert numbers smaller than 1000

def under_1000(number):

    parts = []

    if number >= 100:
        h = number // 100 * 100
        parts.append(hundreds[h])
        number %= 100


    if 10 <= number <= 19:
        parts.append(teens[number])
        number = 0


    elif number >= 20:
        t = number // 10 * 10
        parts.append(tens[t])
        number %= 10


    if 0 < number < 10:
        parts.append(ones[number])


    return " and ".join(parts)



# Convert complete number to words

def number_to_words(number):

    if number == 0:
        return "zero"


    groups = []


    while number:

        groups.append(number % 1000)
        number //= 1000



    result = []


    for i in range(len(groups)-1, -1, -1):

        if groups[i]:

            text = under_1000(groups[i])


            if levels[i]:
                text += " " + levels[i]


            result.append(text)


    return " and ".join(result)



number = int(input("Enter number: "))


print(number_to_words(number))
