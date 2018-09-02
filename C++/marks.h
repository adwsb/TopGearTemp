#ifndef marks.h
#define marks.h

struct submarks{
	char subname[10];
	int internal, external;
};

class marks : private student{
	submarks score[4];

public:
	marks();
	~marks();
	marks(submarks s[]);
	marks(marks m);
};

#endif