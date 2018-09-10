rm(list = ls())
attach(iris)

#1.install SQLDf package and
#Select the rows from iris dataset where sepal length > 2.5
#and store that in subiris data frame

library(sqldf)
names(iris) <- c("SepalLength", "SepalWidth",  "PetalLength", "PetalWidth",  "Species")
subiris <- sqldf("select * from iris where SepalLength > 2.5")

#2.Calculate group wise mean from iris data and perform same using R base counterpart aggregation

sqldf("select Species, AVG(SepalLength) as SepalLength, AVG(SepalWidth) as SepalWidth, AVG(PetalLength) as PetalLength, AVG(PetalWidth) as PetalWidth from subiris group by Species")
aggregate(cbind(Sepal.Length,Sepal.Width,Petal.Length,Petal.Width)~Species, subiris, mean)

#3.Create dept dataframe and emp dataframe and perform inner , leftouter,RightOuter and
#FullOuter Joins using SQLDF

dept <- data.frame(did=c(10,20,30,40,50),
                   dname=c("Accounting","Research","Sales","Operations","HR"),
                   loc=c("New York","Dallas","Boston","Chocago","Boston"))

emp <- data.frame(eno=c(7541,5861,5589,6639,7458,2236,7483,8784,9698,7485,4466),
                  ename=c("Allen","Steve","James","Martin","Alex","Turner","Miller","Scott","Blake","Clark","Neil"),
                  job=c("Analyst","CEO","Clerk","Manager","Salesman","Manager","Analyst","Clerk","Salesman","Salesman","Security"),
                  mgrid=c(6639,NA,6639,2236,6639,6639,2236,6639,2236,6639,2236),
                  did=c(30,40,20,10,30,10,20,20,10,30,60))

#inner
sqldf("select dept.*, emp.* from dept inner join emp on dept.did = emp.did")              
#leftouter
sqldf("select dept.*, emp.* from dept left outer join emp on dept.did = emp.did")               
#rightouter (edited to overcome "RIGHT and FULL OUTER JOINs are not currently supported" error)
sqldf("select dept.*, emp.* from emp left outer join dept on dept.did = emp.did")              
#fullouter  (edited to overcome "RIGHT and FULL OUTER JOINs are not currently supported" error)
sqldf("select dept.*, emp.* from dept left outer join emp on dept.did = emp.did union select * from emp left outer join dept on dept.did = emp.did")


#4.Perform above exercise using dplyr package functions

library(dplyr)
subiris %>% group_by(Species) %>% summarise(SepalLength=mean(SepalLength), SepalWidth=mean(SepalWidth), PetalLength=mean(PetalLength), PetalWidth=mean(PetalWidth))

dept %>% inner_join(emp)
dept %>% left_join(emp)
dept %>% right_join(emp)
dept %>% full_join(emp)

#5.Perform above exercises using dataframe operations

merge(dept, emp, by = "did")
merge(dept, emp, by = "did", all = TRUE)
merge(dept, emp, by = "did", all.x = TRUE)
merge(dept, emp, by = "did", all.y = TRUE)


