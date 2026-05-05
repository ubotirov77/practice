# ==================================== MIT TASK with PYTHON ==============================================
#                                       ✨I-TASK (PYTHON)
# ========================================================================================================
#   Shunday function tuzing, unga string argument pass bolsin.
#   Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
#   MASALAN: get_digits("m14i1t") return qiladi "141"
# ========================================================================================================
# ✨ MASALANI YECHIMI:
def get_digits(arr):
    result = []
    for value in arr:
        if value.isdigit():
            result.append(value)
    return ''.join(result)


result = get_digits("m010rt84r14l68d6d1")
print("The digits in the string are:", result)


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
