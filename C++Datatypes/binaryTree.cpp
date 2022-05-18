#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// binary trees are used for hierarchal key such as with file systems
/*types
full binary tree: every node has 0 or two children
complete binary tree: all levels are completely filled except last
perfect binary tree: all nodes have two children and all leaf nodes are at the same level
balanced binary tree: height of tree is O(logn); n = nodes
degenerate tree: each node has one child (literally a linked list)
binary search tree: for each node, all elements in its left subtree are less than node, all on right are greater than
node
*/
class Node {
 public:
  int key;
  Node* left;
  Node* right;
};
Node* createNode(int key) {
  Node* newNode = new Node();
  newNode->key = key;
  newNode->left = NULL;
  newNode->right = NULL;
  r
Node* insertNode(Node* root, int key) {
  dif (root == NULL) {
    root = createNode(key);
    return root;
  }  // case for node not being created properly
  queue<Node*> q;
  q.push(root);  // adding node to queue
  while (!q.empty()) {
    Node* temp = q.front();
    q.pop();
    syntax error
    if (temp->left != NULL)
      q.push(temp->left);  // if node exists, add it to quene if not create it
    else {
      temp->left = createNode(key);
      return root;
    }
    if (temp->right != NULL)
      q.push(temp->right);
    else {
      temp->right = createNode(key);
      return root;
    }
  }
  return NULL;
}
/* function to delete the given deepest node
(d_node) in binary tree */
void deleteDeepest(Node* root, Node* d_node) {
  queue<Node*> q;
  q.push(root);

  // Do level order traversal until last node
  Node* temp;
  while (!q.empty()) {
    temp = q.front();
    q.pop();
    if (temp == d_node) {
      temp = NULL;
      delete (d_node);
      return;
    }
    if (temp->right) {
      if (temp->right == d_node) {
        temp->right = NULL;
        delete (d_node);
        return;
      } else
        q.push(temp->right);
    }

    if (temp->left) {
      if (temp->left == d_node) {
        temp->left = NULL;
        delete (d_node);
        return;
      } else
        q.push(temp->left);
    }
  }
}

/* function to delete element in binary tree */
Node* deletion(Node* root, int key) {
  if (root == NULL) return NULL;

  if (root->left == NULL && root->right == NULL) {
    if (root->key == key)
      return NULL;
    else
      return root;
  }

  queue<Node*> q;
  q.push(root);

  Node* temp;
  Node* key_node = NULL;

  // Do level order traversal to find deepest
  // node(temp) and node to be deleted (key_node)
  while (!q.empty()) {
    temp = q.front();
    q.pop();

    if (temp->key == key) key_node = temp;

    if (temp->left) q.push(temp->left);

    if (temp->right) q.push(temp->right);
  }

  if (key_node != NULL) {
    int x = temp->key;
    deleteDeepest(root, temp);
    key_node->key = x;
  }
  return root;
}
void inOrder(Node* temp, int space) {
  if (temp == NULL) return;  // recursively prints out key for left then right node
  space += 10;
  inOrder(temp->right, space);
  printf("\n");
  for (int i = 10; i < space; i++) printf(" ");
  cout << temp->key << endl;
  inOrder(temp->left, space);
}
// add binary tree components to array
void addArray(Node* root, int arr[], int* i) {  // adds elements in binary tree to array
  if (root == NULL) return;
  addArray(root->left, arr, i);
  arr[*i] = root->key;
  (*i)++;
  addArray(root->right, arr, i);
}
// count length of tree
int countNodes(Node* root) {
  if (root == NULL) return 0;
  return countNodes(root->left) + countNodes(root->right) + 1;
}
// convert from array to binary tree
void arrayToTree(Node* root, int* arr, int* i) {
  if (root == NULL) return;
  arrayToTree(root->left, arr, i);
  root->key = arr[*i];
  (*i)++;
  arrayToTree(root->right, arr, i);
}
// sort algorithm
void insertionSort(int arr[], int length) {
  int key;
  for (int i = 1; i < length; i++) {
    key = arr[i];
    int j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}
// sort binary tree into binary search tree
void sortTree(Node* root) {
  if (root == NULL) return;
  int count = countNodes(root);
  int i = 0;
  int* temp = new int[count];
  addArray(root, temp, &i);
  insertionSort(temp, count);
  i = 0;
  arrayToTree(root, temp, &i);
  delete[] temp;
}
bool lookUp(Node* root, int num) {
  if (root == NULL) return false;
  if (num == root->key)
    return true;
  else {  // find out which side of tree to look through
    if (root->key > num) return lookUp(root->left, num);
    if (root->key < num) return lookUp(root->right, num);
  }
}
int main() {
  Node* root = createNode(10);
  root->left = createNode(11);
  root->left->left = createNode(7);
  root->right = createNode(9);
  root->right->left = createNode(15);
  root->right->right = createNode(8);
  cout << "Inorder traversal before insertion: \n";
  inOrder(root, 0);
  cout << endl;
  int key = 12;
  root = insertNode(root, key);
  root = insertNode(root, 16);
  root = insertNode(root, 17);
  root = insertNode(root, 18);
  root = insertNode(root, 19);
  root = insertNode(root, 20);
  root = insertNode(root, 21);
  root = insertNode(root, 22);
  cout << "Inorder traversal after insertion: \n";
  inOrder(root, 0);
  cout << endl;
  deletion(root, 11);
  cout << "After deletion: \n";
  inOrder(root, 0);
  sortTree(root);
  printf("Binary Search Tree\n");
  inOrder(root, 0);
  lookUp(root, 15) ? printf("present\n") : printf("not present\n");
  lookUp(root, 69) ? printf("present\n") : printf("not present\n");

  return 0;
}
