import torch
import torchvision
import os

# 创建保存图像和标签的文件夹
os.makedirs('img', exist_ok=True)

# 加载CIFAR-10测试集数据
transform = torchvision.transforms.ToTensor()
test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle=False)

# 创建保存标签的文本文件
labels_file = open('labels.txt', 'w')

# 遍历测试集数据并保存为图像和标签
for i, (image, target) in enumerate(test_loader):
    # 生成文件名
    filename = f'img/test_{i}.jpg'
    # 保存图像
    torchvision.utils.save_image(image, filename)

    # 保存标签到文本文件
    label = str(target.item())
    labels_file.write(f' {label}\n')

    print(f'Saved {filename} with label: {label}')

# 关闭标签文件
labels_file.close()

print('Image and label saving complete.')