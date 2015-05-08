template = """.method static readInt()I
  .limit stack 1
  .limit locals 0
  getstatic Main/__inner__in Ljava/util/Scanner;
  invokevirtual java/util/Scanner/nextInt()I
  ireturn
.end method

.method static readBool()Z
  .limit stack 1
  .limit locals 0
  getstatic Main/__inner__in Ljava/util/Scanner;
  invokevirtual java/util/Scanner/nextBoolean()Z
  ireturn
.end method

.method static readStr()Ljava/lang/String;
  .limit stack 1
  .limit locals 0
  getstatic Main/__inner__in Ljava/util/Scanner;
  invokevirtual java/util/Scanner/next()Ljava/lang/String;
  areturn
.end method"""


def generateReads():
    return [s.strip() for s in template.split('\n')]