#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

char **book = NULL;
unsigned int *page_sizes = NULL;
void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int getIndex() {
  int i = 0;
  for (i = 0; i < 0x20; i++ ){
    if (book[i] == NULL) {
      return i;
    }
  }
  return -1;
}

void add_page() {
  int index = getIndex();
  int size = -1;
  if (index != -1) {
    do {
      printf("Size : ");
      scanf("%d", &size);
    } while (size <= 0 || size > 0x80);
    book[index] = (char* )malloc(size);
    if (!book) {
      perror("malloc");
      exit(1);
    }
    printf("Content: ");
    read(0, book[index], size);
    page_sizes[index] = size;
  }
}

void delete_page() {
  int index = -1;
  do {
    printf("Index: ");
    scanf("%d", &index);
  } while (index < 0 || index >= 0x20 || book[index] == NULL);
  free(book[index]);
}

void edit_page() {
  int index = -1;
  do {
    printf("Index: ");
    scanf("%d", &index);
  } while(index < 0 || index >= 0x20 || book[index] == NULL);
  printf("Content: ");
  read(0, book[index], page_sizes[index]);
}

void show_page() {
  int index = -1;
  do {
    printf("Index: ");
    scanf("%d", &index);
  } while (index < 0 || index >= 0x20 || book[index] == NULL);
  printf("Content: %s\n", book[index]);
}

int main() {
  setup();
  int choice = -1;
  book = (char **)malloc(8 * 0x20);
  page_sizes = (unsigned int *) malloc(8 * 0x20);
  if (!book || !page_sizes) {
    perror("malloc");
    exit(1);
  }
  for(;;) {
    puts("Welcome To TekUpCtf24");
    printf("1. Add\n2. Delete\n3. Edit\n4. Show\nChoice >> ");
    scanf("%d", &choice);
    switch (choice) {
      case 1:
        add_page();
        break;
      case 2:
        delete_page();
        break;
      case 3:
        edit_page();
        break;
      case 4:
        show_page();
        break;
      default:
        continue;
    }
  }

  return 0;
}
