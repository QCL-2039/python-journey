var1 = var2 = True
var3 = var4 = var5 = False
result1 = result2 = result3 = True
result4 = result5 = False

var1 = 4 > 3 - 1
var2 = False and var1
var3 = True
var4 = False
var5 = not (var3 or var4)

result1 = (var1 or var2) and (8 * 10 > 45)
result2 = (var1 or var2) and (result1 and False)
result3 = (var1 and not result1) or result2
result4 = (var1 or var2) or not ((var5 and var1) and False)
result5 = (not var1 and var4) and (result3 or var3)
