import java.util.*;

String s = "59705379150220188753316412925237003623341873502562165618681895846838956306026981091618902964505317589975353803891340688726319912072762197208600522256226277045196745275925595285843490582257194963750523789260297737947126704668555847149125256177428007606338263660765335434914961324526565730304103857985860308906002394989471031058266433317378346888662323198499387391755140009824186662950694879934582661048464385141787363949242889652092761090657224259182589469166807788651557747631571357207637087168904251987880776566360681108470585488499889044851694035762709053586877815115448849654685763054406911855606283246118699187059424077564037176787976681309870931";
int[] pattern = {0, 1, 0, -1};
int[][] signal = new int[2][];

void setup() {
  String m = String.join("", Collections.nCopies(10000, s));
  int pos = Integer.parseInt(s.substring(0, 7));
  signal[0] = new int[s.length()];
  signal[1] = new int[m.length()];

  for (int i=0; i<signal[1].length; i++) {
    signal[1][i] = Integer.parseInt(""+m.charAt(i));
    if (i>=signal[0].length) continue;
    signal[0][i] = Integer.parseInt(""+m.charAt(i));
  }

  for (int i=0; i<100; i++) {
    for (int a=0; a<signal[0].length; a++) {
      calcPos(a);
    }
    for (int a=signal[1].length-1; a>=pos; a--) {
      calcPosb(a);
    }
  }

  String t1="", t2="";
  for (int i=0; i<8; i++) {
    t1 += signal[0][i];
    t2 += signal[1][pos+i];
  }
  println("Task 1: "+t1+"\nTask 2: "+t2);
}

void calcPos(int pos) {
  int sum = 0;
  for (int i=0; i<signal[0].length; i++) {
    sum += signal[0][i]*pattern[(i+1)/(pos+1)%4];
  }
  signal[0][pos] = abs(sum%10);
}

void calcPosb(int pos) {
  if (pos!=signal[1].length-1) {
    signal[1][pos] = abs((signal[1][pos]+signal[1][pos+1])%10);
  }
}
