bool isValid(char* s) {
    char stck[100000];
    int i,top=-1;
    for(i=0;s[i]!='\0';i++){
        if(s[i]=='('|| s[i]=='['|| s[i]=='{')
            stck[++top]=s[i];
        else{
            if(top==-1)
            return false;

            char c=stck[top--];
            if((s[i] ==')' && c !='(' ) ||
            (s[i] ==']' && c !='[' ) ||
            (s[i] =='}' && c !='{'))
            return false; 
        }
    }
    return top ==-1;
}