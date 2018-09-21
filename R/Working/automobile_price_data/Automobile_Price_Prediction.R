rm(list = ls())
setwd("Desktop/DesktopDocuments/TopGearTemp/R/Working/automobile_price_data/")
data = read.csv("Automobile price data _Raw.csv")

# Replace '?' in the data with NA
data[data == "?"] = NA

na_count_col = as.data.frame(sapply(data, function(y) sum(length(which(is.na(y))))))
na_count_col
# I decieded to remove normalized.losses column as the comumn has 41 missing values 
data = data[,-2]

na_count_row = rowSums(is.na(data))
na_count_row
sum(na_count_row > 0)

# I decieded to remove 12 rows with NA value from the dataset
data = data[complete.cases(data),]

# I need to convert categorical variables to numerical data
factor_columns = which(as.numeric(sapply(data, is.factor)) == 1)
for (i in factor_columns) {
  data[,i] = as.numeric(data[,i])
}
str(data)

# Normalization
scaled.data = as.data.frame(scale(data[,-25]))
scaled.data$price = data$price

# Breaking down to 80% training and 20% testing dataset
samples = sample(1:193, 39)
training = scaled.data[-samples,]
testing = scaled.data[samples,]

# Model Training with LInear regression
# We take all the features into account
features = names(scaled.data)
features = paste(features[!features %in% "price"], collapse = "+")
formula = paste("price ~ ", features, collapse = "+")
formula = as.formula(formula)

library(neuralnet)
NN = neuralnet(formula = formula, hidden = c(20,10,5), linear.output = T, threshold = 0.05, stepmax = 1e+9, data = training)
plot(NN)

# Prediction
predictions = compute(NN, testing[,1:24])

# Error Calculations
# 1.Mean Absolute Error
sum(abs(predictions$net.result - testing$price)) / nrow(testing)
# 2. RMS Error
(sum((predictions$net.result - testing$price)**2) / nrow(testing)) ** 0.5
# 3. Relative Absolute Error
T.bar = sum(testing$price)/nrow(testing)
sum(abs(predictions$net.result - testing$price)) / sum(abs(testing$price - T.bar))
# 4. Relative Squared Error
(sum((predictions$net.result - testing$price)**2) / sum((testing$price - T.bar)**2)) ** 0.5
# Coefficient of Determination
pred.bar = mean(predictions$net.result)
pred.sd = sd(predictions$net.result)
test.bar = mean(testing$price)
test.sd = sd(testing$price)
(sum((predictions$net.result-pred.bar)*(testing$price-test.bar)) / (nrow(testing)*pred.sd*test.sd)) ** 2