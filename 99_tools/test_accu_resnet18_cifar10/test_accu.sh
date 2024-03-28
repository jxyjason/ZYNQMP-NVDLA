#!/bin/bash

# 循环读取图片并打印结果
for i in {0..9999}; do
    image_file="/mnt/sdb3/img/test_$i.jpg"
    ./nvdla_runtime --loadable /mnt/sdb3/nvdla_loadables-master/resnet18-cifar10-caffe/loadables/fast-math.nvdla --image "$image_file" --rawdump > /dev/null

    # 打印 output.dimg 的内容
    output_file="output.dimg"
    cat "$output_file"
    echo ""
done
