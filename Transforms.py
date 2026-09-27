from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

# python的用法 - > Tensor 数据类型

# 2.为什么需要Tensor类型


img_path = "hymenoptera_data/train/ants/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

# 1.Transforms如何使用
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

print(tensor_img)

writer.add_image("Tensor_img", tensor_img, 0)

writer.close()


