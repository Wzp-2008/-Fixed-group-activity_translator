import sys
sys.setrecursionlimit(1000000)
def invert_dict(d):
    return {v: k for k, v in d.items()}
e = {"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16","Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24","Y":"25","Z":"26"," ":"27",",":"28",".":"29","?":"30"}
d = invert_dict(e)
def ei(content):
    #加密
    e_content = ""
    content = content.upper()
    for i in content:
        e_content += e[i]
        e_content += " "
    return e_content
def di(content):
    #解密
    content = content.split(" ")
    d_content = ""
    for i in content:
        d_content += d[i]
    return d_content    
