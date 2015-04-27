# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .LLangListener import LLangListener
    from .LLangVisitor import LLangVisitor
else:
    from LLangListener import LLangListener
    from LLangVisitor import LLangVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\66\u01e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\7")
        buf.write(u"\2\u0081\n\2\f\2\16\2\u0084\13\2\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\7\4\u008c\n\4\f\4\16\4\u008f\13\4\3\4\3\4\3\5\3")
        buf.write(u"\5\3\5\3\5\3\6\3\6\3\6\5\6\u009a\n\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\7\3\7\5\7\u00a2\n\7\3\b\3\b\7\b\u00a6\n\b\f\b\16\b")
        buf.write(u"\u00a9\13\b\3\b\5\b\u00ac\n\b\3\b\3\b\3\t\3\t\3\t\7\t")
        buf.write(u"\u00b3\n\t\f\t\16\t\u00b6\13\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write(u"\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00c5\n\f\3\r\3")
        buf.write(u"\r\5\r\u00c9\n\r\3\16\3\16\3\16\5\16\u00ce\n\16\3\16")
        buf.write(u"\3\16\3\17\3\17\3\17\7\17\u00d5\n\17\f\17\16\17\u00d8")
        buf.write(u"\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00e2")
        buf.write(u"\n\21\3\21\3\21\3\22\3\22\3\22\7\22\u00e9\n\22\f\22\16")
        buf.write(u"\22\u00ec\13\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00f4")
        buf.write(u"\n\24\3\25\3\25\3\25\5\25\u00f9\n\25\3\26\3\26\3\27\3")
        buf.write(u"\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write(u"\3\34\3\34\3\34\7\34\u010c\n\34\f\34\16\34\u010f\13\34")
        buf.write(u"\3\35\3\35\7\35\u0113\n\35\f\35\16\35\u0116\13\35\3\35")
        buf.write(u"\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\5\36\u0124\n\36\3\37\3\37\3\37\3 \3 \5 \u012b\n ")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\5\"\u0136\n\"\3\"\3\"")
        buf.write(u"\5\"\u013a\n\"\3\"\3\"\5\"\u013e\n\"\3\"\3\"\3\"\3#\3")
        buf.write(u"#\5#\u0145\n#\3$\3$\5$\u0149\n$\3%\3%\3%\3%\3%\3%\3%")
        buf.write(u"\3%\3%\3%\3%\7%\u0156\n%\f%\16%\u0159\13%\3%\3%\5%\u015d")
        buf.write(u"\n%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write(u")\3)\7)\u016f\n)\f)\16)\u0172\13)\3)\3)\3*\3*\3*\3+\3")
        buf.write(u"+\3+\5+\u017c\n+\3+\3+\3,\3,\3,\7,\u0183\n,\f,\16,\u0186")
        buf.write(u"\13,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\5-\u0198\n-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\7-\u01ae\n-\f-\16-\u01b1\13-\3.\3")
        buf.write(u".\3.\3/\3/\3/\3/\3\60\3\60\3\60\5\60\u01bd\n\60\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write(u"\63\5\63\u01cb\n\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write(u"\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\2")
        buf.write(u"\3X?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write(u"\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\t\3")
        buf.write(u"\2\16\17\3\2\20\22\4\2\16\16\23\23\3\2\24\27\3\2\30\31")
        buf.write(u"\3\2\32\33\4\2\n\n\34 \u01e1\2\u0082\3\2\2\2\4\u0085")
        buf.write(u"\3\2\2\2\6\u0089\3\2\2\2\b\u0092\3\2\2\2\n\u0096\3\2")
        buf.write(u"\2\2\f\u00a1\3\2\2\2\16\u00a3\3\2\2\2\20\u00b4\3\2\2")
        buf.write(u"\2\22\u00b9\3\2\2\2\24\u00bd\3\2\2\2\26\u00c0\3\2\2\2")
        buf.write(u"\30\u00c8\3\2\2\2\32\u00ca\3\2\2\2\34\u00d6\3\2\2\2\36")
        buf.write(u"\u00db\3\2\2\2 \u00df\3\2\2\2\"\u00e5\3\2\2\2$\u00ed")
        buf.write(u"\3\2\2\2&\u00f3\3\2\2\2(\u00f8\3\2\2\2*\u00fa\3\2\2\2")
        buf.write(u",\u00fc\3\2\2\2.\u00fe\3\2\2\2\60\u0100\3\2\2\2\62\u0102")
        buf.write(u"\3\2\2\2\64\u0104\3\2\2\2\66\u0108\3\2\2\28\u0110\3\2")
        buf.write(u"\2\2:\u0123\3\2\2\2<\u0125\3\2\2\2>\u0128\3\2\2\2@\u012c")
        buf.write(u"\3\2\2\2B\u0132\3\2\2\2D\u0144\3\2\2\2F\u0148\3\2\2\2")
        buf.write(u"H\u014a\3\2\2\2J\u015e\3\2\2\2L\u0161\3\2\2\2N\u0166")
        buf.write(u"\3\2\2\2P\u0169\3\2\2\2R\u0175\3\2\2\2T\u0178\3\2\2\2")
        buf.write(u"V\u017f\3\2\2\2X\u0197\3\2\2\2Z\u01b2\3\2\2\2\\\u01b5")
        buf.write(u"\3\2\2\2^\u01bc\3\2\2\2`\u01be\3\2\2\2b\u01c3\3\2\2\2")
        buf.write(u"d\u01ca\3\2\2\2f\u01cc\3\2\2\2h\u01ce\3\2\2\2j\u01d0")
        buf.write(u"\3\2\2\2l\u01d2\3\2\2\2n\u01d4\3\2\2\2p\u01d6\3\2\2\2")
        buf.write(u"r\u01d8\3\2\2\2t\u01da\3\2\2\2v\u01dc\3\2\2\2x\u01de")
        buf.write(u"\3\2\2\2z\u01e0\3\2\2\2|\u0081\5\24\13\2}\u0081\5\b\5")
        buf.write(u"\2~\u0081\5\4\3\2\177\u0081\58\35\2\u0080|\3\2\2\2\u0080")
        buf.write(u"}\3\2\2\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0084")
        buf.write(u"\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write(u"\3\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\7%\2\2\u0086")
        buf.write(u"\u0087\5z>\2\u0087\u0088\5\6\4\2\u0088\5\3\2\2\2\u0089")
        buf.write(u"\u008d\7\3\2\2\u008a\u008c\5\24\13\2\u008b\u008a\3\2")
        buf.write(u"\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e")
        buf.write(u"\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090")
        buf.write(u"\u0091\7\4\2\2\u0091\7\3\2\2\2\u0092\u0093\7.\2\2\u0093")
        buf.write(u"\u0094\5\n\6\2\u0094\u0095\5\16\b\2\u0095\t\3\2\2\2\u0096")
        buf.write(u"\u0097\5z>\2\u0097\u0099\7\5\2\2\u0098\u009a\5\20\t\2")
        buf.write(u"\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b")
        buf.write(u"\3\2\2\2\u009b\u009c\7\6\2\2\u009c\u009d\7\7\2\2\u009d")
        buf.write(u"\u009e\5\f\7\2\u009e\13\3\2\2\2\u009f\u00a2\5&\24\2\u00a0")
        buf.write(u"\u00a2\5\62\32\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2")
        buf.write(u"\2\2\u00a2\r\3\2\2\2\u00a3\u00a7\7\3\2\2\u00a4\u00a6")
        buf.write(u"\5:\36\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write(u"\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ab\3\2\2")
        buf.write(u"\2\u00a9\u00a7\3\2\2\2\u00aa\u00ac\5<\37\2\u00ab\u00aa")
        buf.write(u"\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write(u"\u00ae\7\4\2\2\u00ae\17\3\2\2\2\u00af\u00b0\5\22\n\2")
        buf.write(u"\u00b0\u00b1\7\b\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00af")
        buf.write(u"\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4")
        buf.write(u"\u00b5\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2")
        buf.write(u"\2\u00b7\u00b8\5\22\n\2\u00b8\21\3\2\2\2\u00b9\u00ba")
        buf.write(u"\5z>\2\u00ba\u00bb\7\7\2\2\u00bb\u00bc\5&\24\2\u00bc")
        buf.write(u"\23\3\2\2\2\u00bd\u00be\5\26\f\2\u00be\u00bf\7\t\2\2")
        buf.write(u"\u00bf\25\3\2\2\2\u00c0\u00c1\5&\24\2\u00c1\u00c4\5z")
        buf.write(u">\2\u00c2\u00c3\7\n\2\2\u00c3\u00c5\5\30\r\2\u00c4\u00c2")
        buf.write(u"\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c9")
        buf.write(u"\5X-\2\u00c7\u00c9\5 \21\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write(u"\u00c7\3\2\2\2\u00c9\31\3\2\2\2\u00ca\u00cb\5z>\2\u00cb")
        buf.write(u"\u00cd\7\5\2\2\u00cc\u00ce\5\34\17\2\u00cd\u00cc\3\2")
        buf.write(u"\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write(u"\7\6\2\2\u00d0\33\3\2\2\2\u00d1\u00d2\5\36\20\2\u00d2")
        buf.write(u"\u00d3\7\b\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d1\3\2\2")
        buf.write(u"\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7")
        buf.write(u"\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9")
        buf.write(u"\u00da\5\36\20\2\u00da\35\3\2\2\2\u00db\u00dc\5z>\2\u00dc")
        buf.write(u"\u00dd\7\n\2\2\u00dd\u00de\5X-\2\u00de\37\3\2\2\2\u00df")
        buf.write(u"\u00e1\7\13\2\2\u00e0\u00e2\5\"\22\2\u00e1\u00e0\3\2")
        buf.write(u"\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4")
        buf.write(u"\7\f\2\2\u00e4!\3\2\2\2\u00e5\u00ea\5\30\r\2\u00e6\u00e7")
        buf.write(u"\7\b\2\2\u00e7\u00e9\5\30\r\2\u00e8\u00e6\3\2\2\2\u00e9")
        buf.write(u"\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2")
        buf.write(u"\2\u00eb#\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\7/")
        buf.write(u"\2\2\u00ee\u00ef\7\t\2\2\u00ef%\3\2\2\2\u00f0\u00f4\5")
        buf.write(u"(\25\2\u00f1\u00f4\5\64\33\2\u00f2\u00f4\5*\26\2\u00f3")
        buf.write(u"\u00f0\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2")
        buf.write(u"\2\u00f4\'\3\2\2\2\u00f5\u00f9\5,\27\2\u00f6\u00f9\5")
        buf.write(u".\30\2\u00f7\u00f9\5\60\31\2\u00f8\u00f5\3\2\2\2\u00f8")
        buf.write(u"\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9)\3\2\2\2\u00fa")
        buf.write(u"\u00fb\7\60\2\2\u00fb+\3\2\2\2\u00fc\u00fd\7\"\2\2\u00fd")
        buf.write(u"-\3\2\2\2\u00fe\u00ff\7#\2\2\u00ff/\3\2\2\2\u0100\u0101")
        buf.write(u"\7!\2\2\u0101\61\3\2\2\2\u0102\u0103\7$\2\2\u0103\63")
        buf.write(u"\3\2\2\2\u0104\u0105\7\13\2\2\u0105\u0106\5\66\34\2\u0106")
        buf.write(u"\u0107\7\f\2\2\u0107\65\3\2\2\2\u0108\u010d\5&\24\2\u0109")
        buf.write(u"\u010a\7\b\2\2\u010a\u010c\5&\24\2\u010b\u0109\3\2\2")
        buf.write(u"\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e")
        buf.write(u"\3\2\2\2\u010e\67\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0114")
        buf.write(u"\7\3\2\2\u0111\u0113\5:\36\2\u0112\u0111\3\2\2\2\u0113")
        buf.write(u"\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2")
        buf.write(u"\2\u0115\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118")
        buf.write(u"\7\4\2\2\u01189\3\2\2\2\u0119\u0124\58\35\2\u011a\u0124")
        buf.write(u"\5\24\13\2\u011b\u0124\5Z.\2\u011c\u0124\5H%\2\u011d")
        buf.write(u"\u0124\5R*\2\u011e\u0124\5B\"\2\u011f\u0124\5@!\2\u0120")
        buf.write(u"\u0124\5$\23\2\u0121\u0124\5N(\2\u0122\u0124\5J&\2\u0123")
        buf.write(u"\u0119\3\2\2\2\u0123\u011a\3\2\2\2\u0123\u011b\3\2\2")
        buf.write(u"\2\u0123\u011c\3\2\2\2\u0123\u011d\3\2\2\2\u0123\u011e")
        buf.write(u"\3\2\2\2\u0123\u011f\3\2\2\2\u0123\u0120\3\2\2\2\u0123")
        buf.write(u"\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124;\3\2\2\2\u0125")
        buf.write(u"\u0126\5> \2\u0126\u0127\7\t\2\2\u0127=\3\2\2\2\u0128")
        buf.write(u"\u012a\7-\2\2\u0129\u012b\5X-\2\u012a\u0129\3\2\2\2\u012a")
        buf.write(u"\u012b\3\2\2\2\u012b?\3\2\2\2\u012c\u012d\7*\2\2\u012d")
        buf.write(u"\u012e\7\5\2\2\u012e\u012f\5X-\2\u012f\u0130\7\6\2\2")
        buf.write(u"\u0130\u0131\58\35\2\u0131A\3\2\2\2\u0132\u0133\7)\2")
        buf.write(u"\2\u0133\u0135\7\5\2\2\u0134\u0136\5D#\2\u0135\u0134")
        buf.write(u"\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write(u"\u0139\7\t\2\2\u0138\u013a\5X-\2\u0139\u0138\3\2\2\2")
        buf.write(u"\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d")
        buf.write(u"\7\t\2\2\u013c\u013e\5F$\2\u013d\u013c\3\2\2\2\u013d")
        buf.write(u"\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\7\6\2")
        buf.write(u"\2\u0140\u0141\58\35\2\u0141C\3\2\2\2\u0142\u0145\5\\")
        buf.write(u"/\2\u0143\u0145\5\26\f\2\u0144\u0142\3\2\2\2\u0144\u0143")
        buf.write(u"\3\2\2\2\u0145E\3\2\2\2\u0146\u0149\5\\/\2\u0147\u0149")
        buf.write(u"\5T+\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write(u"G\3\2\2\2\u014a\u014b\7+\2\2\u014b\u014c\7\5\2\2\u014c")
        buf.write(u"\u014d\5X-\2\u014d\u014e\7\6\2\2\u014e\u0157\58\35\2")
        buf.write(u"\u014f\u0150\7,\2\2\u0150\u0151\7\5\2\2\u0151\u0152\5")
        buf.write(u"X-\2\u0152\u0153\7\6\2\2\u0153\u0154\58\35\2\u0154\u0156")
        buf.write(u"\3\2\2\2\u0155\u014f\3\2\2\2\u0156\u0159\3\2\2\2\u0157")
        buf.write(u"\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015c\3\2\2")
        buf.write(u"\2\u0159\u0157\3\2\2\2\u015a\u015b\7(\2\2\u015b\u015d")
        buf.write(u"\58\35\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write(u"I\3\2\2\2\u015e\u015f\5L\'\2\u015f\u0160\7\t\2\2\u0160")
        buf.write(u"K\3\2\2\2\u0161\u0162\7&\2\2\u0162\u0163\7\5\2\2\u0163")
        buf.write(u"\u0164\5V,\2\u0164\u0165\7\6\2\2\u0165M\3\2\2\2\u0166")
        buf.write(u"\u0167\5P)\2\u0167\u0168\7\t\2\2\u0168O\3\2\2\2\u0169")
        buf.write(u"\u016a\7\'\2\2\u016a\u016b\7\5\2\2\u016b\u0170\5^\60")
        buf.write(u"\2\u016c\u016d\7\b\2\2\u016d\u016f\5^\60\2\u016e\u016c")
        buf.write(u"\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write(u"\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2")
        buf.write(u"\2\u0173\u0174\7\6\2\2\u0174Q\3\2\2\2\u0175\u0176\5T")
        buf.write(u"+\2\u0176\u0177\7\t\2\2\u0177S\3\2\2\2\u0178\u0179\5")
        buf.write(u"z>\2\u0179\u017b\7\5\2\2\u017a\u017c\5V,\2\u017b\u017a")
        buf.write(u"\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write(u"\u017e\7\6\2\2\u017eU\3\2\2\2\u017f\u0184\5X-\2\u0180")
        buf.write(u"\u0181\7\b\2\2\u0181\u0183\5X-\2\u0182\u0180\3\2\2\2")
        buf.write(u"\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185")
        buf.write(u"\3\2\2\2\u0185W\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188")
        buf.write(u"\b-\1\2\u0188\u0189\5l\67\2\u0189\u018a\5X-\20\u018a")
        buf.write(u"\u0198\3\2\2\2\u018b\u0198\5\\/\2\u018c\u0198\5T+\2\u018d")
        buf.write(u"\u0198\5d\63\2\u018e\u0198\5 \21\2\u018f\u0198\5\32\16")
        buf.write(u"\2\u0190\u0198\5z>\2\u0191\u0198\5`\61\2\u0192\u0198")
        buf.write(u"\5b\62\2\u0193\u0194\7\5\2\2\u0194\u0195\5X-\2\u0195")
        buf.write(u"\u0196\7\6\2\2\u0196\u0198\3\2\2\2\u0197\u0187\3\2\2")
        buf.write(u"\2\u0197\u018b\3\2\2\2\u0197\u018c\3\2\2\2\u0197\u018d")
        buf.write(u"\3\2\2\2\u0197\u018e\3\2\2\2\u0197\u018f\3\2\2\2\u0197")
        buf.write(u"\u0190\3\2\2\2\u0197\u0191\3\2\2\2\u0197\u0192\3\2\2")
        buf.write(u"\2\u0197\u0193\3\2\2\2\u0198\u01af\3\2\2\2\u0199\u019a")
        buf.write(u"\f\17\2\2\u019a\u019b\5n8\2\u019b\u019c\5X-\20\u019c")
        buf.write(u"\u01ae\3\2\2\2\u019d\u019e\f\16\2\2\u019e\u019f\5p9\2")
        buf.write(u"\u019f\u01a0\5X-\17\u01a0\u01ae\3\2\2\2\u01a1\u01a2\f")
        buf.write(u"\r\2\2\u01a2\u01a3\5r:\2\u01a3\u01a4\5X-\16\u01a4\u01ae")
        buf.write(u"\3\2\2\2\u01a5\u01a6\f\f\2\2\u01a6\u01a7\5t;\2\u01a7")
        buf.write(u"\u01a8\5X-\r\u01a8\u01ae\3\2\2\2\u01a9\u01aa\f\13\2\2")
        buf.write(u"\u01aa\u01ab\5v<\2\u01ab\u01ac\5X-\f\u01ac\u01ae\3\2")
        buf.write(u"\2\2\u01ad\u0199\3\2\2\2\u01ad\u019d\3\2\2\2\u01ad\u01a1")
        buf.write(u"\3\2\2\2\u01ad\u01a5\3\2\2\2\u01ad\u01a9\3\2\2\2\u01ae")
        buf.write(u"\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2")
        buf.write(u"\2\u01b0Y\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\5\\")
        buf.write(u"/\2\u01b3\u01b4\7\t\2\2\u01b4[\3\2\2\2\u01b5\u01b6\5")
        buf.write(u"^\60\2\u01b6\u01b7\5x=\2\u01b7\u01b8\5X-\2\u01b8]\3\2")
        buf.write(u"\2\2\u01b9\u01bd\5z>\2\u01ba\u01bd\5`\61\2\u01bb\u01bd")
        buf.write(u"\5b\62\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write(u"\u01bb\3\2\2\2\u01bd_\3\2\2\2\u01be\u01bf\5z>\2\u01bf")
        buf.write(u"\u01c0\7\13\2\2\u01c0\u01c1\5X-\2\u01c1\u01c2\7\f\2\2")
        buf.write(u"\u01c2a\3\2\2\2\u01c3\u01c4\5z>\2\u01c4\u01c5\7\r\2\2")
        buf.write(u"\u01c5\u01c6\5^\60\2\u01c6c\3\2\2\2\u01c7\u01cb\5f\64")
        buf.write(u"\2\u01c8\u01cb\5h\65\2\u01c9\u01cb\5j\66\2\u01ca\u01c7")
        buf.write(u"\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb")
        buf.write(u"e\3\2\2\2\u01cc\u01cd\7\63\2\2\u01cdg\3\2\2\2\u01ce\u01cf")
        buf.write(u"\7\62\2\2\u01cfi\3\2\2\2\u01d0\u01d1\7\61\2\2\u01d1k")
        buf.write(u"\3\2\2\2\u01d2\u01d3\t\2\2\2\u01d3m\3\2\2\2\u01d4\u01d5")
        buf.write(u"\t\3\2\2\u01d5o\3\2\2\2\u01d6\u01d7\t\4\2\2\u01d7q\3")
        buf.write(u"\2\2\2\u01d8\u01d9\t\5\2\2\u01d9s\3\2\2\2\u01da\u01db")
        buf.write(u"\t\6\2\2\u01dbu\3\2\2\2\u01dc\u01dd\t\7\2\2\u01ddw\3")
        buf.write(u"\2\2\2\u01de\u01df\t\b\2\2\u01dfy\3\2\2\2\u01e0\u01e1")
        buf.write(u"\7\60\2\2\u01e1{\3\2\2\2%\u0080\u0082\u008d\u0099\u00a1")
        buf.write(u"\u00a7\u00ab\u00b4\u00c4\u00c8\u00cd\u00d6\u00e1\u00ea")
        buf.write(u"\u00f3\u00f8\u010d\u0114\u0123\u012a\u0135\u0139\u013d")
        buf.write(u"\u0144\u0148\u0157\u015c\u0170\u017b\u0184\u0197\u01ad")
        buf.write(u"\u01af\u01bc\u01ca")
        return buf.getvalue()
		

class LLangParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"'('", u"')'", u"':'", 
                     u"','", u"';'", u"'='", u"'['", u"']'", u"'.'", u"'-'", 
                     u"'!'", u"'*'", u"'/'", u"'%'", u"'+'", u"'>'", u"'>='", 
                     u"'<'", u"'<='", u"'=='", u"'!='", u"'&&'", u"'||'", 
                     u"'*='", u"'/='", u"'%='", u"'+='", u"'-='", u"'Bool'", 
                     u"'Int'", u"'Str'", u"'None'", u"'record'", u"'writeln'", 
                     u"'readln'", u"'else'", u"'for'", u"'while'", u"'if'", 
                     u"'elif'", u"'return'", u"'fun'", u"'pass'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"BOOL", 
                      u"INT", u"STR", u"NONE", u"RECORD", u"WRITELN", u"READLN", 
                      u"ELSE", u"FOR", u"WHILE", u"IF", u"ELIF", u"RETURN", 
                      u"FUN", u"PASS", u"Identifier", u"BooleanLiteral", 
                      u"StringLiteral", u"IntegerLiteral", u"WS", u"COMMENT", 
                      u"LINE_COMMENT" ]

    RULE_programme = 0
    RULE_recordDeclaration = 1
    RULE_recordBody = 2
    RULE_functionDeclaration = 3
    RULE_functionSignature = 4
    RULE_functionReturnType = 5
    RULE_functionBody = 6
    RULE_functionParameterList = 7
    RULE_functionParameter = 8
    RULE_variableDeclarationStatement = 9
    RULE_variableDeclaration = 10
    RULE_variableInitializer = 11
    RULE_recordInitializer = 12
    RULE_recordFieldInitializerList = 13
    RULE_recordFieldInitializer = 14
    RULE_cortegeInitializer = 15
    RULE_variableInitializerNonEmptyList = 16
    RULE_passStatement = 17
    RULE_exprType = 18
    RULE_primitiveType = 19
    RULE_recordType = 20
    RULE_intType = 21
    RULE_strType = 22
    RULE_boolType = 23
    RULE_voidType = 24
    RULE_cortegeType = 25
    RULE_typeNonEmptyList = 26
    RULE_block = 27
    RULE_statement = 28
    RULE_returnStatement = 29
    RULE_returnExpr = 30
    RULE_whileStatement = 31
    RULE_forStatement = 32
    RULE_forInit = 33
    RULE_forUpdate = 34
    RULE_ifStatement = 35
    RULE_writelnStatement = 36
    RULE_writelnCall = 37
    RULE_readlnStatement = 38
    RULE_readlnCall = 39
    RULE_functionInvocationStatement = 40
    RULE_functionInvocation = 41
    RULE_argumentList = 42
    RULE_expression = 43
    RULE_assignmentStatement = 44
    RULE_assignment = 45
    RULE_leftHandSide = 46
    RULE_cortegeAccess = 47
    RULE_recordFieldAccess = 48
    RULE_literal = 49
    RULE_intLiteral = 50
    RULE_strLiteral = 51
    RULE_boolLiteral = 52
    RULE_unaryOperator = 53
    RULE_mulDivModOperator = 54
    RULE_addSubOperator = 55
    RULE_compareOperator = 56
    RULE_equalOrNotOperator = 57
    RULE_boolOperator = 58
    RULE_assignmentOperator = 59
    RULE_identifier = 60

    ruleNames =  [ u"programme", u"recordDeclaration", u"recordBody", u"functionDeclaration", 
                   u"functionSignature", u"functionReturnType", u"functionBody", 
                   u"functionParameterList", u"functionParameter", u"variableDeclarationStatement", 
                   u"variableDeclaration", u"variableInitializer", u"recordInitializer", 
                   u"recordFieldInitializerList", u"recordFieldInitializer", 
                   u"cortegeInitializer", u"variableInitializerNonEmptyList", 
                   u"passStatement", u"exprType", u"primitiveType", u"recordType", 
                   u"intType", u"strType", u"boolType", u"voidType", u"cortegeType", 
                   u"typeNonEmptyList", u"block", u"statement", u"returnStatement", 
                   u"returnExpr", u"whileStatement", u"forStatement", u"forInit", 
                   u"forUpdate", u"ifStatement", u"writelnStatement", u"writelnCall", 
                   u"readlnStatement", u"readlnCall", u"functionInvocationStatement", 
                   u"functionInvocation", u"argumentList", u"expression", 
                   u"assignmentStatement", u"assignment", u"leftHandSide", 
                   u"cortegeAccess", u"recordFieldAccess", u"literal", u"intLiteral", 
                   u"strLiteral", u"boolLiteral", u"unaryOperator", u"mulDivModOperator", 
                   u"addSubOperator", u"compareOperator", u"equalOrNotOperator", 
                   u"boolOperator", u"assignmentOperator", u"identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    BOOL=31
    INT=32
    STR=33
    NONE=34
    RECORD=35
    WRITELN=36
    READLN=37
    ELSE=38
    FOR=39
    WHILE=40
    IF=41
    ELIF=42
    RETURN=43
    FUN=44
    PASS=45
    Identifier=46
    BooleanLiteral=47
    StringLiteral=48
    IntegerLiteral=49
    WS=50
    COMMENT=51
    LINE_COMMENT=52

    def __init__(self, input):
        super(LLangParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgrammeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ProgrammeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationStatement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.VariableDeclarationStatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.VariableDeclarationStatementContext,i)


        def functionDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(LLangParser.FunctionDeclarationContext,i)


        def recordDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.RecordDeclarationContext)
            else:
                return self.getTypedRuleContext(LLangParser.RecordDeclarationContext,i)


        def block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.BlockContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_programme

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterProgramme(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitProgramme(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitProgramme(self)
            else:
                return visitor.visitChildren(self)




    def programme(self):

        localctx = LLangParser.ProgrammeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__8) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.RECORD) | (1 << LLangParser.FUN) | (1 << LLangParser.Identifier))) != 0):
                self.state = 126
                token = self._input.LA(1)
                if token in [LLangParser.T__8, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                    self.state = 122 
                    self.variableDeclarationStatement()

                elif token in [LLangParser.FUN]:
                    self.state = 123 
                    self.functionDeclaration()

                elif token in [LLangParser.RECORD]:
                    self.state = 124 
                    self.recordDeclaration()

                elif token in [LLangParser.T__0]:
                    self.state = 125 
                    self.block()

                else:
                    raise NoViableAltException(self)

                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self):
            return self.getToken(LLangParser.RECORD, 0)

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def recordBody(self):
            return self.getTypedRuleContext(LLangParser.RecordBodyContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordDeclaration

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def recordDeclaration(self):

        localctx = LLangParser.RecordDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_recordDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LLangParser.RECORD)
            self.state = 132 
            self.identifier()
            self.state = 133 
            self.recordBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationStatement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.VariableDeclarationStatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.VariableDeclarationStatementContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_recordBody

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordBody(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordBody(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordBody(self)
            else:
                return visitor.visitChildren(self)




    def recordBody(self):

        localctx = LLangParser.RecordBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_recordBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(LLangParser.T__0)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__8) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 136 
                self.variableDeclarationStatement()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(LLangParser.FUN, 0)

        def functionSignature(self):
            return self.getTypedRuleContext(LLangParser.FunctionSignatureContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(LLangParser.FunctionBodyContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionDeclaration

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = LLangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(LLangParser.FUN)
            self.state = 145 
            self.functionSignature()
            self.state = 146 
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionSignatureContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionSignatureContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def functionReturnType(self):
            return self.getTypedRuleContext(LLangParser.FunctionReturnTypeContext,0)


        def functionParameterList(self):
            return self.getTypedRuleContext(LLangParser.FunctionParameterListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionSignature

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionSignature(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionSignature(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionSignature(self)
            else:
                return visitor.visitChildren(self)




    def functionSignature(self):

        localctx = LLangParser.FunctionSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148 
            self.identifier()
            self.state = 149
            self.match(LLangParser.T__2)
            self.state = 151
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 150 
                self.functionParameterList()


            self.state = 153
            self.match(LLangParser.T__3)
            self.state = 154
            self.match(LLangParser.T__4)
            self.state = 155 
            self.functionReturnType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionReturnTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprType(self):
            return self.getTypedRuleContext(LLangParser.ExprTypeContext,0)


        def voidType(self):
            return self.getTypedRuleContext(LLangParser.VoidTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionReturnType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionReturnType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionReturnType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionReturnType(self)
            else:
                return visitor.visitChildren(self)




    def functionReturnType(self):

        localctx = LLangParser.FunctionReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionReturnType)
        try:
            self.state = 159
            token = self._input.LA(1)
            if token in [LLangParser.T__8, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157 
                self.exprType()

            elif token in [LLangParser.NONE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158 
                self.voidType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.StatementContext,i)


        def returnStatement(self):
            return self.getTypedRuleContext(LLangParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionBody

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionBody(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = LLangParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LLangParser.T__0)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__8) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 162 
                self.statement()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            _la = self._input.LA(1)
            if _la==LLangParser.RETURN:
                self.state = 168 
                self.returnStatement()


            self.state = 171
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def functionParameter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.FunctionParameterContext)
            else:
                return self.getTypedRuleContext(LLangParser.FunctionParameterContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_functionParameterList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionParameterList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionParameterList(self)
            else:
                return visitor.visitChildren(self)




    def functionParameterList(self):

        localctx = LLangParser.FunctionParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173 
                    self.functionParameter()
                    self.state = 174
                    self.match(LLangParser.T__5) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 181 
            self.functionParameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionParameterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionParameterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def exprType(self):
            return self.getTypedRuleContext(LLangParser.ExprTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionParameter

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionParameter(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionParameter(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionParameter(self)
            else:
                return visitor.visitChildren(self)




    def functionParameter(self):

        localctx = LLangParser.FunctionParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183 
            self.identifier()
            self.state = 184
            self.match(LLangParser.T__4)
            self.state = 185 
            self.exprType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableDeclarationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(LLangParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_variableDeclarationStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableDeclarationStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableDeclarationStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationStatement(self):

        localctx = LLangParser.VariableDeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDeclarationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187 
            self.variableDeclaration()
            self.state = 188
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprType(self):
            return self.getTypedRuleContext(LLangParser.ExprTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def variableInitializer(self):
            return self.getTypedRuleContext(LLangParser.VariableInitializerContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_variableDeclaration

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = LLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190 
            self.exprType()
            self.state = 191 
            self.identifier()
            self.state = 194
            _la = self._input.LA(1)
            if _la==LLangParser.T__7:
                self.state = 192
                self.match(LLangParser.T__7)
                self.state = 193 
                self.variableInitializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def cortegeInitializer(self):
            return self.getTypedRuleContext(LLangParser.CortegeInitializerContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_variableInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableInitializer(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializer(self):

        localctx = LLangParser.VariableInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variableInitializer)
        try:
            self.state = 198
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196 
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197 
                self.cortegeInitializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def recordFieldInitializerList(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldInitializerListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordInitializer(self)
            else:
                return visitor.visitChildren(self)




    def recordInitializer(self):

        localctx = LLangParser.RecordInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_recordInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200 
            self.identifier()
            self.state = 201
            self.match(LLangParser.T__2)
            self.state = 203
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 202 
                self.recordFieldInitializerList()


            self.state = 205
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordFieldInitializerListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldInitializerListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def recordFieldInitializer(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.RecordFieldInitializerContext)
            else:
                return self.getTypedRuleContext(LLangParser.RecordFieldInitializerContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_recordFieldInitializerList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordFieldInitializerList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordFieldInitializerList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordFieldInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldInitializerList(self):

        localctx = LLangParser.RecordFieldInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_recordFieldInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 207 
                    self.recordFieldInitializer()
                    self.state = 208
                    self.match(LLangParser.T__5) 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 215 
            self.recordFieldInitializer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordFieldInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordFieldInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordFieldInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordFieldInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordFieldInitializer(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldInitializer(self):

        localctx = LLangParser.RecordFieldInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_recordFieldInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217 
            self.identifier()
            self.state = 218
            self.match(LLangParser.T__7)
            self.state = 219 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeInitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableInitializerNonEmptyList(self):
            return self.getTypedRuleContext(LLangParser.VariableInitializerNonEmptyListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeInitializer

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeInitializer(self)
            else:
                return visitor.visitChildren(self)




    def cortegeInitializer(self):

        localctx = LLangParser.CortegeInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cortegeInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(LLangParser.T__8)
            self.state = 223
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__11) | (1 << LLangParser.T__12) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 222 
                self.variableInitializerNonEmptyList()


            self.state = 225
            self.match(LLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableInitializerNonEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VariableInitializerNonEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableInitializer(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.VariableInitializerContext)
            else:
                return self.getTypedRuleContext(LLangParser.VariableInitializerContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_variableInitializerNonEmptyList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVariableInitializerNonEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVariableInitializerNonEmptyList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVariableInitializerNonEmptyList(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializerNonEmptyList(self):

        localctx = LLangParser.VariableInitializerNonEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variableInitializerNonEmptyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227 
            self.variableInitializer()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 228
                self.match(LLangParser.T__5)
                self.state = 229 
                self.variableInitializer()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PassStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.PassStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PASS(self):
            return self.getToken(LLangParser.PASS, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_passStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterPassStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitPassStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitPassStatement(self)
            else:
                return visitor.visitChildren(self)




    def passStatement(self):

        localctx = LLangParser.PassStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_passStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(LLangParser.PASS)
            self.state = 236
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ExprTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(LLangParser.PrimitiveTypeContext,0)


        def cortegeType(self):
            return self.getTypedRuleContext(LLangParser.CortegeTypeContext,0)


        def recordType(self):
            return self.getTypedRuleContext(LLangParser.RecordTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_exprType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterExprType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitExprType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitExprType(self)
            else:
                return visitor.visitChildren(self)




    def exprType(self):

        localctx = LLangParser.ExprTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprType)
        try:
            self.state = 241
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238 
                self.primitiveType()

            elif token in [LLangParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239 
                self.cortegeType()

            elif token in [LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240 
                self.recordType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.PrimitiveTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def intType(self):
            return self.getTypedRuleContext(LLangParser.IntTypeContext,0)


        def strType(self):
            return self.getTypedRuleContext(LLangParser.StrTypeContext,0)


        def boolType(self):
            return self.getTypedRuleContext(LLangParser.BoolTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_primitiveType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = LLangParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitiveType)
        try:
            self.state = 246
            token = self._input.LA(1)
            if token in [LLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243 
                self.intType()

            elif token in [LLangParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244 
                self.strType()

            elif token in [LLangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245 
                self.boolType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LLangParser.Identifier, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_recordType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordType(self)
            else:
                return visitor.visitChildren(self)




    def recordType(self):

        localctx = LLangParser.RecordTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_recordType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(LLangParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IntTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LLangParser.INT, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_intType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIntType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIntType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)




    def intType(self):

        localctx = LLangParser.IntTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_intType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(LLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.StrTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(LLangParser.STR, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_strType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterStrType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitStrType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitStrType(self)
            else:
                return visitor.visitChildren(self)




    def strType(self):

        localctx = LLangParser.StrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_strType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(LLangParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BoolTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(LLangParser.BOOL, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_boolType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBoolType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBoolType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBoolType(self)
            else:
                return visitor.visitChildren(self)




    def boolType(self):

        localctx = LLangParser.BoolTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_boolType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(LLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VoidTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.VoidTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(LLangParser.NONE, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_voidType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterVoidType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitVoidType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitVoidType(self)
            else:
                return visitor.visitChildren(self)




    def voidType(self):

        localctx = LLangParser.VoidTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_voidType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(LLangParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeTypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeTypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeNonEmptyList(self):
            return self.getTypedRuleContext(LLangParser.TypeNonEmptyListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeType

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeType(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeType(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeType(self)
            else:
                return visitor.visitChildren(self)




    def cortegeType(self):

        localctx = LLangParser.CortegeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cortegeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(LLangParser.T__8)
            self.state = 259 
            self.typeNonEmptyList()
            self.state = 260
            self.match(LLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeNonEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.TypeNonEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprType(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExprTypeContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExprTypeContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_typeNonEmptyList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterTypeNonEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitTypeNonEmptyList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitTypeNonEmptyList(self)
            else:
                return visitor.visitChildren(self)




    def typeNonEmptyList(self):

        localctx = LLangParser.TypeNonEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typeNonEmptyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262 
            self.exprType()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 263
                self.match(LLangParser.T__5)
                self.state = 264 
                self.exprType()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LLangParser.StatementContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(LLangParser.T__0)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__8) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 271 
                self.statement()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def variableDeclarationStatement(self):
            return self.getTypedRuleContext(LLangParser.VariableDeclarationStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(LLangParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(LLangParser.IfStatementContext,0)


        def functionInvocationStatement(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(LLangParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(LLangParser.WhileStatementContext,0)


        def passStatement(self):
            return self.getTypedRuleContext(LLangParser.PassStatementContext,0)


        def readlnStatement(self):
            return self.getTypedRuleContext(LLangParser.ReadlnStatementContext,0)


        def writelnStatement(self):
            return self.getTypedRuleContext(LLangParser.WritelnStatementContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 289
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279 
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280 
                self.variableDeclarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281 
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282 
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283 
                self.functionInvocationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 284 
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285 
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 286 
                self.passStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 287 
                self.readlnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 288 
                self.writelnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReturnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def returnExpr(self):
            return self.getTypedRuleContext(LLangParser.ReturnExprContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_returnStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReturnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = LLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self.returnExpr()
            self.state = 292
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReturnExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LLangParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_returnExpr

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReturnExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReturnExpr(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReturnExpr(self)
            else:
                return visitor.visitChildren(self)




    def returnExpr(self):

        localctx = LLangParser.ReturnExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(LLangParser.RETURN)
            self.state = 296
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__11) | (1 << LLangParser.T__12) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 295 
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.WhileStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_whileStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitWhileStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = LLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(LLangParser.WHILE)
            self.state = 299
            self.match(LLangParser.T__2)
            self.state = 300 
            self.expression(0)
            self.state = 301
            self.match(LLangParser.T__3)
            self.state = 302 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LLangParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(LLangParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(LLangParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = LLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(LLangParser.FOR)
            self.state = 305
            self.match(LLangParser.T__2)
            self.state = 307
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__8) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 306 
                self.forInit()


            self.state = 309
            self.match(LLangParser.T__6)
            self.state = 311
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__11) | (1 << LLangParser.T__12) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 310 
                self.expression(0)


            self.state = 313
            self.match(LLangParser.T__6)
            self.state = 315
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 314 
                self.forUpdate()


            self.state = 317
            self.match(LLangParser.T__3)
            self.state = 318 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForInitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForInitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(LLangParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forInit

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForInit(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForInit(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = LLangParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forInit)
        try:
            self.state = 322
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321 
                self.variableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForUpdateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ForUpdateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_forUpdate

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterForUpdate(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitForUpdate(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = LLangParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forUpdate)
        try:
            self.state = 326
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325 
                self.functionInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LLangParser.IF, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.BlockContext,i)


        def ELIF(self, i=None):
            if i is None:
                return self.getTokens(LLangParser.ELIF)
            else:
                return self.getToken(LLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(LLangParser.ELSE, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_ifStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIfStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = LLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(LLangParser.IF)
            self.state = 329
            self.match(LLangParser.T__2)
            self.state = 330 
            self.expression(0)
            self.state = 331
            self.match(LLangParser.T__3)
            self.state = 332 
            self.block()
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.ELIF:
                self.state = 333
                self.match(LLangParser.ELIF)
                self.state = 334
                self.match(LLangParser.T__2)
                self.state = 335 
                self.expression(0)
                self.state = 336
                self.match(LLangParser.T__3)
                self.state = 337 
                self.block()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            _la = self._input.LA(1)
            if _la==LLangParser.ELSE:
                self.state = 344
                self.match(LLangParser.ELSE)
                self.state = 345 
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritelnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.WritelnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def writelnCall(self):
            return self.getTypedRuleContext(LLangParser.WritelnCallContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_writelnStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterWritelnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitWritelnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitWritelnStatement(self)
            else:
                return visitor.visitChildren(self)




    def writelnStatement(self):

        localctx = LLangParser.WritelnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_writelnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348 
            self.writelnCall()
            self.state = 349
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritelnCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.WritelnCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WRITELN(self):
            return self.getToken(LLangParser.WRITELN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(LLangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_writelnCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterWritelnCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitWritelnCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitWritelnCall(self)
            else:
                return visitor.visitChildren(self)




    def writelnCall(self):

        localctx = LLangParser.WritelnCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_writelnCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(LLangParser.WRITELN)
            self.state = 352
            self.match(LLangParser.T__2)
            self.state = 353 
            self.argumentList()
            self.state = 354
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadlnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadlnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def readlnCall(self):
            return self.getTypedRuleContext(LLangParser.ReadlnCallContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_readlnStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadlnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadlnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadlnStatement(self)
            else:
                return visitor.visitChildren(self)




    def readlnStatement(self):

        localctx = LLangParser.ReadlnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_readlnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356 
            self.readlnCall()
            self.state = 357
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadlnCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ReadlnCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def READLN(self):
            return self.getToken(LLangParser.READLN, 0)

        def leftHandSide(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.LeftHandSideContext)
            else:
                return self.getTypedRuleContext(LLangParser.LeftHandSideContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_readlnCall

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterReadlnCall(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitReadlnCall(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitReadlnCall(self)
            else:
                return visitor.visitChildren(self)




    def readlnCall(self):

        localctx = LLangParser.ReadlnCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_readlnCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(LLangParser.READLN)
            self.state = 360
            self.match(LLangParser.T__2)
            self.state = 361 
            self.leftHandSide()
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 362
                self.match(LLangParser.T__5)
                self.state = 363 
                self.leftHandSide()
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionInvocationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionInvocationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionInvocationStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionInvocationStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionInvocationStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionInvocationStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionInvocationStatement(self):

        localctx = LLangParser.FunctionInvocationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_functionInvocationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371 
            self.functionInvocation()
            self.state = 372
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.FunctionInvocationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(LLangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_functionInvocation

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterFunctionInvocation(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitFunctionInvocation(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitFunctionInvocation(self)
            else:
                return visitor.visitChildren(self)




    def functionInvocation(self):

        localctx = LLangParser.FunctionInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_functionInvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374 
            self.identifier()
            self.state = 375
            self.match(LLangParser.T__2)
            self.state = 377
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__11) | (1 << LLangParser.T__12) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 376 
                self.argumentList()


            self.state = 379
            self.match(LLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ArgumentListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_argumentList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitArgumentList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = LLangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381 
            self.expression(0)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 382
                self.match(LLangParser.T__5)
                self.state = 383 
                self.expression(0)
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(LLangParser.UnaryOperatorContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def literal(self):
            return self.getTypedRuleContext(LLangParser.LiteralContext,0)


        def cortegeInitializer(self):
            return self.getTypedRuleContext(LLangParser.CortegeInitializerContext,0)


        def recordInitializer(self):
            return self.getTypedRuleContext(LLangParser.RecordInitializerContext,0)


        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


        def mulDivModOperator(self):
            return self.getTypedRuleContext(LLangParser.MulDivModOperatorContext,0)


        def addSubOperator(self):
            return self.getTypedRuleContext(LLangParser.AddSubOperatorContext,0)


        def compareOperator(self):
            return self.getTypedRuleContext(LLangParser.CompareOperatorContext,0)


        def equalOrNotOperator(self):
            return self.getTypedRuleContext(LLangParser.EqualOrNotOperatorContext,0)


        def boolOperator(self):
            return self.getTypedRuleContext(LLangParser.BoolOperatorContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 390 
                self.unaryOperator()
                self.state = 391 
                self.expression(14)
                pass

            elif la_ == 2:
                self.state = 393 
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 394 
                self.functionInvocation()
                pass

            elif la_ == 4:
                self.state = 395 
                self.literal()
                pass

            elif la_ == 5:
                self.state = 396 
                self.cortegeInitializer()
                pass

            elif la_ == 6:
                self.state = 397 
                self.recordInitializer()
                pass

            elif la_ == 7:
                self.state = 398 
                self.identifier()
                pass

            elif la_ == 8:
                self.state = 399 
                self.cortegeAccess()
                pass

            elif la_ == 9:
                self.state = 400 
                self.recordFieldAccess()
                pass

            elif la_ == 10:
                self.state = 401
                self.match(LLangParser.T__2)
                self.state = 402 
                self.expression(0)
                self.state = 403
                self.match(LLangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 427
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 407
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 408 
                        self.mulDivModOperator()
                        self.state = 409 
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 411
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 412 
                        self.addSubOperator()
                        self.state = 413 
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 415
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 416 
                        self.compareOperator()
                        self.state = 417 
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 419
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 420 
                        self.equalOrNotOperator()
                        self.state = 421 
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 423
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 424 
                        self.boolOperator()
                        self.state = 425 
                        self.expression(10)
                        pass

             
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AssignmentStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_assignmentStatement

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = LLangParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432 
            self.assignment()
            self.state = 433
            self.match(LLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def leftHandSide(self):
            return self.getTypedRuleContext(LLangParser.LeftHandSideContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(LLangParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_assignment

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAssignment(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435 
            self.leftHandSide()
            self.state = 436 
            self.assignmentOperator()
            self.state = 437 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LeftHandSideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.LeftHandSideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_leftHandSide

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterLeftHandSide(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitLeftHandSide(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitLeftHandSide(self)
            else:
                return visitor.visitChildren(self)




    def leftHandSide(self):

        localctx = LLangParser.LeftHandSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_leftHandSide)
        try:
            self.state = 442
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439 
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440 
                self.cortegeAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441 
                self.recordFieldAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeAccessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeAccessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeAccess

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeAccess(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeAccess(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeAccess(self)
            else:
                return visitor.visitChildren(self)




    def cortegeAccess(self):

        localctx = LLangParser.CortegeAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_cortegeAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444 
            self.identifier()
            self.state = 445
            self.match(LLangParser.T__8)
            self.state = 446 
            self.expression(0)
            self.state = 447
            self.match(LLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecordFieldAccessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldAccessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def leftHandSide(self):
            return self.getTypedRuleContext(LLangParser.LeftHandSideContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_recordFieldAccess

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordFieldAccess(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordFieldAccess(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldAccess(self):

        localctx = LLangParser.RecordFieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_recordFieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449 
            self.identifier()
            self.state = 450
            self.match(LLangParser.T__10)
            self.state = 451 
            self.leftHandSide()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def intLiteral(self):
            return self.getTypedRuleContext(LLangParser.IntLiteralContext,0)


        def strLiteral(self):
            return self.getTypedRuleContext(LLangParser.StrLiteralContext,0)


        def boolLiteral(self):
            return self.getTypedRuleContext(LLangParser.BoolLiteralContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_literal

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal)
        try:
            self.state = 456
            token = self._input.LA(1)
            if token in [LLangParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453 
                self.intLiteral()

            elif token in [LLangParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454 
                self.strLiteral()

            elif token in [LLangParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 455 
                self.boolLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IntLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(LLangParser.IntegerLiteral, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_intLiteral

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIntLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)




    def intLiteral(self):

        localctx = LLangParser.IntLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(LLangParser.IntegerLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.StrLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(LLangParser.StringLiteral, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_strLiteral

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterStrLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitStrLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitStrLiteral(self)
            else:
                return visitor.visitChildren(self)




    def strLiteral(self):

        localctx = LLangParser.StrLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_strLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(LLangParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BoolLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BooleanLiteral(self):
            return self.getToken(LLangParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_boolLiteral

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)




    def boolLiteral(self):

        localctx = LLangParser.BoolLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boolLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(LLangParser.BooleanLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.UnaryOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_unaryOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitUnaryOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryOperator(self):

        localctx = LLangParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__11 or _la==LLangParser.T__12):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulDivModOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.MulDivModOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_mulDivModOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterMulDivModOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitMulDivModOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitMulDivModOperator(self)
            else:
                return visitor.visitChildren(self)




    def mulDivModOperator(self):

        localctx = LLangParser.MulDivModOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_mulDivModOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__13) | (1 << LLangParser.T__14) | (1 << LLangParser.T__15))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddSubOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AddSubOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_addSubOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAddSubOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAddSubOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAddSubOperator(self)
            else:
                return visitor.visitChildren(self)




    def addSubOperator(self):

        localctx = LLangParser.AddSubOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_addSubOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__11 or _la==LLangParser.T__16):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompareOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CompareOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_compareOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCompareOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCompareOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCompareOperator(self)
            else:
                return visitor.visitChildren(self)




    def compareOperator(self):

        localctx = LLangParser.CompareOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_compareOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__17) | (1 << LLangParser.T__18) | (1 << LLangParser.T__19) | (1 << LLangParser.T__20))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EqualOrNotOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.EqualOrNotOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_equalOrNotOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterEqualOrNotOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitEqualOrNotOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitEqualOrNotOperator(self)
            else:
                return visitor.visitChildren(self)




    def equalOrNotOperator(self):

        localctx = LLangParser.EqualOrNotOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_equalOrNotOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__21 or _la==LLangParser.T__22):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.BoolOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_boolOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterBoolOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitBoolOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitBoolOperator(self)
            else:
                return visitor.visitChildren(self)




    def boolOperator(self):

        localctx = LLangParser.BoolOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_boolOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__23 or _la==LLangParser.T__24):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.AssignmentOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLangParser.RULE_assignmentOperator

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = LLangParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__7) | (1 << LLangParser.T__25) | (1 << LLangParser.T__26) | (1 << LLangParser.T__27) | (1 << LLangParser.T__28) | (1 << LLangParser.T__29))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LLangParser.Identifier, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_identifier

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitIdentifier(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = LLangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(LLangParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[43] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         



