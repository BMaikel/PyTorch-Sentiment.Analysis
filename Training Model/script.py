import numpy as np
import pandas as pd

import torch
from torch.utils.data import random_split, TensorDataset, DataLoader

from sklearn.preprocessing import LabelEncoder

def read(path): #Read and clean.
    data = pd.read_csv(path)
    data = data.drop(data.columns[0], axis=1)
    data = data.drop_duplicates()
    return data

def status_target(status, label_encoder = LabelEncoder()):
  labels = label_encoder.fit_transform(status)
  return torch.tensor(labels, dtype=torch.long)

def df_to_Dataset(ids, masks, labels):
    return TensorDataset(torch.tensor(ids, dtype=torch.long),
                         torch.tensor(masks, dtype=torch.long),
                         status_target(labels))

def split_data(data, train, val, test, shuffle, batch_size):
  train_size = int(train * len(data))
  val_size = int(val * len(data))
  test_size = len(data) - train_size - val_size

  train_dataset, val_dataset, test_dataset = random_split(data, [train_size, val_size, test_size])

  train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=shuffle)
  val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=shuffle)
  test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=shuffle)
    
  return train_dataloader, val_dataloader, test_dataloader