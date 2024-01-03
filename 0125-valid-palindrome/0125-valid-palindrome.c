bool isPalindrome(char* s) {
    if (s == NULL) {
        return false;
    }

    char* palindrome = (char *)malloc((sizeof(char))*strlen(s));
    char* pslow = palindrome;
    
    while(*s) {
        if(isalnum(*s)) {
            *palindrome = tolower(*s);
            *palindrome++;
        }
        *s++;
    }
    
    while(pslow < --palindrome) {
        // find next character for the pointers

        if(*pslow != *palindrome) {
            return false;
        }
        *pslow++;
    }
    
    return true;
}