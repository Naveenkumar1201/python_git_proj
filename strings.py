res = var.startswith(substr)
res = var.endswith(substr)

var = "india is great"

res = var.startswith('INDIA')
print(res)

res = var.endswith("eat")
print(res)

#################################################

# var = "santhosh#560100#bangalore#japan"
#
# res = var.split('#')
# print(res)
#
# data = ['A', 'B', 'C', 'D', 'E']
# res = "_".join(data)
# print(res)

# var = "hi san hello san bye san"
#
# res = var.count("o")
# print(res)
#
# var = "######santhosh ##### india###############"
#
# res = var.lstrip("#")
# print(res)
#
# res = var.rstrip('#')
# print(res)
#
# res = var.strip("#")
# print(res)
#
# res = var.replace("#", "")
# print(res)


var = "nandhini"
res = var.isalpha()
print(res)

var = "9986019197abc"
res = var.isdigit()
print(res)


res = var.isalnum()

res = var.isupper()

res = var.islower()

res = var.isspace()











































