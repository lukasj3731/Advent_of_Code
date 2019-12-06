String input = "168630-718098";
String[] list = input.split("-");
int min, max;

void setup() {
  min = Integer.parseInt(list[0]);
  max = Integer.parseInt(list[1]);
  int c1 = 0, c2 = 0;
  for(int i=min;i<=max;i++) {
    c1 += (isPwd1(""+i))? 1:0;
    c2 += (isPwd2(""+i))? 1:0;
  }
  println("Task 1: "+c1);
  println("Task 2: "+c2);
}

boolean isPwd1(String n) {
  return adj(n) && ordered(n);
}

boolean isPwd2(String n) {
  return adjo2(n) && ordered(n);
}

boolean adj(String n) {
  boolean r = false;
  for(int i=0;i<n.length()-1;i++) {
    r = (n.charAt(i)==n.charAt(i+1))? true : r;
  }
  return r;
}

boolean ordered(String n) {
  boolean r = true; 
  for(int i=0;i<n.length()-1;i++) {
    r = (n.charAt(i)>n.charAt(i+1))? false : r;
  }
  return r;
}

boolean adjo2(String n) {
  String m = "x"+n+"x";
  boolean r = false;
  for(int i=1;i<m.length()-2;i++) {
    r = (m.charAt(i)==m.charAt(i+1) && m.charAt(i)!= m.charAt(i-1) && m.charAt(i)!= m.charAt(i+2))? true : r;
  }
  return r;
}
