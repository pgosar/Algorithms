#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <unordered_set>
using namespace std;
class Node {
  public:
  int data;
  Node *next;
};
//adding nodes
  //add node to front
  void push(Node** head_ref, int new_data){
    Node* new_node = new Node(); //allocating node
    new_node->data = new_data; //putting data into node
    new_node->next = (*head_ref); //setting node next to new_node as head
    (*head_ref)=new_node; //move the head to point to new node
  }
  //add a node after a given node
  void insertAfter(Node* prev_node, int new_data){
    if(prev_node==NULL){ //checks if the given previous node exists
      printf("previous node cannot be NULL");
      return;}
    Node* new_node = new Node(); //allocate new node
    new_node -> data = new_data; //put in data
    new_node ->next = prev_node->next; //make the node next to new node the prev node
    prev_node->next = new_node; //move the next node of prev node to new node
  }
  //add node to end of linked list
  void append(Node**head_ref, int new_data){
    Node* new_node = new Node(); //allocate node
    Node *last = *head_ref; //define last node which new node will be added to
    new_node -> data = new_data; //put in data
    new_node->next = NULL; //node after last node is NULL
    if(*head_ref==NULL){ //if linked list is empty, make new node the head
      *head_ref = new_node;
      return;}
    while(last->next !=NULL)last=last->next; //traverse till last node is reached
    last->next = new_node; //set node after previous last node to new node
    return;
  }
  //print out a linked list starting from head
  void printList(Node *node){
    while(node!=NULL) { //while the linked list exists 
      cout << " " << node->data; //prints out what the node contain
      node = node ->next; //goes to next node in list
    }
  }

//deleting nodes
  //iteratively
  void deleteNodeIterative(Node** head_ref, int key){
    Node* temp= *head_ref; //store head node
    Node *prev = NULL;
    if(temp!=NULL && temp->data==key){ //if the head node is the one to be deleted (holds specified key)
      *head_ref=temp->next; //change head
      delete temp; //free memory
      return;
    }
    else{ //if head node is not the one to be deleted
      while(temp!=NULL &&temp->data !=key){ //go through list until it finds node that needs to be deleted
        prev=temp; //keeps track of previous node 
        temp=temp->next;
      }
      if(temp==NULL){return;printf("was not present");} //if key was not present in list
      prev->next=temp->next; //unlink node from list
      delete temp; //free memory
    }
  }
  //recursively
  void deleteNodeRecursive(Node*&head, int val){
    if(head==NULL){
      printf("element not present");
      return;}
    if(head->data==val){
      Node* new_node = head;
      head = head->next;
      delete(new_node);
      return;
    }
    deleteNodeRecursive(head->next,val);
  }
  //delete at given position
  void deleteAtPosition(Node** head_ref, int position){
    //if linked list is empty
    if(*head_ref==NULL)return;
    Node *temp = *head_ref; //store head node in temp
    if(position==0){
      *head_ref=temp->next;
      delete(temp);
      return;}
    //find the previous node of the node to be deleted
    for(int i=0; temp!=NULL && i < position-1;i++)temp=temp->next;
    //if position is more than number of nodes
    if(temp==NULL ||temp->next==NULL)return;
    //reroute node before one to be deleted to point towards one after deleted node
    Node *next = temp->next->next;
    delete(temp->next);
    temp->next=next; //unlink deleted node from list
  }
  //deleting a linked list
  void deleteLinkedList(Node**head_ref){
    Node* temp = *head_ref;
    Node* next = NULL;
    while(temp != NULL){ //checks to see if the current node exists
      next = temp->next; //traverses linked list 
      delete(temp); //deletes node
      temp = next; //sets temp to node after deleted one
      }
      *head_ref = NULL;
  }
//finding length of linked list
  //iteratively
  int findLengthIterative(Node *head){
    int count=0;
    Node* temp = head;
    while(temp !=NULL){ //while current node exists, count up, traverse list
      count++;
      temp=temp->next;}
    return count;
  }
  //recursively
  int findLengthRecursive(Node *head){
    if(head==NULL)return 0;
    return findLengthRecursive(head->next)+1;
  }
//search for element in linked list 
  //iteratively
  bool searchElementIterative(Node *head, int key){
    Node* temp = head;
    while(temp!=NULL){ //while temp is not null search node data for key return true if found else return false
      if(temp->data ==key)return true;
      else{temp=temp->next;}}
    return false;
  }
  //recursively
  bool searchElementRecursive(Node *head, int key){
    if(head==NULL)return false;
    return searchElementRecursive(head->next, key);
  }
//function to get Nth node in linked list
int NthNode(Node *head, int n){
  int position = 0;
  Node* temp = head;
  while(temp!=NULL){ //if temp is not null see if position matches given and output data, traverse list
    if(position+1==n)return temp->data;
    temp=temp->next;
    position++;}
  return -1;
}
//function to get Nth node from the end of a linked list
int NthNodeEnd(Node *head, int n){
  int position = 0, len=0;
  Node *temp=head;
  while(temp!=NULL){len++;temp=temp->next;}
  if(n > len)return -1;
  temp=head;
  for(int i=1;i<len-n+1;i++)temp=temp->next;
  return temp->data;
}
//find middle of linked list
int listMiddle(Node *head){
  int count =0;
  Node* temp = head;
  while(temp!=NULL){count++;temp=temp->next;}
  temp=head;
  if(count%2==0){
    for(int i =1; i < count/2;i++)temp=temp->next;
    return temp->data;}
  else{
    for(int i =0; i < count/2;i++)temp=temp->next;
    return temp->data;}
}
//number of times element appears
int elementCount(Node *head, int num){
int count = 0;
Node* temp = head;
while(temp!=NULL){
  if(temp->data==num)count++;
  temp=temp->next;}
return count;
}
//detect loop in linked list
bool detectLoop(Node*head){
  unordered_set<Node*> map;
  Node* temp =head;
  while(temp!=NULL){
    if(map.end()!= map.find(temp))return true; //loop found
    map.insert(temp);
    temp=temp->next;
  }
  return false;
}
//detect and remove loop in linked list
bool deleteLoop(Node*head){
  unordered_set<Node*> map;
  while(head!=NULL){
    if(map.end()!= map.find(head)){
      head->next=NULL;
      return true; //loop found
    }
    map.insert(head);
    head=head->next;
  }
  return false;
}
//stopped at number 13 @geeks for geeks 
int main() {
  Node* head = NULL; //start with empty list
  append(&head, 6); //list is now 6->NULL
  push(&head, 7); //list is now 7->6->NULL
  push(&head, 1); //list is now 1->7->6->NULL
  append(&head, 4); //list is now 1->7->6->4->NULL
  insertAfter(head->next, 8); //list is now 1->7->8->6->4->NULL
  printf("Linked List: ");
  printList(head);printf("\n");
  deleteNodeIterative(&head, 1);
  printf("Linked list after deletion: ");
  deleteNodeRecursive(head, 7);
  printList(head);printf("\n");
  deleteAtPosition(&head, 2);
  printf("Linked list after deletion at specified position: ");
  printList(head);printf("\n");
  deleteLinkedList(&head);
  printList(head);
  printf("Linked List deleted");printf("\n");
  append(&head, 6); //list is now 6->NULL
  push(&head, 7); //list is now 7->6->NULL
  push(&head, 1); //list is now 1->7->6->NULL
  append(&head, 4); //list is now 1->7->6->4->NULL
  insertAfter(head->next, 8); //list is now 1->7->8->6->4->NULL
  push(&head, 6);
  printf("Linked List: ");
  printList(head);printf("\n");
  cout << "Length of linked list is " <<findLengthIterative(head)<<endl;
  cout << "Length of linked list calculated recursively is " << findLengthRecursive(head)<< endl;
  printf("Is specified key in linked list: ");
  searchElementIterative(head, 6) ? printf("yes\n") : printf("no\n");
  printf("Is specified key in linked list: ");
  searchElementRecursive(head, 69) ? printf("yes\n") : printf("no\n");
  printf("Datapoint of given node: ");
  cout <<NthNode(head,2);printf("\n");
  cout << "Datapoint of given node from end: " << NthNodeEnd(head,2);printf("\n");;
  cout <<"Middle of linked list: " << listMiddle(head);printf("\n");
  printf("Linked List: ");
  printList(head);printf("\n");
  cout << "Number of times element appears in linked list: " << elementCount(head, 6) << endl;
  Node* head_2 = NULL;
  push(&head_2, 20);push(&head_2, 4);push(&head_2, 15);push(&head_2, 10);
  head_2->next->next->next->next = head_2;
  detectLoop(head) ? printf("Loop found\n") : printf("Loop not found\n");
  detectLoop(head_2) ? printf("Loop found\n") : printf("Loop not found\n");
  deleteLoop(head_2) ? printf("Loop found and deleted\n") : printf("Loop not found\n");
  detectLoop(head_2) ? printf("Loop found\n") : printf("Loop not found\n");
  return 0;
}