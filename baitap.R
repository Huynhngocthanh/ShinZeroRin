# Bài 1
# k???t qu??? 12
answer1 <- 0
for (j in 3:5){ answer1 <- j+answer1 }
answer1
# K???t qu??? 22
answer2 <- 10
for (j in 3:5){ answer2 <- j+answer2 }
answer2
# k???t qu??? 600
answer3 <- 10
for (j in 3:5){ answer3 <- j*answer3 }
answer3

# Bài 2
n = prod(3:5, start = 10)
n

# Bài 3
tong1 <- 0
for (j in 1:100){ tong1 <- j+tong1 }
tong1

tong2 <- 0
n <- 100
i <- 1
while (i<= n){
  tong2 <- tong2 + i
  i <- i + 1
}
tong2

sum(1:100)

# Bài 4
tich1 <- 1
for (j in 1:50){ tich1 <- j*tich1 }
tich1

tich2 = prod(1:50, start = 1)
tich2

# Bài 5
bk <- 3:20
tt <- (4*(bk**3))/3
frame <- data.frame(bankinh = bk, thetich = tt)
frame

#Bài 6
is.ordered(frame)
sapply(frame, is.factor)
sapply(frame, factor)
sapply(frame, sum)
sapply(frame, mean)
sapply(frame, levels)
