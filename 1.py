import torch_geometric.datasets as datasets

# 加载ENZYMES数据集
dataset = datasets.TUDataset(root='/tmp/ENZYMES', name='ENZYMES')

# 获取数据集的类别数量和特征数量
num_classes = dataset.num_classes
num_features = dataset.num_features

print("ENZYMES 数据集有 {} 个类别".format(num_classes))
print("ENZYMES 数据集有 {} 个特征".format(num_features))

# 查看第一个图的基本信息
data = dataset[200]
print(data)
