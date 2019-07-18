import os
import sys


path = "/Users/xushengfu/Desktop/SunmiAppStore_v5.2.1_p_pro_tes.apk"
print  (os.path.dirname(path))
tmp_path=os.path.dirname(path)
path1 = tmp_path+"/ES_ids.txt"
path2 = tmp_path+"/ES_res.txt"
path3 = tmp_path+"/ES_local.txt"
path31 = tmp_path+"/ES_locals.txt"
path4 = tmp_path+"/ES_res_p.txt"
path5 = tmp_path+"/ES_locals_p.txt"
path7 = tmp_path+"/ES_locals_result.txt"
path8 = tmp_path+"/ES_locals_result111.txt"
os.system(
    "/Users/xushengfu/Library/Android/sdk/build-tools/26.0.2/aapt dump xmltree " + path + " AndroidManifest.xml | grep 'android:label' >" + path1)
os.system(
    "/Users/xushengfu/Library/Android/sdk/build-tools/26.0.2/aapt dump --include-meta-data badging " + path + " | grep -E 'application-label' >" + path3)
os.system(
    "/Users/xushengfu/Library/Android/sdk/build-tools/26.0.2/aapt dump --include-meta-data badging " + path + " | grep 'locales' >" + path31)

fids = open(path1)
lines = fids.readlines()
ids = lines[0].split('=')[1]
id = ids[1:ids.__len__() - 1]
print (id)

os.system(
    "/Users/xushengfu/Library/Android/sdk/build-tools/26.0.2/aapt dump resources " + path + " | grep -E '" + id + "|^\s*config' >" + path2)
fids.close()

os.system("grep -B 1 " + id + " " + path2 + " >" + path4)
os.system("grep 'config' " + path4 + " >" + path5)

localsidos = []
with open(path5, 'r') as file_to_read:
    while True:
        line = file_to_read.readline()
        if not line:
            break
            pass
        e_tmp = line.split()[1]
        E_tmp = e_tmp[0:e_tmp.__len__() - 1]
        localsidos.append(E_tmp.split('-')[0])
        pass
pass
print ("localsidos=")
print (localsidos)
#
# localsid = []
# with open(path6, 'r') as file_to_read:
#     while True:
#         line = file_to_read.readline()
#         if not line:
#             break
#             pass
#         e_tmp = line.split()[1]
#         E_tmp = e_tmp[0:e_tmp.__len__() - 1]
#         localsid.append(E_tmp)
#         pass
# pass
# print ("localsid=")
# print (localsid)

localsids =[]
with open(path31, 'r') as file_to_read:
    while True:
        line = file_to_read.readline()
        if not line:
            break
            pass
        localsids = line.split(':')[1].split()
        pass
pass
print ("localsids=")
print (localsids)



results =set()
for i in localsids:
    for y in localsidos:
        if i.__contains__(y):
            results.add(y)


print("----END---")
print(results)

if results.__sizeof__()==1:
    print("----END111---")

file7=open(path7,"a")
for i in results:
    file7.write("application-label-"+i)
    file7.write("|")
file7.close()

os.remove(path1)
os.remove(path2)
os.remove(path31)
os.remove(path4)
os.remove(path5)



file8=open(path7, 'r')
resultss=file8.readline()
re=resultss[0:resultss.__len__()-1]
print ("re=")
print (re)

os.system("grep  -E '"+ re+"' " + path3 + " >" + path2)
os.remove(path3)
os.remove(path7)
# os.system("grep '-label-ca' " +   + " >" + path7)
# os.system("grep 'application-label-" + localsid[0] + "' " + path3 + " >" + path7)
