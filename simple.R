#IMPLEMENT SIMPLE LINEAR REGRESSION IN R

#sample data
x <- c(1,2,3,4,5)
y <- c(2,5,7,9,8)

#fit linear regression model
model <- lm(y ~ x)

#print summary of the model
summary(model)

#plot the data and regression line
plot(x, y, main="Simple linear regression", xlab= "x", ylab= "y")
abline(model, color="red")
