# DICTIONARY ITERATION


digits = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹"
}


# Print keys
for key in digits:
    print(key)


# Print values
for value in digits.values():
    print(value)


# Print items
for item in digits.items():
    print(item)


# Print key and value
for key, value in digits.items():
    print(f"Key: {key}  Value: {value}")
