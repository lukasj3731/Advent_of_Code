import java.util.*;

String s = "59705379150220188753316412925237003623341873502562165618681895846838956306026981091618902964505317589975353803891340688726319912072762197208600522256226277045196745275925595285843490582257194963750523789260297737947126704668555847149125256177428007606338263660765335434914961324526565730304103857985860308906002394989471031058266433317378346888662323198499387391755140009824186662950694879934582661048464385141787363949242889652092761090657224259182589469166807788651557747631571357207637087168904251987880776566360681108470585488499889044851694035762709053586877815115448849654685763054406911855606283246118699187059424077564037176787976681309870931";

int[] pattern = {0,1,0,-1};
int pos;
int[] signal2;
int[] signal1;

void setup() {
  String m = String.join("", Collections.nCopies(10000, s));
  pos = Integer.parseInt(s.substring(0,7));
  
  signal2 = new int[m.length()];
  signal1 =new int[s.length()];
  
  for(int i=0;i<signal2.length;i++) {
    signal2[i] = Integer.parseInt(""+m.charAt(i));
  }
  for(int i=0;i<signal1.length;i++) {
    signal1[i] = Integer.parseInt(""+m.charAt(i));
  }

  for(int i=0;i<100;i++) {
    applyFFTOP();
    applyFFT();
  }

  String t1="",t2="";
  for(int i=0;i<8;i++) {
    t1+=signal1[i];
    t2+=signal2[pos+i];
  }
  println("Task 1: "+t1+"\nTask 2: "+t2);
}

void applyFFT() {
  for(int i=0;i<signal1.length;i++){
    calcPos(i);
  }
}

void calcPos(int pos) {
  int sum = 0;
  for(int i=0;i<signal1.length;i++){
    sum += signal1[i]*pattern[(i+1)/(pos+1)%4];
  }
  signal1[pos] = abs(sum%10);
}

void applyFFTOP() {
  for(int i=signal2.length-1;i>=pos;i--){
    calcPosOP(i);
  }
}

void calcPosOP(int pos) {
  if(pos!=signal2.length-1) {
    signal2[pos] = abs((signal2[pos]+signal2[pos+1])%10);
  }
}
