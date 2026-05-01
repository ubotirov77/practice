# ==================================== MIT TASK with PYTHON ==============================================
#                                     ✨G-TASK (PYTHON)
# ========================================================================================================
# Shunday function tuzingki unga integerlardan iborat array pass bolsin
# va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# ========================================================================================================
# ✨ MASALANI YECHIMI:
# lambda funtion
def get_highest_index(arr): return arr.index(max(arr))


result = get_highest_index([5, 21, 12, 21, 8])
print("The highest number is at index", result)
