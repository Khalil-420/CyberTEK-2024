#include <alloca.h>
#include <linux/limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_ALLOCATIONS 0x10

unsigned long target = 0;
char * allocations[MAX_ALLOCATIONS];

void setup() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);
}

void getInput(char *buffer) {
  int i = 0;
  char c;
  printf("Data: ");
  while ((c = getchar()) != '\n' && c != EOF) {
    buffer[i++] = c;
  }
  buffer[i] = '\0';
}

int getIndex() {
  for (int i = 0; i < MAX_ALLOCATIONS; i++) {
    if (!allocations[i]) {
      return i;
    }
  }
  return -1;
}

void allocate() {
  int index = getIndex(), size = -1;
  char *ptr = NULL;
  if (index == -1) {
    puts("No more allocations");
    return;
  }
  do {
    printf("Size: ");
    scanf("%d", &size);
    getc(stdin);
  } while (size <= 0);

  ptr = (char *) malloc(size);
  if (!ptr) {
    perror("malloc");
    return;
  }
  getInput(ptr);
  allocations[index] = ptr;
  
}

void delete() {
  int index = -1;
  do {
    printf("Index: ");
    scanf("%d", &index);
  } while (index < 0 || allocations[index] == NULL);
  free(allocations[index]);
  allocations[index] = NULL;
}

void edit() {
  int index = -1;
  do {
    printf("Index: ");
    scanf("%d", &index);
    getc(stdin);
  } while (index < 0 || allocations[index] == NULL);
  getInput(allocations[index]);
}

int main() {
  int choice = -1;
  setup();
  for (;;) {
    printf("\n1. Allocate\n2. Delete\n3. Edit\n4. Exit\nChoice >> ");
    scanf("%d", &choice);
    switch (choice) {
      case 1:
        allocate();
        break;
      case 2:
        delete();
        break;
      case 3:
        edit();
        break;
      case 4:
        exit(0);
      case 1337:
        if (target) {
          system("/bin/sh");
        }
        break;
      default:
        continue;
      
    }
  }
  return 0;
}
