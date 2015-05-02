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
        buf.write(u"\67\u01fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\3\2\3\2\3\2\3\2\7\2\u0087\n\2\f\2\16\2\u008a\13\2\3")
        buf.write(u"\3\3\3\3\3\3\3\3\4\3\4\7\4\u0092\n\4\f\4\16\4\u0095\13")
        buf.write(u"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00a0\n\6")
        buf.write(u"\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u00a8\n\7\3\b\3\b\7\b\u00ac")
        buf.write(u"\n\b\f\b\16\b\u00af\13\b\3\b\5\b\u00b2\n\b\3\b\3\b\3")
        buf.write(u"\t\3\t\3\t\7\t\u00b9\n\t\f\t\16\t\u00bc\13\t\3\t\3\t")
        buf.write(u"\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00cb")
        buf.write(u"\n\f\3\r\3\r\3\r\3\r\5\r\u00d1\n\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\7\16\u00d8\n\16\f\16\16\16\u00db\13\16\3\16\3\16")
        buf.write(u"\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00e5\n\20\3\20\3")
        buf.write(u"\20\3\21\3\21\3\21\7\21\u00ec\n\21\f\21\16\21\u00ef\13")
        buf.write(u"\21\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00f7\n\23\3\24")
        buf.write(u"\3\24\3\24\5\24\u00fc\n\24\3\25\3\25\3\26\3\26\3\27\3")
        buf.write(u"\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write(u"\5\33\u010e\n\33\3\34\3\34\3\34\7\34\u0113\n\34\f\34")
        buf.write(u"\16\34\u0116\13\34\3\35\3\35\7\35\u011a\n\35\f\35\16")
        buf.write(u"\35\u011d\13\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u012d\n\37\3 ")
        buf.write(u"\3 \3 \3!\3!\5!\u0134\n!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write(u"#\3#\5#\u013f\n#\3#\3#\5#\u0143\n#\3#\3#\5#\u0147\n#")
        buf.write(u"\3#\3#\3#\3$\3$\5$\u014e\n$\3%\3%\5%\u0152\n%\3&\3&\3")
        buf.write(u"&\3&\3&\3&\7&\u015a\n&\f&\16&\u015d\13&\3&\5&\u0160\n")
        buf.write(u"&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*")
        buf.write(u"\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\7,\u017b\n,\f,\16,\u017e")
        buf.write(u"\13,\3,\3,\3-\3-\3-\3.\3.\3.\5.\u0188\n.\3.\3.\3/\3/")
        buf.write(u"\3/\7/\u018f\n/\f/\16/\u0192\13/\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01a1")
        buf.write(u"\n\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\7\60\u01b7\n\60\f\60\16\60\u01ba\13\60\3\61\3\61\3\61")
        buf.write(u"\3\62\3\62\3\62\3\62\3\63\3\63\3\63\5\63\u01c6\n\63\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\7\64\u01d3\n\64\f\64\16\64\u01d6\13\64\3\65\3\65\3\65")
        buf.write(u"\5\65\u01db\n\65\3\65\5\65\u01de\n\65\3\66\3\66\3\66")
        buf.write(u"\5\66\u01e3\n\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3")
        buf.write(u"<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3A\2\4^fB\2\4\6\b")
        buf.write(u"\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write(u"8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\2\t\3\2\17")
        buf.write(u"\20\3\2\21\23\4\2\17\17\24\24\3\2\25\30\3\2\31\32\3\2")
        buf.write(u"\33\34\4\2\n\n\35!\u01f6\2\u0088\3\2\2\2\4\u008b\3\2")
        buf.write(u"\2\2\6\u008f\3\2\2\2\b\u0098\3\2\2\2\n\u009c\3\2\2\2")
        buf.write(u"\f\u00a7\3\2\2\2\16\u00a9\3\2\2\2\20\u00ba\3\2\2\2\22")
        buf.write(u"\u00bf\3\2\2\2\24\u00c3\3\2\2\2\26\u00c6\3\2\2\2\30\u00cc")
        buf.write(u"\3\2\2\2\32\u00d9\3\2\2\2\34\u00de\3\2\2\2\36\u00e2\3")
        buf.write(u"\2\2\2 \u00e8\3\2\2\2\"\u00f0\3\2\2\2$\u00f6\3\2\2\2")
        buf.write(u"&\u00fb\3\2\2\2(\u00fd\3\2\2\2*\u00ff\3\2\2\2,\u0101")
        buf.write(u"\3\2\2\2.\u0103\3\2\2\2\60\u0105\3\2\2\2\62\u0107\3\2")
        buf.write(u"\2\2\64\u010d\3\2\2\2\66\u010f\3\2\2\28\u0117\3\2\2\2")
        buf.write(u":\u0120\3\2\2\2<\u012c\3\2\2\2>\u012e\3\2\2\2@\u0131")
        buf.write(u"\3\2\2\2B\u0135\3\2\2\2D\u013b\3\2\2\2F\u014d\3\2\2\2")
        buf.write(u"H\u0151\3\2\2\2J\u0153\3\2\2\2L\u0161\3\2\2\2N\u0167")
        buf.write(u"\3\2\2\2P\u016a\3\2\2\2R\u016d\3\2\2\2T\u0172\3\2\2\2")
        buf.write(u"V\u0175\3\2\2\2X\u0181\3\2\2\2Z\u0184\3\2\2\2\\\u018b")
        buf.write(u"\3\2\2\2^\u01a0\3\2\2\2`\u01bb\3\2\2\2b\u01be\3\2\2\2")
        buf.write(u"d\u01c5\3\2\2\2f\u01c7\3\2\2\2h\u01dd\3\2\2\2j\u01e2")
        buf.write(u"\3\2\2\2l\u01e4\3\2\2\2n\u01e6\3\2\2\2p\u01e8\3\2\2\2")
        buf.write(u"r\u01ea\3\2\2\2t\u01ec\3\2\2\2v\u01ee\3\2\2\2x\u01f0")
        buf.write(u"\3\2\2\2z\u01f2\3\2\2\2|\u01f4\3\2\2\2~\u01f6\3\2\2\2")
        buf.write(u"\u0080\u01f8\3\2\2\2\u0082\u0087\5\24\13\2\u0083\u0087")
        buf.write(u"\5\b\5\2\u0084\u0087\5\4\3\2\u0085\u0087\5:\36\2\u0086")
        buf.write(u"\u0082\3\2\2\2\u0086\u0083\3\2\2\2\u0086\u0084\3\2\2")
        buf.write(u"\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086")
        buf.write(u"\3\2\2\2\u0088\u0089\3\2\2\2\u0089\3\3\2\2\2\u008a\u0088")
        buf.write(u"\3\2\2\2\u008b\u008c\7&\2\2\u008c\u008d\5(\25\2\u008d")
        buf.write(u"\u008e\5\6\4\2\u008e\5\3\2\2\2\u008f\u0093\7\3\2\2\u0090")
        buf.write(u"\u0092\5\24\13\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2")
        buf.write(u"\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096")
        buf.write(u"\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7\4\2\2\u0097")
        buf.write(u"\7\3\2\2\2\u0098\u0099\7/\2\2\u0099\u009a\5\n\6\2\u009a")
        buf.write(u"\u009b\5\16\b\2\u009b\t\3\2\2\2\u009c\u009d\5\u0080A")
        buf.write(u"\2\u009d\u009f\7\5\2\2\u009e\u00a0\5\20\t\2\u009f\u009e")
        buf.write(u"\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write(u"\u00a2\7\6\2\2\u00a2\u00a3\7\7\2\2\u00a3\u00a4\5\f\7")
        buf.write(u"\2\u00a4\13\3\2\2\2\u00a5\u00a8\5$\23\2\u00a6\u00a8\5")
        buf.write(u"\60\31\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write(u"\r\3\2\2\2\u00a9\u00ad\7\3\2\2\u00aa\u00ac\5<\37\2\u00ab")
        buf.write(u"\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2")
        buf.write(u"\2\u00ad\u00ae\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write(u"\3\2\2\2\u00b0\u00b2\5> \2\u00b1\u00b0\3\2\2\2\u00b1")
        buf.write(u"\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7\4\2")
        buf.write(u"\2\u00b4\17\3\2\2\2\u00b5\u00b6\5\22\n\2\u00b6\u00b7")
        buf.write(u"\7\b\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b9")
        buf.write(u"\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write(u"\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be")
        buf.write(u"\5\22\n\2\u00be\21\3\2\2\2\u00bf\u00c0\5\u0080A\2\u00c0")
        buf.write(u"\u00c1\7\7\2\2\u00c1\u00c2\5$\23\2\u00c2\23\3\2\2\2\u00c3")
        buf.write(u"\u00c4\5\26\f\2\u00c4\u00c5\7\t\2\2\u00c5\25\3\2\2\2")
        buf.write(u"\u00c6\u00c7\5$\23\2\u00c7\u00ca\5\u0080A\2\u00c8\u00c9")
        buf.write(u"\7\n\2\2\u00c9\u00cb\5^\60\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write(u"\u00cb\3\2\2\2\u00cb\27\3\2\2\2\u00cc\u00cd\7\13\2\2")
        buf.write(u"\u00cd\u00ce\5\u0080A\2\u00ce\u00d0\7\5\2\2\u00cf\u00d1")
        buf.write(u"\5\32\16\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write(u"\u00d2\3\2\2\2\u00d2\u00d3\7\6\2\2\u00d3\31\3\2\2\2\u00d4")
        buf.write(u"\u00d5\5\34\17\2\u00d5\u00d6\7\b\2\2\u00d6\u00d8\3\2")
        buf.write(u"\2\2\u00d7\u00d4\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7")
        buf.write(u"\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db")
        buf.write(u"\u00d9\3\2\2\2\u00dc\u00dd\5\34\17\2\u00dd\33\3\2\2\2")
        buf.write(u"\u00de\u00df\5\u0080A\2\u00df\u00e0\7\n\2\2\u00e0\u00e1")
        buf.write(u"\5^\60\2\u00e1\35\3\2\2\2\u00e2\u00e4\7\f\2\2\u00e3\u00e5")
        buf.write(u"\5 \21\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write(u"\u00e6\3\2\2\2\u00e6\u00e7\7\r\2\2\u00e7\37\3\2\2\2\u00e8")
        buf.write(u"\u00ed\5^\60\2\u00e9\u00ea\7\b\2\2\u00ea\u00ec\5^\60")
        buf.write(u"\2\u00eb\u00e9\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb")
        buf.write(u"\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee!\3\2\2\2\u00ef\u00ed")
        buf.write(u"\3\2\2\2\u00f0\u00f1\7\60\2\2\u00f1\u00f2\7\t\2\2\u00f2")
        buf.write(u"#\3\2\2\2\u00f3\u00f7\5&\24\2\u00f4\u00f7\5\62\32\2\u00f5")
        buf.write(u"\u00f7\5(\25\2\u00f6\u00f3\3\2\2\2\u00f6\u00f4\3\2\2")
        buf.write(u"\2\u00f6\u00f5\3\2\2\2\u00f7%\3\2\2\2\u00f8\u00fc\5*")
        buf.write(u"\26\2\u00f9\u00fc\5,\27\2\u00fa\u00fc\5.\30\2\u00fb\u00f8")
        buf.write(u"\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write(u"\'\3\2\2\2\u00fd\u00fe\7\61\2\2\u00fe)\3\2\2\2\u00ff")
        buf.write(u"\u0100\7#\2\2\u0100+\3\2\2\2\u0101\u0102\7$\2\2\u0102")
        buf.write(u"-\3\2\2\2\u0103\u0104\7\"\2\2\u0104/\3\2\2\2\u0105\u0106")
        buf.write(u"\7%\2\2\u0106\61\3\2\2\2\u0107\u0108\7\f\2\2\u0108\u0109")
        buf.write(u"\5\66\34\2\u0109\u010a\7\r\2\2\u010a\63\3\2\2\2\u010b")
        buf.write(u"\u010e\5&\24\2\u010c\u010e\5\62\32\2\u010d\u010b\3\2")
        buf.write(u"\2\2\u010d\u010c\3\2\2\2\u010e\65\3\2\2\2\u010f\u0114")
        buf.write(u"\5\64\33\2\u0110\u0111\7\b\2\2\u0111\u0113\5\64\33\2")
        buf.write(u"\u0112\u0110\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112")
        buf.write(u"\3\2\2\2\u0114\u0115\3\2\2\2\u0115\67\3\2\2\2\u0116\u0114")
        buf.write(u"\3\2\2\2\u0117\u011b\7\3\2\2\u0118\u011a\5<\37\2\u0119")
        buf.write(u"\u0118\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2")
        buf.write(u"\2\u011b\u011c\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b")
        buf.write(u"\3\2\2\2\u011e\u011f\7\4\2\2\u011f9\3\2\2\2\u0120\u0121")
        buf.write(u"\58\35\2\u0121;\3\2\2\2\u0122\u012d\5:\36\2\u0123\u012d")
        buf.write(u"\5\24\13\2\u0124\u012d\5`\61\2\u0125\u012d\5J&\2\u0126")
        buf.write(u"\u012d\5X-\2\u0127\u012d\5D#\2\u0128\u012d\5B\"\2\u0129")
        buf.write(u"\u012d\5\"\22\2\u012a\u012d\5T+\2\u012b\u012d\5P)\2\u012c")
        buf.write(u"\u0122\3\2\2\2\u012c\u0123\3\2\2\2\u012c\u0124\3\2\2")
        buf.write(u"\2\u012c\u0125\3\2\2\2\u012c\u0126\3\2\2\2\u012c\u0127")
        buf.write(u"\3\2\2\2\u012c\u0128\3\2\2\2\u012c\u0129\3\2\2\2\u012c")
        buf.write(u"\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d=\3\2\2\2\u012e")
        buf.write(u"\u012f\5@!\2\u012f\u0130\7\t\2\2\u0130?\3\2\2\2\u0131")
        buf.write(u"\u0133\7.\2\2\u0132\u0134\5^\60\2\u0133\u0132\3\2\2\2")
        buf.write(u"\u0133\u0134\3\2\2\2\u0134A\3\2\2\2\u0135\u0136\7+\2")
        buf.write(u"\2\u0136\u0137\7\5\2\2\u0137\u0138\5^\60\2\u0138\u0139")
        buf.write(u"\7\6\2\2\u0139\u013a\58\35\2\u013aC\3\2\2\2\u013b\u013c")
        buf.write(u"\7*\2\2\u013c\u013e\7\5\2\2\u013d\u013f\5F$\2\u013e\u013d")
        buf.write(u"\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write(u"\u0142\7\t\2\2\u0141\u0143\5^\60\2\u0142\u0141\3\2\2")
        buf.write(u"\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146")
        buf.write(u"\7\t\2\2\u0145\u0147\5H%\2\u0146\u0145\3\2\2\2\u0146")
        buf.write(u"\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\7\6\2")
        buf.write(u"\2\u0149\u014a\58\35\2\u014aE\3\2\2\2\u014b\u014e\5b")
        buf.write(u"\62\2\u014c\u014e\5\26\f\2\u014d\u014b\3\2\2\2\u014d")
        buf.write(u"\u014c\3\2\2\2\u014eG\3\2\2\2\u014f\u0152\5b\62\2\u0150")
        buf.write(u"\u0152\5Z.\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2")
        buf.write(u"\u0152I\3\2\2\2\u0153\u0154\7,\2\2\u0154\u0155\7\5\2")
        buf.write(u"\2\u0155\u0156\5^\60\2\u0156\u0157\7\6\2\2\u0157\u015b")
        buf.write(u"\5:\36\2\u0158\u015a\5L\'\2\u0159\u0158\3\2\2\2\u015a")
        buf.write(u"\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2")
        buf.write(u"\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0160")
        buf.write(u"\5N(\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write(u"K\3\2\2\2\u0161\u0162\7-\2\2\u0162\u0163\7\5\2\2\u0163")
        buf.write(u"\u0164\5^\60\2\u0164\u0165\7\6\2\2\u0165\u0166\5:\36")
        buf.write(u"\2\u0166M\3\2\2\2\u0167\u0168\7)\2\2\u0168\u0169\5:\36")
        buf.write(u"\2\u0169O\3\2\2\2\u016a\u016b\5R*\2\u016b\u016c\7\t\2")
        buf.write(u"\2\u016cQ\3\2\2\2\u016d\u016e\7\'\2\2\u016e\u016f\7\5")
        buf.write(u"\2\2\u016f\u0170\5\\/\2\u0170\u0171\7\6\2\2\u0171S\3")
        buf.write(u"\2\2\2\u0172\u0173\5V,\2\u0173\u0174\7\t\2\2\u0174U\3")
        buf.write(u"\2\2\2\u0175\u0176\7(\2\2\u0176\u0177\7\5\2\2\u0177\u017c")
        buf.write(u"\5d\63\2\u0178\u0179\7\b\2\2\u0179\u017b\5d\63\2\u017a")
        buf.write(u"\u0178\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2")
        buf.write(u"\2\u017c\u017d\3\2\2\2\u017d\u017f\3\2\2\2\u017e\u017c")
        buf.write(u"\3\2\2\2\u017f\u0180\7\6\2\2\u0180W\3\2\2\2\u0181\u0182")
        buf.write(u"\5Z.\2\u0182\u0183\7\t\2\2\u0183Y\3\2\2\2\u0184\u0185")
        buf.write(u"\5\u0080A\2\u0185\u0187\7\5\2\2\u0186\u0188\5\\/\2\u0187")
        buf.write(u"\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2")
        buf.write(u"\2\u0189\u018a\7\6\2\2\u018a[\3\2\2\2\u018b\u0190\5^")
        buf.write(u"\60\2\u018c\u018d\7\b\2\2\u018d\u018f\5^\60\2\u018e\u018c")
        buf.write(u"\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write(u"\u0191\3\2\2\2\u0191]\3\2\2\2\u0192\u0190\3\2\2\2\u0193")
        buf.write(u"\u0194\b\60\1\2\u0194\u0195\5r:\2\u0195\u0196\5^\60\16")
        buf.write(u"\u0196\u01a1\3\2\2\2\u0197\u01a1\5Z.\2\u0198\u01a1\5")
        buf.write(u"j\66\2\u0199\u01a1\5\36\20\2\u019a\u01a1\5\30\r\2\u019b")
        buf.write(u"\u01a1\5d\63\2\u019c\u019d\7\5\2\2\u019d\u019e\5^\60")
        buf.write(u"\2\u019e\u019f\7\6\2\2\u019f\u01a1\3\2\2\2\u01a0\u0193")
        buf.write(u"\3\2\2\2\u01a0\u0197\3\2\2\2\u01a0\u0198\3\2\2\2\u01a0")
        buf.write(u"\u0199\3\2\2\2\u01a0\u019a\3\2\2\2\u01a0\u019b\3\2\2")
        buf.write(u"\2\u01a0\u019c\3\2\2\2\u01a1\u01b8\3\2\2\2\u01a2\u01a3")
        buf.write(u"\f\r\2\2\u01a3\u01a4\5t;\2\u01a4\u01a5\5^\60\16\u01a5")
        buf.write(u"\u01b7\3\2\2\2\u01a6\u01a7\f\f\2\2\u01a7\u01a8\5v<\2")
        buf.write(u"\u01a8\u01a9\5^\60\r\u01a9\u01b7\3\2\2\2\u01aa\u01ab")
        buf.write(u"\f\13\2\2\u01ab\u01ac\5x=\2\u01ac\u01ad\5^\60\f\u01ad")
        buf.write(u"\u01b7\3\2\2\2\u01ae\u01af\f\n\2\2\u01af\u01b0\5z>\2")
        buf.write(u"\u01b0\u01b1\5^\60\13\u01b1\u01b7\3\2\2\2\u01b2\u01b3")
        buf.write(u"\f\t\2\2\u01b3\u01b4\5|?\2\u01b4\u01b5\5^\60\n\u01b5")
        buf.write(u"\u01b7\3\2\2\2\u01b6\u01a2\3\2\2\2\u01b6\u01a6\3\2\2")
        buf.write(u"\2\u01b6\u01aa\3\2\2\2\u01b6\u01ae\3\2\2\2\u01b6\u01b2")
        buf.write(u"\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write(u"\u01b9\3\2\2\2\u01b9_\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write(u"\u01bc\5b\62\2\u01bc\u01bd\7\t\2\2\u01bda\3\2\2\2\u01be")
        buf.write(u"\u01bf\5d\63\2\u01bf\u01c0\5~@\2\u01c0\u01c1\5^\60\2")
        buf.write(u"\u01c1c\3\2\2\2\u01c2\u01c6\5\u0080A\2\u01c3\u01c6\5")
        buf.write(u"h\65\2\u01c4\u01c6\5f\64\2\u01c5\u01c2\3\2\2\2\u01c5")
        buf.write(u"\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6e\3\2\2\2\u01c7")
        buf.write(u"\u01c8\b\64\1\2\u01c8\u01c9\5\u0080A\2\u01c9\u01ca\7")
        buf.write(u"\f\2\2\u01ca\u01cb\5l\67\2\u01cb\u01cc\7\r\2\2\u01cc")
        buf.write(u"\u01d4\3\2\2\2\u01cd\u01ce\f\4\2\2\u01ce\u01cf\7\f\2")
        buf.write(u"\2\u01cf\u01d0\5l\67\2\u01d0\u01d1\7\r\2\2\u01d1\u01d3")
        buf.write(u"\3\2\2\2\u01d2\u01cd\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write(u"\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5g\3\2\2\2\u01d6")
        buf.write(u"\u01d4\3\2\2\2\u01d7\u01da\5\u0080A\2\u01d8\u01d9\7\16")
        buf.write(u"\2\2\u01d9\u01db\5h\65\2\u01da\u01d8\3\2\2\2\u01da\u01db")
        buf.write(u"\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01de\5f\64\2\u01dd")
        buf.write(u"\u01d7\3\2\2\2\u01dd\u01dc\3\2\2\2\u01dei\3\2\2\2\u01df")
        buf.write(u"\u01e3\5l\67\2\u01e0\u01e3\5n8\2\u01e1\u01e3\5p9\2\u01e2")
        buf.write(u"\u01df\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2")
        buf.write(u"\2\u01e3k\3\2\2\2\u01e4\u01e5\7\64\2\2\u01e5m\3\2\2\2")
        buf.write(u"\u01e6\u01e7\7\63\2\2\u01e7o\3\2\2\2\u01e8\u01e9\7\62")
        buf.write(u"\2\2\u01e9q\3\2\2\2\u01ea\u01eb\t\2\2\2\u01ebs\3\2\2")
        buf.write(u"\2\u01ec\u01ed\t\3\2\2\u01edu\3\2\2\2\u01ee\u01ef\t\4")
        buf.write(u"\2\2\u01efw\3\2\2\2\u01f0\u01f1\t\5\2\2\u01f1y\3\2\2")
        buf.write(u"\2\u01f2\u01f3\t\6\2\2\u01f3{\3\2\2\2\u01f4\u01f5\t\7")
        buf.write(u"\2\2\u01f5}\3\2\2\2\u01f6\u01f7\t\b\2\2\u01f7\177\3\2")
        buf.write(u"\2\2\u01f8\u01f9\7\61\2\2\u01f9\u0081\3\2\2\2(\u0086")
        buf.write(u"\u0088\u0093\u009f\u00a7\u00ad\u00b1\u00ba\u00ca\u00d0")
        buf.write(u"\u00d9\u00e4\u00ed\u00f6\u00fb\u010d\u0114\u011b\u012c")
        buf.write(u"\u0133\u013e\u0142\u0146\u014d\u0151\u015b\u015f\u017c")
        buf.write(u"\u0187\u0190\u01a0\u01b6\u01b8\u01c5\u01d4\u01da\u01dd")
        buf.write(u"\u01e2")
        return buf.getvalue()
		

class LLangParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"'('", u"')'", u"':'", 
                     u"','", u"';'", u"'='", u"'new'", u"'['", u"']'", u"'.'", 
                     u"'-'", u"'!'", u"'*'", u"'/'", u"'%'", u"'+'", u"'>'", 
                     u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", u"'&&'", 
                     u"'||'", u"'*='", u"'/='", u"'%='", u"'+='", u"'-='", 
                     u"'Bool'", u"'Int'", u"'Str'", u"'None'", u"'record'", 
                     u"'writeln'", u"'readln'", u"'else'", u"'for'", u"'while'", 
                     u"'if'", u"'elif'", u"'return'", u"'fun'", u"'pass'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"BOOL", u"INT", u"STR", u"NONE", u"RECORD", u"WRITELN", 
                      u"READLN", u"ELSE", u"FOR", u"WHILE", u"IF", u"ELIF", 
                      u"RETURN", u"FUN", u"PASS", u"Identifier", u"BooleanLiteral", 
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
    RULE_recordInitializer = 11
    RULE_recordFieldInitializerList = 12
    RULE_recordFieldInitializer = 13
    RULE_cortegeInitializer = 14
    RULE_expressionList = 15
    RULE_passStatement = 16
    RULE_exprType = 17
    RULE_primitiveType = 18
    RULE_recordId = 19
    RULE_intType = 20
    RULE_strType = 21
    RULE_boolType = 22
    RULE_voidType = 23
    RULE_cortegeType = 24
    RULE_cortegeTypeUnit = 25
    RULE_cortegeTypeNonEmptyList = 26
    RULE_block = 27
    RULE_justBlock = 28
    RULE_statement = 29
    RULE_returnStatement = 30
    RULE_returnExpr = 31
    RULE_whileStatement = 32
    RULE_forStatement = 33
    RULE_forInit = 34
    RULE_forUpdate = 35
    RULE_ifStatement = 36
    RULE_elifBlock = 37
    RULE_elseBlock = 38
    RULE_writelnStatement = 39
    RULE_writelnCall = 40
    RULE_readlnStatement = 41
    RULE_readlnCall = 42
    RULE_functionInvocationStatement = 43
    RULE_functionInvocation = 44
    RULE_argumentList = 45
    RULE_expression = 46
    RULE_assignmentStatement = 47
    RULE_assignment = 48
    RULE_leftHandSide = 49
    RULE_cortegeAccess = 50
    RULE_recordFieldAccess = 51
    RULE_literal = 52
    RULE_intLiteral = 53
    RULE_strLiteral = 54
    RULE_boolLiteral = 55
    RULE_unaryOperator = 56
    RULE_mulDivModOperator = 57
    RULE_addSubOperator = 58
    RULE_compareOperator = 59
    RULE_equalOrNotOperator = 60
    RULE_boolOperator = 61
    RULE_assignmentOperator = 62
    RULE_identifier = 63

    ruleNames =  [ u"programme", u"recordDeclaration", u"recordBody", u"functionDeclaration", 
                   u"functionSignature", u"functionReturnType", u"functionBody", 
                   u"functionParameterList", u"functionParameter", u"variableDeclarationStatement", 
                   u"variableDeclaration", u"recordInitializer", u"recordFieldInitializerList", 
                   u"recordFieldInitializer", u"cortegeInitializer", u"expressionList", 
                   u"passStatement", u"exprType", u"primitiveType", u"recordId", 
                   u"intType", u"strType", u"boolType", u"voidType", u"cortegeType", 
                   u"cortegeTypeUnit", u"cortegeTypeNonEmptyList", u"block", 
                   u"justBlock", u"statement", u"returnStatement", u"returnExpr", 
                   u"whileStatement", u"forStatement", u"forInit", u"forUpdate", 
                   u"ifStatement", u"elifBlock", u"elseBlock", u"writelnStatement", 
                   u"writelnCall", u"readlnStatement", u"readlnCall", u"functionInvocationStatement", 
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
    T__30=31
    BOOL=32
    INT=33
    STR=34
    NONE=35
    RECORD=36
    WRITELN=37
    READLN=38
    ELSE=39
    FOR=40
    WHILE=41
    IF=42
    ELIF=43
    RETURN=44
    FUN=45
    PASS=46
    Identifier=47
    BooleanLiteral=48
    StringLiteral=49
    IntegerLiteral=50
    WS=51
    COMMENT=52
    LINE_COMMENT=53

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


        def justBlock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.JustBlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.JustBlockContext,i)


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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.RECORD) | (1 << LLangParser.FUN) | (1 << LLangParser.Identifier))) != 0):
                self.state = 132
                token = self._input.LA(1)
                if token in [LLangParser.T__9, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                    self.state = 128 
                    self.variableDeclarationStatement()

                elif token in [LLangParser.FUN]:
                    self.state = 129 
                    self.functionDeclaration()

                elif token in [LLangParser.RECORD]:
                    self.state = 130 
                    self.recordDeclaration()

                elif token in [LLangParser.T__0]:
                    self.state = 131 
                    self.justBlock()

                else:
                    raise NoViableAltException(self)

                self.state = 136
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

        def recordId(self):
            return self.getTypedRuleContext(LLangParser.RecordIdContext,0)


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
            self.state = 137
            self.match(LLangParser.RECORD)
            self.state = 138 
            self.recordId()
            self.state = 139 
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
            self.state = 141
            self.match(LLangParser.T__0)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 142 
                self.variableDeclarationStatement()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
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
            self.state = 150
            self.match(LLangParser.FUN)
            self.state = 151 
            self.functionSignature()
            self.state = 152 
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
            self.state = 154 
            self.identifier()
            self.state = 155
            self.match(LLangParser.T__2)
            self.state = 157
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 156 
                self.functionParameterList()


            self.state = 159
            self.match(LLangParser.T__3)
            self.state = 160
            self.match(LLangParser.T__4)
            self.state = 161 
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
            self.state = 165
            token = self._input.LA(1)
            if token in [LLangParser.T__9, LLangParser.BOOL, LLangParser.INT, LLangParser.STR, LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163 
                self.exprType()

            elif token in [LLangParser.NONE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164 
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
            self.state = 167
            self.match(LLangParser.T__0)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 168 
                self.statement()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
            _la = self._input.LA(1)
            if _la==LLangParser.RETURN:
                self.state = 174 
                self.returnStatement()


            self.state = 177
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
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 179 
                    self.functionParameter()
                    self.state = 180
                    self.match(LLangParser.T__5) 
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 187 
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
            self.state = 189 
            self.identifier()
            self.state = 190
            self.match(LLangParser.T__4)
            self.state = 191 
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
            self.state = 193 
            self.variableDeclaration()
            self.state = 194
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


        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


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
            self.state = 196 
            self.exprType()
            self.state = 197 
            self.identifier()
            self.state = 200
            _la = self._input.LA(1)
            if _la==LLangParser.T__7:
                self.state = 198
                self.match(LLangParser.T__7)
                self.state = 199 
                self.expression(0)


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
        self.enterRule(localctx, 22, self.RULE_recordInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(LLangParser.T__8)
            self.state = 203 
            self.identifier()
            self.state = 204
            self.match(LLangParser.T__2)
            self.state = 206
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 205 
                self.recordFieldInitializerList()


            self.state = 208
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
        self.enterRule(localctx, 24, self.RULE_recordFieldInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 210 
                    self.recordFieldInitializer()
                    self.state = 211
                    self.match(LLangParser.T__5) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 218 
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
        self.enterRule(localctx, 26, self.RULE_recordFieldInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220 
            self.identifier()
            self.state = 221
            self.match(LLangParser.T__7)
            self.state = 222 
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

        def expressionList(self):
            return self.getTypedRuleContext(LLangParser.ExpressionListContext,0)


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
        self.enterRule(localctx, 28, self.RULE_cortegeInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(LLangParser.T__9)
            self.state = 226
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 225 
                self.expressionList()


            self.state = 228
            self.match(LLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ExpressionListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_expressionList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterExpressionList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitExpressionList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = LLangParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230 
            self.expression(0)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 231
                self.match(LLangParser.T__5)
                self.state = 232 
                self.expression(0)
                self.state = 237
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
        self.enterRule(localctx, 32, self.RULE_passStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(LLangParser.PASS)
            self.state = 239
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


        def recordId(self):
            return self.getTypedRuleContext(LLangParser.RecordIdContext,0)


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
        self.enterRule(localctx, 34, self.RULE_exprType)
        try:
            self.state = 244
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241 
                self.primitiveType()

            elif token in [LLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242 
                self.cortegeType()

            elif token in [LLangParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 243 
                self.recordId()

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
        self.enterRule(localctx, 36, self.RULE_primitiveType)
        try:
            self.state = 249
            token = self._input.LA(1)
            if token in [LLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246 
                self.intType()

            elif token in [LLangParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247 
                self.strType()

            elif token in [LLangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248 
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

    class RecordIdContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordIdContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LLangParser.Identifier, 0)

        def getRuleIndex(self):
            return LLangParser.RULE_recordId

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterRecordId(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitRecordId(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitRecordId(self)
            else:
                return visitor.visitChildren(self)




    def recordId(self):

        localctx = LLangParser.RecordIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_recordId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
        self.enterRule(localctx, 40, self.RULE_intType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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
        self.enterRule(localctx, 42, self.RULE_strType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
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
        self.enterRule(localctx, 44, self.RULE_boolType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
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
        self.enterRule(localctx, 46, self.RULE_voidType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
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

        def cortegeTypeNonEmptyList(self):
            return self.getTypedRuleContext(LLangParser.CortegeTypeNonEmptyListContext,0)


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
        self.enterRule(localctx, 48, self.RULE_cortegeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(LLangParser.T__9)
            self.state = 262 
            self.cortegeTypeNonEmptyList()
            self.state = 263
            self.match(LLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeTypeUnitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeTypeUnitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(LLangParser.PrimitiveTypeContext,0)


        def cortegeType(self):
            return self.getTypedRuleContext(LLangParser.CortegeTypeContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeTypeUnit

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeTypeUnit(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeTypeUnit(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeTypeUnit(self)
            else:
                return visitor.visitChildren(self)




    def cortegeTypeUnit(self):

        localctx = LLangParser.CortegeTypeUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cortegeTypeUnit)
        try:
            self.state = 267
            token = self._input.LA(1)
            if token in [LLangParser.BOOL, LLangParser.INT, LLangParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265 
                self.primitiveType()

            elif token in [LLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266 
                self.cortegeType()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CortegeTypeNonEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.CortegeTypeNonEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def cortegeTypeUnit(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.CortegeTypeUnitContext)
            else:
                return self.getTypedRuleContext(LLangParser.CortegeTypeUnitContext,i)


        def getRuleIndex(self):
            return LLangParser.RULE_cortegeTypeNonEmptyList

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterCortegeTypeNonEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitCortegeTypeNonEmptyList(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitCortegeTypeNonEmptyList(self)
            else:
                return visitor.visitChildren(self)




    def cortegeTypeNonEmptyList(self):

        localctx = LLangParser.CortegeTypeNonEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_cortegeTypeNonEmptyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269 
            self.cortegeTypeUnit()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 270
                self.match(LLangParser.T__5)
                self.state = 271 
                self.cortegeTypeUnit()
                self.state = 276
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
            self.state = 277
            self.match(LLangParser.T__0)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__0) | (1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.WRITELN) | (1 << LLangParser.READLN) | (1 << LLangParser.FOR) | (1 << LLangParser.WHILE) | (1 << LLangParser.IF) | (1 << LLangParser.PASS) | (1 << LLangParser.Identifier))) != 0):
                self.state = 278 
                self.statement()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 284
            self.match(LLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JustBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.JustBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LLangParser.BlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_justBlock

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterJustBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitJustBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitJustBlock(self)
            else:
                return visitor.visitChildren(self)




    def justBlock(self):

        localctx = LLangParser.JustBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_justBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286 
            self.block()
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

        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


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
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 298
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288 
                self.justBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289 
                self.variableDeclarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290 
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291 
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 292 
                self.functionInvocationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 293 
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 294 
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 295 
                self.passStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 296 
                self.readlnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 297 
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
        self.enterRule(localctx, 60, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300 
            self.returnExpr()
            self.state = 301
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
        self.enterRule(localctx, 62, self.RULE_returnExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(LLangParser.RETURN)
            self.state = 305
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 304 
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
        self.enterRule(localctx, 64, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(LLangParser.WHILE)
            self.state = 308
            self.match(LLangParser.T__2)
            self.state = 309 
            self.expression(0)
            self.state = 310
            self.match(LLangParser.T__3)
            self.state = 311 
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
        self.enterRule(localctx, 66, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(LLangParser.FOR)
            self.state = 314
            self.match(LLangParser.T__2)
            self.state = 316
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__9) | (1 << LLangParser.BOOL) | (1 << LLangParser.INT) | (1 << LLangParser.STR) | (1 << LLangParser.Identifier))) != 0):
                self.state = 315 
                self.forInit()


            self.state = 318
            self.match(LLangParser.T__6)
            self.state = 320
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 319 
                self.expression(0)


            self.state = 322
            self.match(LLangParser.T__6)
            self.state = 324
            _la = self._input.LA(1)
            if _la==LLangParser.Identifier:
                self.state = 323 
                self.forUpdate()


            self.state = 326
            self.match(LLangParser.T__3)
            self.state = 327 
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
        self.enterRule(localctx, 68, self.RULE_forInit)
        try:
            self.state = 331
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330 
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
        self.enterRule(localctx, 70, self.RULE_forUpdate)
        try:
            self.state = 335
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333 
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334 
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

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def elifBlock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LLangParser.ElifBlockContext)
            else:
                return self.getTypedRuleContext(LLangParser.ElifBlockContext,i)


        def elseBlock(self):
            return self.getTypedRuleContext(LLangParser.ElseBlockContext,0)


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
        self.enterRule(localctx, 72, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(LLangParser.IF)
            self.state = 338
            self.match(LLangParser.T__2)
            self.state = 339 
            self.expression(0)
            self.state = 340
            self.match(LLangParser.T__3)
            self.state = 341 
            self.justBlock()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.ELIF:
                self.state = 342 
                self.elifBlock()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
            _la = self._input.LA(1)
            if _la==LLangParser.ELSE:
                self.state = 348 
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElifBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ElifBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(LLangParser.ELIF, 0)

        def expression(self):
            return self.getTypedRuleContext(LLangParser.ExpressionContext,0)


        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_elifBlock

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterElifBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitElifBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitElifBlock(self)
            else:
                return visitor.visitChildren(self)




    def elifBlock(self):

        localctx = LLangParser.ElifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(LLangParser.ELIF)
            self.state = 352
            self.match(LLangParser.T__2)
            self.state = 353 
            self.expression(0)
            self.state = 354
            self.match(LLangParser.T__3)
            self.state = 355 
            self.justBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.ElseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LLangParser.ELSE, 0)

        def justBlock(self):
            return self.getTypedRuleContext(LLangParser.JustBlockContext,0)


        def getRuleIndex(self):
            return LLangParser.RULE_elseBlock

        def enterRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.enterElseBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LLangListener ):
                listener.exitElseBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, LLangVisitor ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = LLangParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(LLangParser.ELSE)
            self.state = 358 
            self.justBlock()
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
        self.enterRule(localctx, 78, self.RULE_writelnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360 
            self.writelnCall()
            self.state = 361
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
        self.enterRule(localctx, 80, self.RULE_writelnCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(LLangParser.WRITELN)
            self.state = 364
            self.match(LLangParser.T__2)
            self.state = 365 
            self.argumentList()
            self.state = 366
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
        self.enterRule(localctx, 82, self.RULE_readlnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368 
            self.readlnCall()
            self.state = 369
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
        self.enterRule(localctx, 84, self.RULE_readlnCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(LLangParser.READLN)
            self.state = 372
            self.match(LLangParser.T__2)
            self.state = 373 
            self.leftHandSide()
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 374
                self.match(LLangParser.T__5)
                self.state = 375 
                self.leftHandSide()
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 381
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
        self.enterRule(localctx, 86, self.RULE_functionInvocationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383 
            self.functionInvocation()
            self.state = 384
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
        self.enterRule(localctx, 88, self.RULE_functionInvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386 
            self.identifier()
            self.state = 387
            self.match(LLangParser.T__2)
            self.state = 389
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__2) | (1 << LLangParser.T__8) | (1 << LLangParser.T__9) | (1 << LLangParser.T__12) | (1 << LLangParser.T__13) | (1 << LLangParser.Identifier) | (1 << LLangParser.BooleanLiteral) | (1 << LLangParser.StringLiteral) | (1 << LLangParser.IntegerLiteral))) != 0):
                self.state = 388 
                self.argumentList()


            self.state = 391
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
        self.enterRule(localctx, 90, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393 
            self.expression(0)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LLangParser.T__5:
                self.state = 394
                self.match(LLangParser.T__5)
                self.state = 395 
                self.expression(0)
                self.state = 400
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


        def functionInvocation(self):
            return self.getTypedRuleContext(LLangParser.FunctionInvocationContext,0)


        def literal(self):
            return self.getTypedRuleContext(LLangParser.LiteralContext,0)


        def cortegeInitializer(self):
            return self.getTypedRuleContext(LLangParser.CortegeInitializerContext,0)


        def recordInitializer(self):
            return self.getTypedRuleContext(LLangParser.RecordInitializerContext,0)


        def leftHandSide(self):
            return self.getTypedRuleContext(LLangParser.LeftHandSideContext,0)


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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 402 
                self.unaryOperator()
                self.state = 403 
                self.expression(12)
                pass

            elif la_ == 2:
                self.state = 405 
                self.functionInvocation()
                pass

            elif la_ == 3:
                self.state = 406 
                self.literal()
                pass

            elif la_ == 4:
                self.state = 407 
                self.cortegeInitializer()
                pass

            elif la_ == 5:
                self.state = 408 
                self.recordInitializer()
                pass

            elif la_ == 6:
                self.state = 409 
                self.leftHandSide()
                pass

            elif la_ == 7:
                self.state = 410
                self.match(LLangParser.T__2)
                self.state = 411 
                self.expression(0)
                self.state = 412
                self.match(LLangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 436
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 416
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 417 
                        self.mulDivModOperator()
                        self.state = 418 
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 420
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 421 
                        self.addSubOperator()
                        self.state = 422 
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 424
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 425 
                        self.compareOperator()
                        self.state = 426 
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 428
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 429 
                        self.equalOrNotOperator()
                        self.state = 430 
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = LLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 432
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 433 
                        self.boolOperator()
                        self.state = 434 
                        self.expression(8)
                        pass

             
                self.state = 440
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
        self.enterRule(localctx, 94, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441 
            self.assignment()
            self.state = 442
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
        self.enterRule(localctx, 96, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444 
            self.leftHandSide()
            self.state = 445 
            self.assignmentOperator()
            self.state = 446 
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


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


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
        self.enterRule(localctx, 98, self.RULE_leftHandSide)
        try:
            self.state = 451
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448 
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449 
                self.recordFieldAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 450 
                self.cortegeAccess(0)
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


        def intLiteral(self):
            return self.getTypedRuleContext(LLangParser.IntLiteralContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


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



    def cortegeAccess(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LLangParser.CortegeAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_cortegeAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454 
            self.identifier()
            self.state = 455
            self.match(LLangParser.T__9)
            self.state = 456 
            self.intLiteral()
            self.state = 457
            self.match(LLangParser.T__10)
            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LLangParser.CortegeAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cortegeAccess)
                    self.state = 459
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 460
                    self.match(LLangParser.T__9)
                    self.state = 461 
                    self.intLiteral()
                    self.state = 462
                    self.match(LLangParser.T__10) 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RecordFieldAccessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LLangParser.RecordFieldAccessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LLangParser.IdentifierContext,0)


        def recordFieldAccess(self):
            return self.getTypedRuleContext(LLangParser.RecordFieldAccessContext,0)


        def cortegeAccess(self):
            return self.getTypedRuleContext(LLangParser.CortegeAccessContext,0)


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
        self.enterRule(localctx, 102, self.RULE_recordFieldAccess)
        try:
            self.state = 475
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469 
                self.identifier()
                self.state = 472
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 470
                    self.match(LLangParser.T__11)
                    self.state = 471 
                    self.recordFieldAccess()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474 
                self.cortegeAccess(0)
                pass


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
        self.enterRule(localctx, 104, self.RULE_literal)
        try:
            self.state = 480
            token = self._input.LA(1)
            if token in [LLangParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477 
                self.intLiteral()

            elif token in [LLangParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478 
                self.strLiteral()

            elif token in [LLangParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 479 
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
        self.enterRule(localctx, 106, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
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
        self.enterRule(localctx, 108, self.RULE_strLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
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
        self.enterRule(localctx, 110, self.RULE_boolLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
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
        self.enterRule(localctx, 112, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__12 or _la==LLangParser.T__13):
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
        self.enterRule(localctx, 114, self.RULE_mulDivModOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__14) | (1 << LLangParser.T__15) | (1 << LLangParser.T__16))) != 0)):
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
        self.enterRule(localctx, 116, self.RULE_addSubOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__12 or _la==LLangParser.T__17):
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
        self.enterRule(localctx, 118, self.RULE_compareOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__18) | (1 << LLangParser.T__19) | (1 << LLangParser.T__20) | (1 << LLangParser.T__21))) != 0)):
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
        self.enterRule(localctx, 120, self.RULE_equalOrNotOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__22 or _la==LLangParser.T__23):
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
        self.enterRule(localctx, 122, self.RULE_boolOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            _la = self._input.LA(1)
            if not(_la==LLangParser.T__24 or _la==LLangParser.T__25):
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
        self.enterRule(localctx, 124, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LLangParser.T__7) | (1 << LLangParser.T__26) | (1 << LLangParser.T__27) | (1 << LLangParser.T__28) | (1 << LLangParser.T__29) | (1 << LLangParser.T__30))) != 0)):
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
        self.enterRule(localctx, 126, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
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
        self._predicates[46] = self.expression_sempred
        self._predicates[50] = self.cortegeAccess_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

    def cortegeAccess_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         



