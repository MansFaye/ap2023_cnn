"""Main python script, used to build the model from scratch
"""

import scripts.preprocessing as preprocessing
import scripts.training as train
import scripts.visualization as visu
import torch

# Load the data, transform it
batch_size = 32

train_data, test_data, train_loader, test_loader = preprocessing.load(batch_size, 8)


# Checking dataset size and visualizing a few images
preprocessing.data_check(train_data, test_data, train_loader)

# Create CNN
net = train.CNN()

print('The model:')
print(net)

# train model
epochs = 20
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

train_loss, test_loss, train_acc, test_acc = train.train(net, train_loader, test_loader, epochs, device)

# Visualize loss and accuracy
visu.loss_acc_plot(train_loss, test_loss, train_acc, test_acc, epochs)
