#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int main() {
  setup();
  char buffer[0x20];
  puts("Welcome to TekUpCtf 2024 ^-^");
  printf("first words ? >> ");
  read(0, buffer, 0x200);
  printf("%s\n", buffer);
  return 0;
}
