# -*- coding: utf-8 -*-
#reference: http://pytorch.org/tutorials/beginner/pytorch_with_examples.html
import torch
import numpy as np
import matplotlib.pyplot as plt

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 629, 1, 10, 1

x1 = torch.range(-3.14, 3.14, 0.01)
x = torch.unsqueeze(x1, 1)

#plot true function data
y = torch.cos(x)
plt.plot(x, y, 'C1', label="true function data")

# define the model with tanh()
model = torch.nn.Sequential(
	torch.nn.Linear(D_in, H),
    torch.nn.Tanh(),
    torch.nn.Linear(H, D_out),
)
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4
#plot original data before training
plt.plot(x, model(x).detach().numpy(), 'C3', label="data before training")
for t in range(500):
    y_pred = model(x)
    #loss
    loss = loss_fn(y_pred, y)
    model.zero_grad()
    loss.backward()

    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad

#plot final data after training
plt.plot(x, y_pred.detach().numpy(), 'C2', label="data after training")
plt.legend()
plt.show()