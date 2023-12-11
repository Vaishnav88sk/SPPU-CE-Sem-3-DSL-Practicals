#include <iostream>
using namespace std;
#define size 10

class braces
{
    int top;
    char stk[size];
public:
    braces()
    {
     top=-1;
    }
    void push(char);
    char pop();
    int isfull();
    int isempty();
    void check();
};

void braces::push(char x)
{
    top=top+1;
    stk[top]=x;
}

char braces::pop()
{
    char s;
    s=stk[top];
    top=top-1;
    return s;
}

int braces::isfull()
{
    if(top==size)
        return 1;
    else
        return 0;
}

int braces::isempty()
{
    if(top==-1)
        return 1;
    else
        return 0;
}

void braces::check(){
    int i=0;
    int res;
    char exp[20];
    cout<<"\nEnter the expression to check whether it is in well or not :  ";
    cin>>exp;
    if((exp[0]==')')||(exp[0]==']')||(exp[0]=='}'))
    {
        cout<<"\n Invalid Expression.....\n";
    }
    else
    {
        while(exp[i]!='\0'){
            if(exp[i]=='(' || exp[i]=='{' || exp[i]=='['){
                top++;
                stk[top]=exp[i];
            }
            else if((exp[i]==']'&&exp[top]=='[') || (exp[i]=='}'&&exp[top]=='{') || (exp[i]==')'&&exp[top]=='(')){
                top--;
            }else if((exp[i]==']' || exp[i]=='}' || exp[i]==')') && top ==-1){
                res = 1;
            }
            else{
                break;
            }
            i++;
        }
        if(res==1){
            cout<<"Invalid Expression!"<<endl;

        }else if (top==-1){
            cout<<"Expression is Valid!"<<endl;
        }else{
            cout<<"Expression is Invalid!"<<endl;
        }
    }


}

int main()
{
    braces s1;
    s1.check();
    return 0;
}