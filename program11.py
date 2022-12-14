#string concatenation is the way of combining two strings

#exapmle 1
# var1 = "consistency"
# var2 = "is the key"

# #
# print(f"{var1} {var2}")

#using the + operator
var4 = "bitches come and go brah"
var5 = "but u know i stay"
var3 = var4 + var5
print(var3)


#using the join operator
print (" ".join([var4, var5]))

#using the format operator
print("{} {}".format(var3,var4))

#using % method
print("%s %s"% (var4,var5))