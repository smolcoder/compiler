template = """.method static writeln([Ljava/lang/Object;)V
  .limit stack 2
  .limit locals 5
Label0:
     aload_0
     astore_1
Label2:
     aload_1
     arraylength
     istore_2
Label5:
     iconst_0
     istore_3
Label7:
     iload_3
     iload_2
     if_icmpge Label39
     aload_1
     iload_3
     aaload
     astore 4
Label17:
     getstatic java/lang/System/out Ljava/io/PrintStream;
     aload 4
     invokevirtual java/io/PrintStream/print(Ljava/lang/Object;)V
     getstatic java/lang/System/out Ljava/io/PrintStream;
     bipush 32
     invokevirtual java/io/PrintStream/print(C)V
Label33:
     iinc 3 1
     goto Label7
Label39:
     getstatic java/lang/System/out Ljava/io/PrintStream;
     invokevirtual java/io/PrintStream/println()V
Label45:
     return
.end method"""


def generateWriteLn():
    return [s.strip() for s in template.split('\n')]