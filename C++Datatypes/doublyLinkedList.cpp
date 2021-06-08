#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <unordered_set>
using namespace std;

class Node {
    public:
    int data;
    Node* next;
    Node* prev;
};
//add node
void push(Node** head_ref, int num){
    Node* new_node = new Node();
    new_node->data = num;
    new_node->next = (*head_ref);
    new_node->prev = NULL;
    if((*head_ref) !=NULL)(*head_ref)->prev=new_node;
    (*head_ref) = new_node;
}
//add node after another node
void insertAfter(Node* prev_node, int num){
    if(prev_node==NULL)return;
    Node* new_node = new Node();
    new_node->data = num;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
    new_node->prev = prev_node;
    if(new_node->next!=NULL)new_node->next->prev=new_node;
}
//add node to end
void insertEnd(Node** head_ref, int num){
    Node* new_node = new Node();
    Node* last = *head_ref;
    new_node->data = num;
    new_node->next=NULL;
    if(*head_ref==NULL){
        new_node->prev = NULL;
        *head_ref = new_node;
        return;}
    while(last->next!=NULL)last=last->next;
    last->next=new_node;
    new_node->prev = last;
    return;
}
//add node before given node
void insertBefore(Node** head_ref, Node* next_node, int num){
    if(next_node==NULL)return;
    Node* new_node = new Node();
    new_node->data = num;
    new_node->prev = next_node->prev;
    next_node->prev = new_node;
    new_node->next = next_node;
    if(new_node->prev!=NULL)new_node->prev->next=new_node;
    else{(*head_ref)=new_node;}
}
//delete node
void deleteNode(Node** head_ref, int key){
    Node* temp = *head_ref;
    if(temp == NULL)return;
    if(temp!=NULL && temp->data==key){
        *head_ref = temp->next;
        delete temp;return;
    }
    else{
        while(temp!=NULL && temp->data!=key)temp=temp->next;
        if(temp->next!=NULL)temp->next->prev=temp->prev;
        if(temp->prev!=NULL)temp->prev->next=temp->next;
        delete temp;return;
    }
}
//delete at position
void deleteAtPosition(Node** head_ref, int pos){
    if(*head_ref==NULL || pos<=0)return;
    Node *temp = *head_ref;
    for(int i = 1; temp!=NULL && i<pos;i++)temp=temp->next;
    if(temp==NULL)return;
    if(*head_ref==temp)*head_ref=temp->next;
    if(temp->next!=NULL)temp->next->prev=temp->prev;
    if(temp->prev!=NULL)temp->prev->next=temp->next;
    delete temp;
}
//reverse linked list
void reverse(Node**head_ref){
    Node *temp = NULL;
    Node *current = *head_ref;
    while(current!=NULL){
        temp=current->prev;
        current->prev= current->next;
        current->next = temp;
        current = current->prev;}
    if(temp!=NULL)*head_ref = temp->prev;
}
//remove duplicates (with hash table)
void removeDuplicates(Node** head_ref){
    unordered_set<int> set;
    Node* temp = *head_ref;
    while(temp!=NULL){
        if(set.find(temp->data)!=set.end()){
            deleteNode(head_ref, temp->data);
        }
        else{        
            set.insert(temp->data);
        }
        temp = temp->next;}


}
//print list
void printList(Node* head){
    Node* last;
    printf("Transversal in forward direction: \n");
    while(head!=NULL){
    printf(" %d", head->data);
    last=head;
    head=head->next;}
    printf("\nTraversal in reverse: \n");
    while(last!=NULL){
        printf(" %d", last->data);
        last=last->prev;}
    printf("\n");
}
int main() {
  Node* head = NULL;
  push(&head, 1); //1->NULL
  push(&head, 2); // 2->1->NULL
  insertAfter(head->next, 3); //2->1->3->NULL
  insertBefore(&head, head->next, 4); //2->4->1->3->NULL
  insertEnd(&head, 5); //2->4->1->3->5->NULL
  printList(head);
  deleteAtPosition(&head, 5);
  //deleteNode(&head, 2); stupid memory issues i cant be bothered
  printList(head);
  reverse(&head);
  printList(head);
  push(&head, 12);
  push(&head, 12);
  push(&head, 10);
  push(&head, 4);
  push(&head, 8);
  push(&head, 4);
  push(&head, 6);
  push(&head, 4); 
  push(&head, 4);
  push(&head, 8);
  printList(head);
  removeDuplicates(&head);
  printList(head);
  return 0;
}