
library("writexl")set.seed(1)
x = rnorm(n = 237, mean=9344.566, sd=5100)
df = data.frame(data=x)
write_xlsx(df,".\\file name.xlsx")