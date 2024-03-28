# 读取 test_accu_output.txt 文件内容
with open('test_accu_output_7157.txt', 'r') as file:
    lines = file.readlines()

# 读取 labels.txt 文件内容
with open('labels.txt', 'r') as file:
    labels = file.readlines()

# 遍历每一行
totalnum = 0
truenum = 0
for i in range(len(lines)):
    # 分割每行的数据
    data = lines[i].split()

    # 将数据转换为浮点数
    data = [float(num) for num in data]

    # 获取最大值和对应位置
    max_value = max(data)
    max_index = data.index(max_value)

    # 获取 labels.txt 中对应行的值
    label = int(labels[i].strip())
    totalnum += 1

    # 比较最大值的位置与 labels.txt 中的值
    if max_index == label:
        print(1)
        truenum+=1
    else:
        print(0)

print(totalnum)
print(truenum)
print(truenum/totalnum)