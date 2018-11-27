//Understanding AVL tree via its movements

#include<stdio.h>
#include<stdlib.h>
struct tree{
    struct node* root;
};
struct node{
    int data;
    struct node* l;
    struct node* r;
};
struct node * newnode(int data){
    struct node* tmp = (struct node*)(malloc(sizeof(struct node)));
    tmp->data=data;
    tmp->l=NULL;
    tmp->r=NULL;
    return tmp;
}
int height(struct node *n){
    int lh=0,rh=0;
    if(!n)
        return 0;
    if(n->l)
        lh=height(n->l);
    if(n->r)
        rh=height(n->r);
    return (lh>rh?lh:rh)+1;
}
struct node* rot_l(struct node* n){
    if(!(n->r))
        return n;
/*
        n                         nr
    nl      nr       =>         n
                            nl
*/
    printf("rotating left");
    struct node* nr=n->r;
    n->r = nr->l;
    nr->l = n;
    return nr;
}
struct node* rot_r(struct node* n){
    if(!(n->l))
        return n;
/*
        n               nl
    nl      nr      =>      n
                                nr
*/
    printf("\n rotating right");
    struct node* nl=n->l;
    n->l = nl->r;
    nl->r = n;
    return nl;
}
struct node* avl_check(struct node* n){
    int lh=height(n->l), rh=height(n->r);
    if (lh-rh>1)
        return rot_r(n);
    if (lh-rh<-1)
        return rot_l(n);
    return n;
}
struct node* search_and_insert(struct node* n, int data){
    if(data < n->data){
        printf("->l");
        if(n->l)
            n->l = search_and_insert(n->l,data);
        else
            n->l =newnode(data);
    }
    else{
        printf("->r");
        if(n->r)
            n->r = search_and_insert(n->r,data);
        else
            n->r=newnode(data);

    }
    return avl_check(n);
}
void insert_data(struct tree* t, int data){
    if(t->root){
        printf("current root : %d\n",t->root->data);
        t->root = search_and_insert(t->root,data);

    }
    else{
        printf("no root\n");
        t->root=newnode(data);
        printf("%d",t->root->data);

    }
}

void _preorder(struct node* n){
    if(n)
        printf(" %d ",n->data);
    if(n->l){
        printf("L");
        _preorder(n->l);
    }
    if(n->r){
        printf("R");
        _preorder(n->r);
    }
    printf("U");
}
void _inorder(struct node* n){
    if(n->l){
        printf("L");
        _inorder(n->l);
    }
    if(n)
        printf(" %d ",n->data);
    if(n->r){
        printf("R");
        _inorder(n->r);
    }
    printf("U");
}
void _postorder(struct node* n){
    if(n->l){
        printf("L");
        _postorder(n->l);
    }
    if(n)
        printf(" %d ",n->data);
    if(n->r){
        printf("R");
        _postorder(n->r);
    }
    printf("U");
}
void preorder(struct tree* t){
    printf("\nPre Order Travesal\n");
    printf("==================\n");
    _preorder(t->root);
}
void inorder(struct tree* t){
    printf("\nIn Order Traversal\n");
    printf("==================\n");
    _inorder(t->root);
}
void postorder(struct tree* t){
    printf("\nPost Order Traversal\n");
    printf("====================\n");
    _postorder(t->root);
}
int main(){
    int data[]={9,8,7,6,5,4,3,2,1,0},i;
    struct tree* t = (struct tree*)(malloc)(sizeof(sizeof(struct tree)));
    t->root=NULL;
    for(i=0;i<sizeof(data)/sizeof(int);i++){
        printf("\nInserting %d...\n",data[i]);
        insert_data(t,data[i]);
    }
    printf("\n\n");
    preorder(t);
    inorder(t);
    postorder(t);
    printf("\nheight :%d\n",height(t->root));
}


