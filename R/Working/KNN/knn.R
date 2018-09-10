rm(list = ls())
library(ggbiplot)
library(pca3d)
library(class)
library(gmodels)

#Data Reading
data = read.csv("wisc_bc_data.csv", header = TRUE)
data = data[-1]
str(data)

#Normalization
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x))) 
}

#PCA
#pca3d(princomp(data[,c(2:31)]), group = data$diagnosis)
#ggbiplot(princomp(data[,c(2:31)]), groups = data$diagnosis, varname.size = 0)

#Nomalization
data_n = as.data.frame(lapply(data[2:31], normalize))
summary(data)

#Divide Train, Test
N_sample = 100
s_index = sample(1:569, N_sample)
data_Train = data_n[-s_index,]
data_Test = data_n[s_index,]

#KNN
N_K = 25
data_knn = knn(train = data_Train, test = data_Test, cl = data[-s_index, 1], k = N_K)

CrossTable(x = data[s_index,1], data_knn)