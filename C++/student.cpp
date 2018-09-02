#include <student.h>

student::student(){
	Name = Roll = Subjects[0] = Subjects[1] Subjects[2] Subjects[3] = "";
}

student::student(string Name, string Roll, string Subjects[]){
	this.Name = Name;
	this.Roll = Roll;
	this.Subjects[0] = Subjects[0];
	this.Subjects[1] = Subjects[1];
	this.Subjects[2] = Subjects[2];
	this.Subjects[3] = Subjects[3];
}

student::student(student s){
	ths.Name = s.Name;
	this.Roll = s.Roll;
	this.Subjects[0] = s.Subjects[0];
	this.Subjects[1] = s.Subjects[1];
	this.Subjects[2] = s.Subjects[2];
	this.Subjects[3] = s.Subjects[3];
}