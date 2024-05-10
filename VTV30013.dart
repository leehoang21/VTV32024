import 'dart:io';

int n = 1;

input() {
  n = int.parse(stdin.readLineSync() ?? '');
}

double Sn(int n) {
  if (n == 1) {
    return 0.5;
  } else {
    return (n / (n + 1)) + Sn(n - 1);
  }
}

void output(double n) {
  print(n.toStringAsFixed(10));
}

void main() {
  int testcase = int.parse(stdin.readLineSync() ?? '');
  for (int i = 0; i < testcase; i++) {
    input();
    double a = Sn(n);
    output(a);
  }
}
