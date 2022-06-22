#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
	int id;
	struct node* left;
	struct node* right;
} node;

node* root;

node* MakeNode(int num){
	node *p = (node*)malloc(sizeof(node));
	p->id = num;
	p->left=NULL;
	p->right=NULL;
	return p;
}

node* find(node* cur,int id){
	node* p;
	if(cur==NULL) return NULL;
	if(cur->id==id)	return cur;
	p = find(cur->left,id);
	if(p!=NULL) return p;
	p = find(cur->right,id);
	return p;
}

void add(int num){
	int u = num/2;
	node *par = find(root,u);
	if (par->left==NULL){ 
		par->left = MakeNode(num);
		return;
	}
	par->right = MakeNode(num);
}

void Print(node* cur){
	if(cur==NULL) return;
	Print(cur->left);
	printf("%d ",cur->id);
	Print(cur->right);
}

int main(){
	/*root = MakeNode(1);
	for(int i=2;i<=50;i++) add(i);
	Print(root);*/
	char string[] = "7167745CF7456666C74F15667F4674667646761C4441C64764";
	char result[51];
	int index[] = {32, 16, 33, 8, 34, 17, 35, 4, 36, 18, 37, 9, 38, 19, 39, 2, 40, 20, 41, 10, 42, 21, 43, 5, 44, 22, 45, 11, 46, 23, 47, 1, 48, 24, 49, 12, 50, 25, 6, 26, 13, 27, 3, 28, 14, 29, 7, 30, 15, 31};
	for(int i=0;i<50;i++){
		result[index[i]-1] = string[i];
	}
	for(int i=0;i<49;i=i+2) printf("%c%c ",result[i],result[i+1]);
}

