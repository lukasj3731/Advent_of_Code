import java.util.*;

String in = "2 RWPCH => 9 PVTL;1 FHFH => 4 BLPJK;146 ORE => 5 VJNBT;8 KDFNZ, 1 ZJGH, 1 GSCG => 5 LKPQG;11 NWDZ, 2 WBQR, 1 VRQR => 2 BMJR;3 GSCG => 4 KQDVM;5 QVNKN, 6 RPWKC => 3 BCNV;10 QMBM, 4 RBXB, 2 VRQR => 1 JHXBM;15 RPWKC => 6 MGCQ;1 QWKRZ => 4 FHFH;10 RWPCH => 6 MZKG;11 JFKGV, 5 QVNKN, 1 CTVK => 4 VQDT;1 SXKT => 5 RPWKC;1 VQDT, 25 ZVMCB => 2 RBXB;6 LGLNV, 4 XSNKB => 3 WBQR;199 ORE => 2 SXKT;1 XSNKB, 6 CWBNX, 1 HPKB, 5 PVTL, 1 JNKH, 9 SXKT, 3 KQDVM => 3 ZKTX;7 FDSX => 6 WJDF;7 JLRM => 4 CWBNX;167 ORE => 5 PQZXH;13 JHXBM, 2 NWDZ, 4 RFLX, 12 VRQR, 10 FJRFG, 14 PVTL, 2 JLRM => 6 DGFG;12 HPKB, 3 WHVXC => 9 ZJGH;1 JLRM, 2 ZJGH, 2 QVNKN => 9 FJRFG;129 ORE => 7 KZFPJ;2 QMBM => 1 RWPCH;7 VJMWM => 4 JHDW;7 PQZXH, 7 SXKT => 9 BJVQM;1 VJMWM, 4 JHDW, 1 MQXF => 7 FDSX;1 RPWKC => 7 WHVXC;1 ZJGH => 1 ZVMCB;1 RWPCH => 3 MPKR;187 ORE => 8 VJMWM;15 CTVK => 5 GSCG;2 XSNKB, 15 ZVMCB, 3 KDFNZ => 2 RFLX;18 QVNKN => 8 XLFZJ;4 CWBNX => 8 ZSCX;2 ZJGH, 1 JLRM, 1 MGCQ => 9 NPRST;13 BJVQM, 2 BCNV => 2 QWKRZ;2 QWKRZ, 2 BLPJK, 5 XSNKB => 2 VRQR;13 HPKB, 3 VQDT => 9 JLRM;2 SXKT, 1 VJNBT, 5 VLWQB => 6 CTVK;2 MPKR, 2 LMNCH, 24 VRQR => 8 DZFNW;2 VQDT => 1 KDFNZ;1 CTVK, 6 FDSX => 6 QVNKN;3 CTVK, 1 QVNKN => 4 HPKB;3 NPRST, 1 KGSDJ, 1 CTVK => 2 QMBM;4 KZFPJ, 1 PQZXH => 5 VLWQB;2 VQDT => 7 KGSDJ;3 MPKR => 2 JNKH;1 KQDVM => 5 XQBS;3 ZKGMX, 1 XQBS, 11 MZKG, 11 NPRST, 1 DZFNW, 5 VQDT, 2 FHFH => 6 JQNF;2 FJRFG, 17 BMJR, 3 BJVQM, 55 JQNF, 8 DGFG, 13 ZJGH, 29 ZKTX => 1 FUEL;27 KZFPJ, 5 VJNBT => 5 MQXF;11 FDSX, 1 WHVXC, 1 WJDF => 4 ZKGMX;1 ZVMCB => 4 NWDZ;1 XLFZJ => 6 LGLNV;13 ZSCX, 4 XLFZJ => 8 LMNCH;1 RPWKC, 1 FDSX, 2 BJVQM => 8 JFKGV;1 WJDF, 1 LKPQG => 4 XSNKB";
String[] l = in.split(";");
ArrayList<Reaction> reactions = new ArrayList<Reaction>();
Map<String, Long> stock = new HashMap<String, Long>();

void setup() {
  for (int i=0; i<l.length; i++) {
    reactions.add(new Reaction(l[i]));
  }

  println("Task 1: "+calcneed(1, "FUEL"));
  println("Task 2: "+calcget(1000000000000L));
}

long calcget(long l) {
  long i=0;
  double step = 0.1/calcneed(1, "FUEL");
  long f = 0;
  while (f<l) {
    f = calcneed(i, "FUEL");
    resetStock();
    i+= Math.ceil((l-f)*step);
  }
  return i-1;
}

void resetStock() {
  for(String s:stock.keySet()) {
    stock.put(s,0L);
  }
}

long calcneed(long amount, String name) {
  if (name.equals("ORE")) {
    return amount;
  }
  if (stock.get(name)>=amount) {
    stock.put(name, stock.get(name)-amount);
    return 0;
  } else {
    amount -= stock.get(name);
    stock.put(name, (long)0);
  }
  Reaction r = getReac(name);
  long f=0;
  f = (long)Math.floor(amount/r.output.amount);
  while (f*r.output.amount<amount) {
    f++;
  }
  stock.put(name, f*r.output.amount-amount);
  long sum =0;
  for (Ore o : r.inputs) {
    sum += calcneed(o.amount*f, o.name);
  }
  return sum;
}

Reaction getReac(String name) {
  for (Reaction r : reactions) {
    if (r.output.name.equals(name)) {
      return r;
    }
  }
  return null;
}

class Reaction {
  Ore output;
  ArrayList<Ore> inputs = new ArrayList<Ore> ();
  public Reaction (String in) {
    String[] temp = in.split("=>");
    output = new Ore(temp[1]);
    temp = temp[0].split(",");
    for (int i=0; i<temp.length; i++) {
      inputs.add(new Ore(temp[i]));
    }
  }

  boolean equals(Object o) {
    return o.equals(output.name);
  }
}

class Ore {
  long amount;
  String name;
  public Ore(String in) {
    in = in.charAt(0)==' '?in.substring(1):in;
    amount = Long.parseLong(in.split(" ")[0]);
    name = in.split(" ")[1];
    stock.put(name, 0L);
  }
}
