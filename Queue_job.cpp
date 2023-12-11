#include <iostream>
using namespace std;
const int MAX=10;
class Queue
{
int data[MAX];
int front,rear;
public:
Queue()
{
front=rear=-1;
}
void enqueue(int);
void dequeue();
int isFull();
int isEmpty();
void display();
};
int Queue::isFull()
{
if(rear==MAX-1)
return 1;
else
return 0;
}
int Queue::isEmpty()
{
if(rear==-1||front==rear+1)
return 1;
else
return 0;
}
void Queue::enqueue(int id)
{
if(isFull())
{
cout<<"\nCan't add ! Queue is Full !";
}
else
{
if(rear==-1)
{
front++;
data[++rear]=id;
cout<<"\nJob added successfully !";
}
else
{
data[++rear]=id;
cout<<"\nJob added successfully !";
}
}
}
void Queue::dequeue()
{
if(isEmpty())
{
cout<<"\nCan't delete ! Queue is Empty !";
}
else
{
front++;
cout<<"\nJob removed successfully !";
}
}
void Queue::display()
{
if(isEmpty())
{
cout<<"Queue is Empty !";
}
else
{
for(int i=front;i<=rear;i++)
cout<<data[i]<<" ";
}
}
int main()
{
int ch,id;
Queue q;
cout<<"\n--------------Job Queue Menu --------------";
cout<<"\n1. Add Job";
cout<<"\n2. Remove Job";
cout<<"\n3. Display Jobs";
cout<<"\n4. Exit";
do
{
cout<<"\nEnter your choice:";
cin>>ch;
switch(ch)
{
case 1:
cout<<"\nEnter Job ID :: ";
cin>>id;
q.enqueue(id);
break;
case 2:
q.dequeue();
break;
case 3:
cout<<"\nJobs in Queue :: ";
q.display();
break;
}
}while(ch!=4);
}