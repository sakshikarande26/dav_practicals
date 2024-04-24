# Sample dataset with multiple independent variables (predictors) and a dependent variable
data <- data.frame(
  x1 = c(1, 2, 3, 4, 5),
  x2 = c(2, 3, 4, 5, 6),
  y = c(3, 4, 5, 6, 7)
)

# Fit multiple linear regression model
model <- lm(y ~ x1 + x2, data = data)

# Print summary of the model
summary(model)

