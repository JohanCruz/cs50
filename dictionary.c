/**
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include "dictionary.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
typedef struct sllist
             { bool data;
               struct sllist* next[27]; 
             } sllnode;

     
sllnode* head = NULL;   sllnode* nnode= NULL; sllnode* position= NULL; sllnode* datas[1000000];
int ncount=0; int count=0; char bf; int bfb; 


     
bool load(const char* dictionary)
{           for( int in=-1; in<1000000; in++)
               {datas[in] = NULL;
               } 
                  
            nnode = malloc(sizeof(sllnode));  //  nnode->data = 1;
            head=nnode;
            //nnode = malloc(sizeof(sllnode)); 
               for(int i=-1;i<27; i++)
               { nnode->next[i] = NULL; 
               } //  inicializa en null los punteros del nodo
            
            //if(head->next[0]==NULL){printf("la cosa si era nula.\n");}
            //head->next[0]=nnode;  // apunta al primer puntero al del primer nodo al segundo nodo
            //nnode->data = 0; //pone cero en el dato del nodo
            // printf("%d.\n",head->data); printf("%d.\n",nnode->data); visualiza el dato del nodo
            // free(nnode);  nnode=head; free(nnode); //free(head); // libera la memoria de dos nodos
            position=nnode;
            
            
            // TODO
            FILE* inptr = fopen(dictionary, "r");
            fread(&bf, sizeof(char), 1, inptr);
                        for (int i=0; !feof(inptr);i++)
                        {  bfb=(int)bf-97;  //printf("bfb: %d. bf: %c. \n",bfb, bf);
                            
                    
                             if(((0<=bfb)&&(bfb<=25))) 
                              {  if ((position->next[bfb])==NULL)
                                    {
                                      nnode = malloc(sizeof(sllnode));
                                      position->next[bfb]=nnode;
                                      for(int i=-1;i<27; i++)
                                      { nnode->next[i] = NULL;
                                          
                                      }
                                      
                                      position=nnode;
                                      position->data=0;
                                      datas[count]=nnode; count++;
                                     
                                    }
                                    else{ 
                                              if (((0<=bfb)&&(bfb<=25))&&((position->next[bfb])!=NULL))
                                             {
                                                 
                                         position=position->next[bfb]; //printf("una letra en esa posicion .\n");
                                             }
                                            }
                                    
                              }
                              else{            
                                        if(bf=='\n')
                                        { position->data=1;
                                          //printf(" enter .\n");
                                          ncount++;
                                          position=head;        // pone indicador de fin de palabra y redirecciona a la cabeza
                                                                   //printf("enter. \n"); 
                                        } 
                                        
                                        if(bfb==-58&&position->next[26]==NULL)
                                              { nnode = malloc(sizeof(sllnode));
                                              position->next[26]=nnode;
                                                for(int i=-1;i<27; i++)
                                                {nnode->next[i] = NULL;
                                                }
                                                
                                                position=nnode;
                                                position->data=0;
                                                datas[count]=nnode; count++;
                                              }
                                              
                                        if ((bfb==-58)&&((position->next[26])!=NULL))
                                             {
                                         position=position->next[26]; //printf("una letra en esa posicion .\n");
                                             }
                                
                                 }   
                                                      
                                                                   
                                                    
                                                          
                                           /* if(bfb==39&&position->next[26]!=NULL){      //no se va a repetir nunca
                                                position=position->next[26];
                                                
                                            }*/
                                                        
                                     
                                          
                                             
                                                             
                                                                        
                                                                   
                                                               
                                  
                                            
                                          
                                            
                        fread(&bf, sizeof(char), 1, inptr);   
                        }
            
            //printf("%d.\n\n\n\n\n",count);
        
            
            //for(int n=0;n<100;n++){  // printf("%c",bf);     fread(&bf, sizeof(char), 1, inptr);     }
            
            fclose(inptr);
                    
            return true; //false;
            
            
            
            
            
}








/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{    // TODO
    return ncount;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{  
   for(count++;count!=-1;count--)
   {
     free(datas[count]);  //count--;
    }
free(head);
return true;
}

/**
 * Returns true if word is in dictionary else false.
 */
int j;
bool check(const char* word)
{    
    for( j=0;word[j]!='\0';j++){}
    j--;
    //printf("tamaño %d.\n",j); 
    // TODO

    position=head;
    
     int res=0;
    
    for(int i=0;i<=j;i++)
    {    res=(int)tolower(word[i])-97; 
        //printf(" word[i] +%c+",word[i]); 
        if(res>=0&&res<=122)
          {
                                 if(position->next[res]!=NULL)
                                    { position=position->next[res];
                                        // 
                                        if(position->data==1)
                                                {//printf("data "); 
                                                
                                                }
                                    }
                                        else 
                                        { //printf(".  %c  .%d.",word[i],(int)tolower(word[i])-97);
                                            return false; 
                                        }
          }
          else {if(res==-58) 
                  {
                        
                                     if(position->next[26]!=NULL)
                                       {position=position->next[26];
                                       // printf(".  %c  .%d.",word[i],(int)tolower(word[26]));
                                        }
                                        else { 
                                            //printf(".  %c  .%d.",word[i],(int)tolower(word[26]));
                                            return false;
                                        }
                                     
                  }
               }
          
          
    }

if(position->data==1)
{//printf("data "); 
return true;
}
/*    
if(position->data==1)
{return true;  

}else {
  return false;  
}
*/
return false;
    
}
