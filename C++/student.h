#ifndef student.h
#define student.h

class student{
	string Name, Roll;
	string Subjects [4];

public:
	student();
	~student();
	student(string Name, string Roll, string Subjects[]);
	student(student s);
};


#endif