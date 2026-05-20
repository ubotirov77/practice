# ==================================== MIT TASK with PYTHON ==============================================
#                                       ✨O-TASK (PYTHON)
# ========================================================================================================
#  Shunday function yozing, u har xil valuelardan iborat
#  array qabul qilsin va List ichidagi sonlar
#  yigindisini hisoblab chiqqan javobni qaytarsin.
#  MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45
# ========================================================================================================
# ✨ MASALANI YECHIMI:

def calculate_summary(arr):
    total = 0

    for item in arr:
        if type(item) == int:
            total += item

    return total


result = calculate_summary([34, "10", {"son": 10}, True, 100])
print("result:", result)

# ==================================== MIT TASK with PYTHON ==============================================
#                                       ✨M-TASK (PYTHON)
# ========================================================================================================
#   Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham,
#   orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
#   MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;
# ========================================================================================================
# ✨ MASALANI YECHIMI:


# def is_palindrome(text):
#     reversed_text = text[::-1]

#     if reversed_text.lower() == text.lower():
#         return True
#     else:
#         return False


# print(is_palindrome("Madam"))
# print(is_palindrome("Norman"))


# ==================================== MIT TASK with PYTHON ==============================================
#                                       ✨k-TASK (PYTHON)
# ========================================================================================================
#   Shunday function yozing, u string qabul qilsin
#   va string ichidagi eng uzun sozni qaytarsin.
#   MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
# ========================================================================================================
# ✨ MASALANI YECHIMI:
# def find_longest(text):
#     words = text.split()

#     def get_highest_index(words):
#         return words.index(max(words, key=len))

#     index = get_highest_index(words)

#     return words[index]


# print(find_longest("I come from Uzbekistan"))


# ==================================== MIT TASK with PYTHON ==============================================
#                                       ✨I-TASK (PYTHON)
# ========================================================================================================
#   Shunday function tuzing, unga string argument pass bolsin.
#   Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
#   MASALAN: get_digits("m14i1t") return qiladi "141"
# ========================================================================================================
# ✨ MASALANI YECHIMI:


# def get_digits(arr):
#     result = []
#     for value in arr:
#         if value.isdigit():
#             result.append(value)
#     return ''.join(result)


# result = get_digits("m010rt84r14l68d6d1")
# print("The digits in the string are:", result)


# ========================================================================================================
#                                     ✨G-TASK (PYTHON)
# ========================================================================================================
# Shunday function tuzingki unga integerlardan iborat array pass bolsin
# va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# ========================================================================================================
# ✨ MASALANI YECHIMI:
# lambda funtion
# def get_highest_index(arr): return arr.index(max(arr))


# result = get_highest_index([5, 21, 12, 21, 8])
# print("The highest number is at index", result)
