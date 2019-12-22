import java.math.BigInteger;
import java.util.*;

String in = "deal with increment 13,cut 5485,deal with increment 50,cut 9877,deal with increment 8,cut 4323,deal with increment 6,cut 2478,deal with increment 32,cut 299,deal with increment 72,cut 5108,deal with increment 10,cut -1774,deal with increment 24,cut -8840,deal with increment 34,cut 7488,deal with increment 74,cut 1851,deal into new stack,deal with increment 60,cut -6016,deal into new stack,deal with increment 49,cut -8082,deal with increment 54,deal into new stack,deal with increment 15,deal into new stack,deal with increment 38,cut -4112,deal with increment 13,deal into new stack,cut 4372,deal into new stack,deal with increment 75,cut -5702,deal with increment 65,cut 4979,deal with increment 39,cut 1967,deal with increment 55,cut 8554,deal with increment 50,deal into new stack,cut 1337,deal with increment 53,cut 426,deal with increment 7,cut 8947,deal with increment 58,cut 8826,deal with increment 52,cut 6167,deal with increment 18,cut -4305,deal with increment 20,cut 7168,deal with increment 10,cut 422,deal with increment 41,cut -1601,deal with increment 72,deal into new stack,deal with increment 27,cut -3921,deal with increment 47,cut 4024,deal into new stack,cut 7800,deal with increment 10,cut -3742,deal with increment 35,deal into new stack,deal with increment 72,cut 7456,deal with increment 29,cut -6731,deal with increment 57,cut -6162,deal into new stack,deal with increment 26,cut -4817,deal with increment 48,cut 9420,deal into new stack,deal with increment 8,cut -7408,deal into new stack,cut -3479,deal with increment 31,cut 5246,deal with increment 12,cut -9275,deal with increment 37,cut -4512,deal with increment 15,cut -8511,deal with increment 8";

String[] instr = in.split(",");

int d = 10007;
int pos = 2019;

BigInteger D = new BigInteger("119315717514047");
BigInteger position = new BigInteger("7171");

void setup() {
  println("Task 1: "+forw(2019));
  
  // thanks u/etotheipi1/ for explaining this on reddit. had no idea how to do this,
  // and all my approaches failed miserably or took way to long. But after thoroughly 
  // reading this and adjusting my code I think I get it now. Even if I don't completely 
  // get the modulo invers maths yet, at least I got it working.
  
  D = new BigInteger("119315717514047");
  position = new BigInteger("7171");
  BigInteger X = new BigInteger("2020");
  BigInteger Y = rev(X);
  BigInteger Z = rev(Y);
  BigInteger A = (Y.subtract(Z)).multiply(X.subtract(Y).modInverse(D)).mod(D);
  BigInteger B = Y.subtract(A.multiply(X)).mod(D);
  BigInteger n = new BigInteger("101741582076661");
  println("Task 2: "+A.modPow(n,D).multiply(X).add(  A.modPow(n,D).subtract(BigInteger.ONE).multiply(A.subtract(BigInteger.ONE).modInverse(D)).multiply(B)).mod(D));  
}

int forw(int x) {
  pos = x;
  for(int i=0;i<instr.length;i++) {
    doOp1(instr[i], pos);
  }
  return pos;
}

void doOp1(String in, int pos) {
  if (in.charAt(0)=='c') {
    cut(pos, Integer.parseInt(in.split(" ")[1]));
  } else if (in.charAt(5) == 'w') {
    inc(pos,Integer.parseInt(in.split(" ")[3]));
  } else {
    deal(pos);
  }
}

void deal(int p) {
  pos = d-1-p;
}

void cut(int p, int n) {
  pos = (p+d-n)%d;
}

void inc(int p, int n) {
  pos = (p*n)%d;
}

//task 2 methods, credit to u/etotheipi1/
void rev_deal(BigInteger pos) {
  position =  D.subtract(pos).subtract(BigInteger.ONE);
}

void rev_cut(BigInteger pos, BigInteger n) {
  position = pos.add(D).add(n).mod(D);
}

void rev_inc(BigInteger pos, BigInteger n) {
  position = n.modInverse(D).multiply(pos).mod(D);
}

BigInteger rev(BigInteger x) {
  position = x;
  for(int i=instr.length-1;i>=0;i--) {
    doOp2(instr[i], position);
  }
  return position;
}

void doOp2(String in, BigInteger position) {
  if (in.charAt(0)=='c') {
    rev_cut(position, new BigInteger(in.split(" ")[1]));
  } else if (in.charAt(5) == 'w') {
    rev_inc(position, new BigInteger(in.split(" ")[3]));
  } else {
    rev_deal(position);
  }
}
