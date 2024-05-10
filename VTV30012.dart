import 'dart:io';

List<String> l = [];
int n = 1;

input() {
  n = int.parse(stdin.readLineSync() ?? '');
  l = (stdin.readLineSync() ?? '').split(' ');
}

String solve(int i) {
  if (i >= n) {
    return 'Yes';
  }
  if (double.parse(l[i]) < 0) {
    return solve(i + 1);
  } else {
    return 'No';
  }
}

void output(String n) {
  print(n);
}

void main() {
  int testcase = int.parse(stdin.readLineSync() ?? '');
  for (int i = 0; i < testcase; i++) {
    input();
    String a = solve(0);
    output(a);
  }
}
