setwd("Desktop/TopGearTemp/R/Working/pima_indians_diabetes_study/")

rm(list = ls())
data = read.csv("Pima Indians Diabetes Binary Classification dataset.csv")

## Split into Testing and Training Data
sample_i = sample(768, 100)
data_train = data[-sample_i,]
data_test = data[sample_i,]

## Model Training
model = glm(Class.variable..0.or.1. ~ ., data = data_train, family = binomial)

## Model Testing
predict = ifelse(predict(model, data_test,type = "response") > 0.5, 1, 0)
error = mean(predict != data_test$Class.variable..0.or.1.)
accuracy = 1 - error

table(predict, data_test$Class.variable..0.or.1.)

