#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int n,q,count=0;
    scanf("%d",&n);
    char strings[n][20];
    for(int i=0;i<n;i++){
        scanf("%s",strings[i]);
    }
    scanf("%d",&q);
    char queries[q][20];
    for(int j=0;j<q;j++){
        scanf("%s",queries[j]);
    }
    for(int j=0;j<q;j++){
        for(int i=0;i<n;i++){
            if(strcmp(strings[i],queries[j])==0){
                count++;
            }
        }
        printf("%d\n",count);
        count=0;
    }
    return 0;
}
