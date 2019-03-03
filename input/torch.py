import os; os.environ['OMP_NUM_THREADS'] = '4'
import torch
import torch.nn as nn

def fcnn(x_train,y_train,x_test,y_test):
    # Device configuration
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model_path="fcnn.model"
    # Hyper-parameters
    input_size = 784
    hidden_size = 500
    num_classes = 10
    num_epochs = 5
    learning_rate = 0.1


    # Fully connected neural network with one hidden layer
    class NeuralNet(nn.Module):
        def __init__(self):
            super(NeuralNet, self).__init__()
            self.model = nn.Sequential( nn.Linear(30, 40),
                nn.Linear(input_size, 1024),
                nn.ReLU(),
                nn.Linear(1024, 64),
                nn.ReLU(),
                nn.Linear(1024, 64),
                nn.ReLU(),
                nn.Linear(64, 1))

        def forward(self, x):
            # out = self.fc1(x)
            # out = self.relu(out)
            # out = self.fc2(out)
            # return out
            return self.model(x)

    model = NeuralNet(input_size, hidden_size, num_classes).to(device)
    # Loss and optimizer
    loss_func = torch.nn.MSELoss()      # 预测值和真实值的误差计算公式 (均方差)
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  # 传入 net 的所有参数, 学习率

    if not os.path.exists(model_path):
        # Train the model
        for epoch in range(num_epochs):
            out = model(x_train)  # 喂给 net 训练数据 x, 每迭代一步，输出预测值
            loss = loss_func(out, y_train)  # 计算两者的误差
            optimizer.zero_grad()   # 清空上一步的残余更新参数值
            loss.backward()         # 误差反向传播, 计算参数更新值
            optimizer.step()        # 将参数更新值施加到 net 的 parameters 上
            if epoch % 100 == 0:
                print('Epoch [{}/{}]  Loss: {:.4f}'  .format(epoch , num_epochs, loss.item()))
                print(datetime.datetime.now())

                # Save the model checkpoint
        torch.save(model.state_dict(), 'model.ckpt')
    else:
        model.load_state_dict(torch.load(model_path))
        model.eval()

    #模型預測
    y_predicted = model(torch.from_numpy(x_test)).detach().numpy()
    return y_predicted

